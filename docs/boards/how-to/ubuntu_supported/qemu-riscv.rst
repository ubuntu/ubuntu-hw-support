.. _install-ubuntu-on-qemu-risc-v:

Install Ubuntu on QEMU (RISC-V)
===============================

Prerequisites
-------------

To boot a RISC-V virtual machine you will need the following packages

* :lp-pkg:`opensbi` -- :term:`OpenSBI` implements the RISC-V
  Supervisor Binary Interface (:term:`SBI`).

* :lp-pkg:`qemu-system-riscv64 <qemu>` -- :term:`QEMU` is used to
  emulate a RISC-V machine.

and one of

* :lp-pkg:`qemu-efi-riscv64 <edk2>` -- EDK II is the reference implementation
  of the :term:`UEFI` :term:`API`.

* :lp-pkg:`u-boot-qemu <u-boot>` -- U-Boot is another firmware. It implements a
  subset of the UEFI API.

installed.

The packages can be installed with the following commands:

.. code-block:: text

    sudo apt update
    sudo apt install opensbi qemu-system-riscv64 qemu-efi-riscv64 u-boot-qemu


Using the pre-installed server image
------------------------------------

* Download one of the supported images:

  .. ubuntu-images::
      :releases: noble-
      :image-types: preinstalled-server
      :archs: riscv64
      :matches: (riscv64\.img)

  .. on jammy, use the +unmatched image for QEMU; later releases should use
     the unsuffixed images, hence the horrid regex above.

* Unpack the image:

  .. code-block:: text

      xz -dk ubuntu-*-preinstalled-server-riscv64.img.xz

* Optionally, if you want a larger disk, you can expand the disk (the
  file-system will be automatically resized too):

  .. code-block:: text

      qemu-img resize -f raw ubuntu-*-preinstalled-server-riscv64.img +5G


Running via U-Boot
~~~~~~~~~~~~~~~~~~

* Next use U-Boot to boot the virtual machine. A working example with all
  the options is:

  .. code-block:: text

      qemu-system-riscv64 \
        -cpu rva23s64 \
        -machine virt,acpi=off -m 4G -smp cpus=2 \
        -nographic \
        -kernel /usr/lib/u-boot/qemu-riscv64_smode/uboot.elf \
        -netdev user,id=net0 \
        -device virtio-net-device,netdev=net0 \
        -device virtio-rng-pci \
        -drive file=ubuntu-*-preinstalled-server-riscv64.img,format=raw,if=virtio

  The important options to use are:

  \-cpu
      controls the emulated CPU

      .. note::

          Ubuntu releases from 25.10 onward require the RVA23S64 ISA profile,
          which is only available on QEMU 10.1 or later.
          If your QEMU version is preceding 10.1 (e.g. on Ubuntu 25.04 and
          below), you can only run Ubuntu 25.04 and below. In that case, remove
          ``-cpu rva23s64``.

  \-machine
      selects the platform emulated by QEMU.

  \-m
      specifies the memory size

  \-smp
      specifies the number of CPUs

  \-bios
      This option can be used to select the first stage firmware by QEMU. Since
      QEMU 7.0 this defaults to OpenSBI. On earlier version of QEMU to have to
      explicitly specify
      ``-bios /usr/lib/riscv64-linux-gnu/opensbi/generic/fw_dynamic.bin``.

  \-kernel
      Here the option is used load U-Boot as second stage boot-loader.

* Watch the serial console output and wait for cloud-init to complete. It will
  show a line with the text 'Cloud-init finished' like:

  .. code-block:: text

      [   68.346028] cloud-init[703]: Cloud-init v. 22.2-0ubuntu1~20.04.3 finished at Thu, 22 Sep 2022 11:35:28 +0000. Datasource DataSourceNoCloud [seed=/var/lib/cloud/seed/nocloud-net][dsmode=net].  Up 68.26 seconds

* Login with the user *ubuntu* and the default password *ubuntu*; you will be
  asked to choose a new password.


Running via EDK II
~~~~~~~~~~~~~~~~~~

EDK II may be used instead of U-Boot to run RISC-V virtual machines.

.. code-block:: text

    sudo apt update
    sudo apt install qemu-efi-riscv64
    cp /usr/share/qemu-efi-riscv64/RISCV_VIRT_VARS.fd .
    qemu-system-riscv64 \
      -cpu rva23s64 \
      -machine virt,acpi=off -m 4G -smp cpus=2 \
      -nographic \
      -drive if=pflash,format=raw,unit=0,file=/usr/share/qemu-efi-riscv64/RISCV_VIRT_CODE.fd,readonly=on \
      -drive if=pflash,format=raw,unit=1,file=RISCV_VIRT_VARS.fd,readonly=off \
      -netdev user,id=net0 \
      -device virtio-net-device,netdev=net0 \
      -device virtio-rng-pci \
      -drive file=ubuntu-*-preinstalled-server-riscv64.img,format=raw,if=virtio

.. note::

    RISC-V virtual machines can be boot via device-tree (``acpi=off``) or via
    ACPI (``acpi=on``). If ACPI is supported, depends on the kernel version.


Cloud-init seed
~~~~~~~~~~~~~~~

Sample files for a cloud-init seed are present on the FAT partition labeled
"CIDATA". See :ref:`configure-your-board-for-headless-use` for more information.


Using the live server image
---------------------------

Installing live server image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Download one of the supported images:

   .. ubuntu-images::
       :releases: noble-
       :image-types: live-server
       :archs: riscv64

#. Create the disk image onto which you will install Ubuntu; 16 GiB should be
   enough:

   .. code-block:: text

       truncate -s 16G disk

#. Start the installer with (using U-Boot as example):

   .. code-block:: text

       qemu-system-riscv64 \
         -cpu rva23s64 \
         -machine virt,acpi=off -m 4G -smp cpus=2 \
         -nographic \
         -kernel /usr/lib/u-boot/qemu-riscv64_smode/uboot.elf \
         -netdev user,id=net0 \
         -device virtio-net-device,netdev=net0 \
         -device virtio-rng-pci \
         -drive file=disk,format=raw,if=virtio \
         -drive file=ubuntu-*-live-server-riscv64.iso,format=raw,if=virtio

#. Follow the installation steps in
   `Ubuntu Server installation tutorial
   <https://ubuntu.com/tutorials/install-ubuntu-server>`_.

When rebooting we have to remove the installer image. Otherwise the installer
may restart.

.. restarting or not depends on the order of drives.

U-Boot gives you a 2-second time window to press the Enter key to reach the
U-Boot console. In U-Boot's console you can use the ``poweroff`` command to stop
QEMU. Another option to exit QEMU is pressing keys ``CTRL-a`` followed by key
``x``. You can get quick help by pressing keys ``CTRL-a`` followed by key ``h``.


Running Ubuntu
~~~~~~~~~~~~~~

To run your installed Ubuntu image use:

.. code-block:: text

    qemu-system-riscv64 \
      -cpu rva23s64 \
      -machine virt,acpi=off -m 4G -smp cpus=2 \
      -nographic \
      -kernel /usr/lib/u-boot/qemu-riscv64_smode/uboot.elf \
      -netdev user,id=net0 \
      -device virtio-net-device,netdev=net0 \
      -device virtio-rng-pci \
      -drive file=disk,format=raw,if=virtio


Limitations
-----------

* The number of virtual CPUs was limited to 8 before QEMU 7.0. The limit was
  raised in QEMU 7.0 to 512. OpenSBI is limited to 128 CPUs. U-Boot supports
  32 CPUs.
