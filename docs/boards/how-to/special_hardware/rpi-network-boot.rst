.. _network-boot-a-raspberry-pi:

Network boot a Raspberry Pi
===========================

A Raspberry Pi 5 can boot Ubuntu with no local storage. The boot
:term:`EEPROM` fetches the kernel, initramfs and device tree from a
:term:`TFTP` server, and the initramfs then mounts the root file-system from a
Network Block Device (NBD) exported by a server.

This guide sets up a server for a single Pi, prepares an Ubuntu Server image
for network boot, and boots the Pi from it.

.. note::

    This procedure applies to the Raspberry Pi 5 running Ubuntu Server for
    Raspberry Pi. Other models, and other network root file-systems such as
    NFS or iSCSI, are not covered here.

.. TODO(review): fill in the resolute version once the SRU for LP: #2164978
   is released.

The Pi image needs at least the following version of
:lp-pkg:`ubuntu-raspi-settings`, which adds the drivers the Pi 5 needs to
bring up its Ethernet interface in the initramfs:

* 26.10.3 on Ubuntu 26.10

* 26.04.3 on Ubuntu 26.04 LTS

You will need:

* A Raspberry Pi 5, and a microSD card for the one-time preparation steps

* A server running Ubuntu, with a wired network interface on the same network
  segment as the Pi

* A network segment where the server can act as the :term:`DHCP` server, for
  example a direct cable between the server and the Pi, or a dedicated switch.
  Do not run a second DHCP server on an existing network

* Optionally, a :ref:`UART console <connect-to-a-uart-console>` on the Pi.
  This is the only way to see what happens during a failed network boot

Throughout this guide, the server uses the address 10.0.0.1 and the Pi uses
10.0.0.145. Replace them with addresses suitable for your network.


Overview
--------

The boot proceeds as follows:

1. The Pi's boot EEPROM requests an address over DHCP, and downloads
   :file:`config.txt`, the device tree, the kernel and the initramfs from the
   TFTP server.

2. The initramfs brings up the Ethernet interface with the static address
   given on the kernel command line, and connects to the NBD export holding
   the root file-system.

3. The system switches to the root file-system on the NBD device, and keeps
   the network configuration it was given, so the connection to the root
   file-system is never interrupted.

The boot partition is not used after the boot EEPROM has loaded its files, and
is not mounted on the running system.


Prepare the image
-----------------

The preparation happens once, on the Pi itself, booted from a microSD card.

1. :ref:`Flash <flash-images-to-a-microsd-card>` the Ubuntu Server for
   Raspberry Pi image to a microSD card, boot the Pi from it, and log in.

2. Bring the system up to date, so the package version listed above is
   installed:

   .. code-block:: text

       sudo apt update
       sudo apt full-upgrade

3. Include NBD support in the initramfs. By default, the initramfs only
   includes what is needed to mount the current root file-system, which is on
   the microSD card:

   .. code-block:: text

       echo 'add_dracutmodules+=" nbd "' | sudo tee /etc/dracut.conf.d/90-nbd.conf

4. Keep the network configuration from the initramfs on the running system.
   Create :file:`/etc/netplan/90-network-root.yaml` with the following
   content, replacing the addresses with your own:

   .. code-block:: yaml

       network:
         version: 2
         ethernets:
           eth0:
             dhcp4: false
             addresses: [10.0.0.145/24]
             routes:
               - to: default
                 via: 10.0.0.1
             critical: true

   Then restrict its permissions, as :term:`Netplan` requires:

   .. code-block:: text

       sudo chmod 600 /etc/netplan/90-network-root.yaml

   ``critical: true`` stops systemd-networkd from removing the address while
   the system is running, which would cut the connection to the root
   file-system. Do not run ``netplan apply`` now: the new configuration takes
   effect on the next boot.

5. Allow the system to boot without its boot partition, by adding ``nofail``
   to the :file:`/boot/firmware` line in :file:`/etc/fstab`:

   .. code-block:: text

       LABEL=system-boot   /boot/firmware  vfat    defaults,nofail 0   1

6. Rebuild the initramfs, and install it as the one the boot firmware loads:

   .. code-block:: text

       sudo dracut --force /tmp/initrd.img
       sudo cp /tmp/initrd.img /boot/firmware/current/initrd.img


Configure the boot EEPROM
-------------------------

While the Pi is still booted from the microSD card, add network boot to the
boot order in the :ref:`EEPROM configuration
<edit-the-raspberry-pi-boot-configuration>`:

.. code-block:: text

    sudo rpi-eeprom-config --edit

Set the following properties:

.. code-block:: ini

    BOOT_ORDER=0xf21
    TFTP_IP=10.0.0.1
    TFTP_FILE_TIMEOUT=300000

`BOOT_ORDER`_ is read from right to left: try the microSD card (``1``), then
the network (``2``), then start again (``f``). The microSD card stays first, so
the Pi still boots from a card if one is inserted. ``TFTP_IP`` is the address
of your TFTP server. The default ``TFTP_FILE_TIMEOUT`` is too short for an
initramfs of this size on some networks; the value above allows five minutes
per file.

Shut the Pi down and remove the microSD card:

.. code-block:: text

    sudo poweroff


Set up the server
-----------------

Do the following on the server, with the microSD card from the previous steps
inserted in a card reader. Check the device name of the card with
:manpage:`lsblk(8)`; this guide uses :file:`/dev/sdX`.

.. warning::

    The :manpage:`dd(1)` command below reads from the card. Double check the
    device name: writing to the wrong device destroys its data.

1. Install the servers:

   .. code-block:: text

       sudo apt install dnsmasq nbd-server

2. Copy the root file-system, the second partition of the card, into an image
   file. Never let two systems use the same root file-system at the same
   time:

   .. code-block:: text

       sudo mkdir -p /srv/nbd
       sudo dd if=/dev/sdX2 of=/srv/nbd/pi-root.img bs=4M status=progress

3. Copy the contents of the boot partition, the first partition of the card,
   to the TFTP directory:

   .. code-block:: text

       sudo mkdir -p /srv/tftp /mnt/pi-boot
       sudo mount -o ro /dev/sdX1 /mnt/pi-boot
       sudo cp -r /mnt/pi-boot/. /srv/tftp/
       sudo umount /mnt/pi-boot

4. Edit :file:`/srv/tftp/current/cmdline.txt`, which the Pi reads as its
   kernel command line, so that it contains a single line:

   .. code-block:: text

       console=serial0,115200 multipath=off dwc_otg.lpm_enable=0 root=nbd:10.0.0.1:pi-root:ext4 ip=10.0.0.145::10.0.0.1:255.255.255.0::eth0:off rootwait fixrtc

   The parameters relevant to network boot are:

   ``root=nbd:10.0.0.1:pi-root:ext4``
       Mount the root file-system from the NBD export ``pi-root`` on the server
       10.0.0.1, as an ext4 file-system

   ``ip=10.0.0.145::10.0.0.1:255.255.255.0::eth0:off``
       The Pi's address, gateway, netmask and interface. Use the same values
       as in the Netplan configuration above. The address must not be in the
       DHCP range below

5. Configure the NBD export in :file:`/etc/nbd-server/config`:

   .. code-block:: ini

       [generic]
           listenaddr = 10.0.0.1

       [pi-root]
           exportname = /srv/nbd/pi-root.img

6. Configure DHCP and TFTP in :file:`/etc/dnsmasq.d/pi-netboot.conf`,
   replacing ``eth0`` with the name of the server's interface on the Pi's
   network:

   .. code-block:: text

       interface=eth0
       bind-interfaces
       port=0
       dhcp-range=10.0.0.100,10.0.0.200,12h
       enable-tftp
       tftp-root=/srv/tftp

   ``port=0`` disables the DNS server, which is not needed here.

7. Give the server's interface its address, and restart both servers:

   .. code-block:: text

       sudo ip addr add 10.0.0.1/24 dev eth0
       sudo systemctl restart nbd-server dnsmasq

   Use :term:`Netplan` to make the address permanent.


Boot the Pi
-----------

Power on the Pi with no microSD card inserted. The first boot takes longer
than usual, as the boot EEPROM spends some time looking for a card before
falling back to the network.

Once the Pi has booted, log in and confirm that the root file-system comes from
an NBD device:

.. code-block:: text

    findmnt /

.. code-block:: text

    TARGET SOURCE    FSTYPE OPTIONS
    /      /dev/nbd0 ext4   rw,relatime


Kernel and initramfs updates
----------------------------

.. TODO(review): untested. Document how to deploy kernel updates over network
   boot once a procedure has been tested, or keep this warning.

.. warning::

    The boot EEPROM loads the kernel and initramfs from the TFTP directory on
    the server, and the boot partition is not mounted on the running Pi.
    Kernel and initramfs updates installed on the Pi therefore do not reach
    the TFTP directory, and do not take effect over network boot.


Troubleshooting
---------------

Without a microSD card, the only output from a failing boot is on the
:ref:`UART console <connect-to-a-uart-console>`.

``NETBOOT init failed`` from the boot EEPROM
    The EEPROM found no network link, or no DHCP response. Check the cable, and
    that :program:`dnsmasq` is running on the right interface.

``Read current/initrd.img failed``, or repeated TFTP timeouts
    Increase ``TFTP_FILE_TIMEOUT`` in the EEPROM configuration. If transfers
    are repeatedly corrupted after the Pi restarts by itself, power it off and
    on again instead.

``Don't know how to handle 'root=nbd:...'``
    The initramfs does not include NBD support. Check
    :file:`/etc/dracut.conf.d/90-nbd.conf` on the image, and rebuild the
    initramfs.

The boot waits for the root device, and the Ethernet interface never appears
    The image is missing the drivers the Pi 5 needs for its Ethernet interface
    in the initramfs. Check that :lp-pkg:`ubuntu-raspi-settings` is at least
    the version listed at the start of this guide, and rebuild the initramfs.

The system stops responding shortly after booting
    The connection to the root file-system was cut, usually because the
    network configuration changed after boot. Check the Netplan configuration
    from the preparation steps.


.. _BOOT_ORDER: https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#BOOT_ORDER
