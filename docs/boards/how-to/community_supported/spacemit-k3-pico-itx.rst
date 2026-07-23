.. _install-ubuntu-on-the-spacemit-k3-pico-itx:

Install Ubuntu on the SpacemiT K3 Pico-ITX
==========================================

Flashing initial firmware and image on the board
------------------------------------------------

SpacemiT provides all-in-one images with firmware (EDK2, as well as firmware
for the power controller) and vendor Ubuntu. It is necessary to flash this
on the board first to have the right firmware to be able to run mainline
Ubuntu.

.. note::

    Flashing instructions are directly available in 
    `SpacemiT's User Guide <https://www.spacemit.com/community/document/info?lang=en&nodepath=hardware/eco/k3_pico/pico_user_guide.md>`_
    for the board. See section "3.1 Method 1: Flashing via Type-C Data Cable".

Putting the board in "flash mode"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /images/spacemit-k3-pico-itx-flash.jpg
   :target: ../../_images/spacemit-k3-pico-itx-flash.jpg
   :alt: SpacemiT TitanTools home page
   :width: 40%
   :align: center

Power off the board, then press and hold the "FDL Flashing button" (2).
While holding, connect an USB-C power cable to the first USB-C connector (17).
Release the "FDL Flashing button" (2). The board is now in flashing mode.

Connect an USB Type-C cable to your host computer and the connector (18) on the board.

Downloading an image to flash
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Vendor images are available on `SpacemiT GitHub repository <https://github.com/spacemit-com/K3-Ubuntu-Images>`_.
Download the latest release, available in the "Releases" section on the right of the page.
Depending on which software you want to use to flash to the board, 
you will need to choose an image format (``.tar.gz`` for TitanTools or ``.img.zst`` for ``fastboot``, see below).

Flashing the image using software on a host machine
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two different software tools available to flash the board:

* `SpacemiT "TitanTools" utility <https://www.spacemit.com/community/document/info?lang=en&nodepath=tools/user_guide/flasher_user_guide.md>`_
* SpacemiT's script for ``fastboot`` (a bit more involved)

Using TitanTools
~~~~~~~~~~~~~~~~

TitanTools is distributed by SpacemiT as an AppImage. On the `website <https://www.spacemit.com/community/document/info?lang=en&nodepath=tools/user_guide/flasher_user_guide.md>`_
you can download it, run ``chmod +x ./titantools_for_linux-X.X.X-Rc.AppImage`` and run it directly with ``./titantools_for_linux-X.X.X-Rc.AppImage``.

This will open the graphical interface of TitanTools.

.. note::
   The TitanTools utility will require elevated privileges and is not verified by Canonical.
   Please proceed at your own risk.

.. image:: /images/spacemit-titantools.png
   :target: ../../_images/spacemit-titantools.png
   :align: center
   :width: 70%
   :alt: SpacemiT TitanTools home page

By default, if running TitanTools on Ubuntu, you need to change the working directory 
(in Settings) to something like "/tmp/titantools" (the default one will not work).

Then, you can select "Dev Tools", "USB Download". Scan for devices and your board should appear.
Select the image you downloaded earlier, and click "Start Flashing".

Using fastboot
~~~~~~~~~~~~~~

.. code-block:: bash

    # Install dependencies
    sudo apt update
    sudo apt install git ubuntu-dev-tools fastboot
    # Clone SpacemiT repository
    git clone https://github.com/spacemit-com/K3-Ubuntu-Images.git gadget
    # Run SpacemiT script to flash the image you previously downloaded
    make IMG=/path/to/ubuntu-26.04-preinstalled-desktop-riscv64.img.zst all

If you want a fine-grained way to flash the image, see instructions in the 
`README.md <https://github.com/spacemit-com/K3-Ubuntu-Images#flash-via-fastboot>`_.

Installing an official or experimental Ubuntu image
---------------------------------------------------

SpacemiT's image has a vendor SpacemiT kernel that is not provided by Canonical or Ubuntu,
and carries patches that are not upstream. Some Canonical software might not work with this kernel, 
and if you choose this image please report issues directly to SpacemiT. You might want 
to install an official Ubuntu image on the board.

Removing stale cloud-init partition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
   :target: ../../_images/spacemit-edk2-boot.png
   :alt: SpacemiT boot splash
   :width: 49 %

.. image:: /images/spacemit-edk2-boot-manager.png
   :target: ../../_images/spacemit-edk2-boot-manager.png
   :alt: SpacemiT boot menu
   :width: 49 %

This should boot into the Ubuntu installer image. Below are examples when selecting Ubuntu Desktop.
For Desktop, it can take a while for the board to reach graphical interface, 
please be patient (around 3-5 minutes).

.. image:: /images/spacemit-ubuntu-install.png
   :target: ../../_images/spacemit-ubuntu-install.png
   :alt: Ubuntu Desktop installer image, Grub prompt
   :width: 49 %

.. image:: /images/spacemit-ubuntu-installer.png
   :target: ../../_images/spacemit-ubuntu-installer.png
   :alt: Ubuntu Desktop installer
   :width: 49 %

Afterwards, you can follow the installer to install on the on-board UFS storage 
or an NVMe drive. The UFS should be ``sda - KINGSTON``.

.. image:: /images/spacemit-install-drive.png
   :target: ../../_images/spacemit-install-drive.png
   :alt: Select drive for the Ubuntu installer
   :align: center
   :width: 79 %

Follow through the installation and reboot into your new installation.

Updating EDK2 and board firmware
--------------------------------

For now the traditional way of updating firmware (fwupd) is not available for the K3 boards.
SpacemiT has packaged their firmware into traditional ``deb`` Ubuntu packages.
Those package will be available on the `ubuntu-risc-v-team/k3 ppa <https://launchpad.net/~ubuntu-risc-v-team/+archive/ubuntu/k3>`_.

.. note::
   Firmware packages are not available yet but should be available soon.

.. code-block:: bash

   sudo add-apt-repository ppa:ubuntu-risc-v-team/k3
   sudo apt update
   # Install spacemit-firmware metapackage to keep all firmware updated 
   sudo apt install spacemit-firmware
   # ...or install each firmware package manually
   sudo apt install u-boot-spl-spacemit spacemit-ec-firmware opensbi-spacemit esos-spacemit edk2-spacemit

