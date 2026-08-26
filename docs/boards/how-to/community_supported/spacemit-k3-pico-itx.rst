.. _install-ubuntu-on-the-spacemit-k3-pico-itx:

Install Ubuntu on the SpacemiT K3 Pico-ITX
==========================================

Flashing initial firmware on the board
--------------------------------------

By default, your SpacemiT K3 board is likely to ship with a Bianbu installation,
and an outdated firmware. It is necessary to update the firmware to install
official Ubuntu images.

.. note::

    SpacemiT also provides all-in-one images with firmware and vendor Ubuntu.
    Those images are only supported by SpacemiT. If you wish to install one of those images, see:

    - `SpacemiT's Ubuntu Image repository <https://github.com/spacemit-com/K3-Ubuntu-Images>`_
    - `SpacemiT's User Guide <https://www.spacemit.com/community/document/info?lang=en&nodepath=hardware/eco/k3_pico/pico_user_guide.md>`_

Putting the board in "flash mode"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /images/spacemit-k3-pico-itx-flash.jpg
   :alt: SpacemiT TitanTools home page
   :width: 40%
   :align: center

Power off the board, then press and hold the "FDL Flashing button" (2).
While holding, connect an USB-C power cable to the first USB-C connector (17).
Release the "FDL Flashing button" (2). The board is now in flashing mode.

Connect an USB Type-C cable to your host computer and the connector (18) on the board.

Installing firmware using Ubuntu packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A simple script is available on `GitHub <https://github.com/canonical/spacemit-k3-flash-firmware>`_ to flash the necessary firmware on the board.
Using it should be simple:

.. code-block:: text

    curl https://raw.githubusercontent.com/canonical/spacemit-k3-flash-firmware/refs/heads/main/flash-k3-firmware.sh | bash

.. warning::
    The firmware flashing script is **experimental**. Please report any issue on the
    `GitHub repository <https://github.com/canonical/spacemit-k3-flash-firmware/issues>`_.
    The Ubuntu RISC-V team is trying hard to provide the best user experience on the SpacemiT K3 for official images,
    but unfortunately firmware updates are necessary.

The script will download firmware packages from Ubuntu repositories, extract the binary payloads,
and use `SpacemiT tools <https://github.com/spacemit-com/K3-Ubuntu-Images>`_ to flash the board.

Installing an official (experimental) Ubuntu image
--------------------------------------------------

.. warning::
    Right now, official Ubuntu images are **experimental**. We expect official support to come with
    Ubuntu 26.10 Stonking Stingray release.

SpacemiT's image has a vendor SpacemiT kernel that is not provided by Canonical or Ubuntu,
and carries patches that are not upstream. Some Canonical software might not work with this kernel,
and if you choose this image please report issues directly to SpacemiT. You might want
to install an official Ubuntu image on the board.

.. note::

    **Removing stale cloud-init partition**

    If you have previously installed a SpacemiT vendor Ubuntu image, you will need to follow this step.
    Otherwise, skip it.

    The SpacemiT image adds a cloud-init partition to the internal UFS storage.
    This partition interferes with the installer used for Ubuntu images, therefore it needs to be removed.
    Log in to the SpacemiT image (user and password ``ubuntu/ubuntu``) and remove the partition:

    .. code-block:: text

       $ sudo fdisk /dev/sda

       # Print the partition table to check that you are deleting the
       # correct, 64M cloud-init partition
       Command (m for help): p

       Disk /dev/sda: 119.27 GiB, 128068878336 bytes, 31266816 sectors
       ...

       Device     Start      End  Sectors   Size Type
       /dev/sda1   3072    28671    25600   100M Microsoft basic data
       /dev/sda2  28672    45055    16384    64M Microsoft basic data
       /dev/sda3  45056 31266782 31221727 119.1G Microsoft basic data

       Command (m for help): d
       Partition number (1-3, default 3): 2

       Partition 2 has been deleted.
       Command (m for help): w
       The partition table has been altered.
       Syncing disks.

Installing from a USB thumb drive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the updated EDK2 firmware, you should now be able to boot from a USB thumb drive.
You can download and burn a preview Ubuntu image for the board.

When selecting a desktop image, you will need to connect a keyboard, mouse and screen to the board.
For a server install, you can use the serial console (UART) or keyboard and screen as well.

Then, reboot the board, press F2 and select the USB thumb drive in "Boot Manager"
as a boot target.

.. image:: /images/spacemit-edk2-boot.png
   :alt: SpacemiT boot splash
   :width: 49 %

.. image:: /images/spacemit-edk2-boot-manager.png
   :alt: SpacemiT boot menu
   :width: 49 %

This should boot into the Ubuntu installer image. Below are examples when selecting Ubuntu Desktop.
For Desktop, it can take a while for the board to reach graphical interface,
please be patient (around 3-5 minutes).

.. image:: /images/spacemit-ubuntu-install.png
   :alt: Ubuntu Desktop installer image, Grub prompt
   :width: 49 %

.. image:: /images/spacemit-ubuntu-installer.png
   :alt: Ubuntu Desktop installer
   :width: 49 %

Afterwards, you can follow the installer to install on the on-board UFS storage
or an NVMe drive. The UFS should be ``sda - KINGSTON``.

.. image:: /images/spacemit-install-drive.png
   :alt: Select drive for the Ubuntu installer
   :align: center
   :width: 79 %

Follow through the installation and reboot into your new installation.

Updating EDK2 and board firmware
--------------------------------

For now the traditional way of updating firmware (fwupd) is not available for the K3 boards.

SpacemiT has packaged their firmware into traditional ``deb`` Ubuntu packages.
The Ubuntu RISC-V team has applied modifications suitable for official Ubuntu images to those packages,
available on the `ubuntu-risc-v-team/k3 ppa <https://launchpad.net/~ubuntu-risc-v-team/+archive/ubuntu/k3>`_.

.. code-block:: bash

   sudo add-apt-repository ppa:ubuntu-risc-v-team/k3
   sudo apt update
   # Install spacemit-firmware metapackage to keep all firmware updated
   sudo apt install spacemit-firmware
   # ...or install each firmware package manually
   sudo apt install u-boot-spl-spacemit spacemit-ec-firmware opensbi-spacemit esos-spacemit edk2-spacemit
