.. _ubuntu-hw-support:

Ubuntu hardware support documentation
======================================

.. toctree::
   :hidden:
   :maxdepth: 2

   boards/index
   image-cookbook/index
   contributing

**Ubuntu hardware support documentation covers installing Ubuntu on non-PC
hardware — including Raspberry Pi and RISC-V single-board computers — and
building custom Ubuntu-based images for hardware not yet supported by Ubuntu.**

**The documentation spans two guides.** The boards documentation covers
installing Ubuntu on specific Ubuntu-supported and community-supported
hardware, configuring boards for use cases such as headless operation and
camera access, and understanding the image types and boot mechanisms in use.
The Image Cookbook covers building, packaging, and distributing custom Ubuntu
images using ``ubuntu-image``, Launchpad PPAs, and custom kernel packages.

**These guides address the need to run Ubuntu on hardware where a standard
installation is unavailable or insufficient.** The boards documentation
provides tested installation paths for supported boards and explains common
boot and hardware configuration scenarios. The Image Cookbook provides the
steps to create distributable Ubuntu images for new hardware platforms.

**This documentation is for hardware engineers, system integrators, and
developers working with non-PC hardware.** It assumes familiarity with Linux
and the command line, but does not require prior experience with Ubuntu
image-building tools or Launchpad.


In this documentation
---------------------

This section maps every major page in the docs set by subject, giving direct
access to content across Diátaxis types without depending on sidebar
navigation.

For a guided introduction, start with the
:ref:`installation tutorials <boards-tutorials>`.


Installing Ubuntu on boards
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each row links the per-board installation pages for a specific platform.

* **Raspberry Pi**: :ref:`Install Ubuntu on the Raspberry Pi <install-ubuntu-on-the-raspberry-pi>` • :ref:`Install directly <install-ubuntu-on-raspberry-pi-directly>` • :ref:`Install via PC <install-ubuntu-on-raspberry-pi-via-pc>`
* **SpacemiT K3**: :ref:`Install Ubuntu on SpacemiT K3 boards <install-ubuntu-on-spacemit-k3>`
* **QEMU**: :ref:`Install Ubuntu on QEMU (ARM64) <install-ubuntu-on-qemu-arm64>` • :ref:`Install Ubuntu on QEMU (RISC-V) <install-ubuntu-on-qemu-risc-v>`

Boards supported by older Ubuntu LTS releases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Allwinner Nezha D1**: :ref:`Install Ubuntu on the Allwinner Nezha D1 <install-ubuntu-on-the-allwinner-nezha-d1>`
* **DeepComputing FML13V01**: :ref:`Install Ubuntu on the DeepComputing FML13V01 <install-ubuntu-on-the-deepcomputing-fml13v01>`
* **Microchip PIC64GX1000**: :ref:`Install Ubuntu on the Microchip PIC64GX1000 Curiosity Kit <install-ubuntu-on-the-microchip-pic64gx1000-curiosity-kit>`
* **Microchip PolarFire SoC Icicle Kit**: :ref:`Install Ubuntu on the Microchip PolarFire SoC Icicle Kit <install-ubuntu-on-the-microchip-polarfire-soc-icicle-kit>`
* **Milk-V Mars**: :ref:`Install Ubuntu on the Milk-V Mars <install-ubuntu-on-the-milk-v-mars>` • :ref:`Install Ubuntu on the Milk-V Mars CM and CM Lite <install-ubuntu-on-the-milk-v-mars-cm-and-cm-lite>`
* **Pine64 Star64**: :ref:`Install Ubuntu on the Pine64 Star64 <install-ubuntu-on-the-pine64-star64>`
* **SiFive HiFive Unmatched**: :ref:`Install Ubuntu on the SiFive HiFive Unmatched <install-ubuntu-on-the-sifive-hifive-unmatched>`
* **Sipeed LicheeRV Dock**: :ref:`Install Ubuntu on the Sipeed LicheeRV Dock <install-ubuntu-on-the-sipeed-licheerv-dock>`
* **StarFive VisionFive**: :ref:`Install Ubuntu on the StarFive VisionFive <install-ubuntu-on-the-starfive-visionfive>` • :ref:`VisionFive 2 <install-ubuntu-on-the-starfive-visionfive-2>` • :ref:`VisionFive 2 Lite <install-ubuntu-on-the-starfive-visionfive-2-lite>`
* **Radxa ROCK Pi 4A** (community-supported): :ref:`Install Ubuntu on the Radxa ROCK Pi 4A <install-ubuntu-on-the-raxda-rock-4a>`


Hardware configuration
~~~~~~~~~~~~~~~~~~~~~~

These guides cover setup tasks and troubleshooting methods that apply across
one or more board families.

* **Flashing images**: :ref:`Flash images to a microSD card <flash-images-to-a-microsd-card>`
* **Headless setup**: :ref:`Configure your board for headless use <configure-your-board-for-headless-use>`
* **Serial console**: :ref:`Connect to a UART console <connect-to-a-uart-console>`
* **Raspberry Pi camera**: :ref:`Using the camera on Raspberry Pi <using-the-camera-on-raspberry-pi>`
* **Raspberry Pi boot configuration**: :ref:`Edit the Raspberry Pi boot configuration <edit-the-raspberry-pi-boot-configuration>`


Building custom images
~~~~~~~~~~~~~~~~~~~~~~

This section covers the complete Image Cookbook workflow: from setting up
Launchpad infrastructure to creating distributable Ubuntu images for new
hardware.

* **Getting started**: :ref:`Image Cookbook overview <image-overview>` • :ref:`Your first Ubuntu image <your-first-ubuntu-image>`
* **Image creation**: :ref:`Create image with ubuntu-image <create-customized-image-with-ubuntu-image>`
  • :ref:`Create installer image <create-installer-image>`
  • :ref:`Customize installer images <customize-installer-images>`
* **Kernel packages**: :ref:`Your first kernel package <your-first-kernel-package>` • :ref:`Package a custom kernel <package-kernel>`
* **Packaging**: :ref:`Package binaries as .deb <package-binaries>` • :ref:`Repackage binaries <repackage-binaries>`

.. vale off

* **Launchpad**: :ref:`Create Launchpad user <create-launchpad-user>` • :ref:`Create team <create-launchpad-team>` • :ref:`Create PPA <create-ppa>` • :ref:`Create Git repository <create_git>` • :ref:`Upload to a PPA <upload-to-ppa>` • :ref:`Consume a PPA <consume-ppa>`

.. vale on


Reference and background
~~~~~~~~~~~~~~~~~~~~~~~~

These pages provide specifications, test cases, and conceptual explanations
that support the tasks described in the tutorial and how-to sections.

* **Glossary**: :ref:`Glossary <glossary>`
* **Image types**: :ref:`Server installer or pre-installed images? <server-installer-or-pre-installed-images>`
* **Raspberry Pi A/B boot**: :ref:`A/B boot on Ubuntu for Raspberry Pi <a-b-boot-on-ubuntu-for-raspberry-pi>`
* **Boot flow**: :ref:`Boot flow <boot-flow>`
* **Firmware requirements**: :ref:`Firmware requirements <firmware-requirements>`
* **Gadget definition**: :ref:`Gadget.yaml fields <gadget-yaml-fields>`
* **Image definition**: :ref:`Image-definition.yaml fields <image-definition-yaml>`
* **Image checklist**: :ref:`Checklist for Ubuntu images <image-checklist>`
* **Kernel test cases**: :ref:`Kernel test cases <kernel-test-cases>`
* **Tools**: :ref:`Tools <image-tools>`


How this documentation is organized
-------------------------------------

This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`_.

* :ref:`Tutorials <boards-tutorials>` • :ref:`Image Cookbook tutorials <image-tutorials>` — installing Ubuntu on Raspberry Pi, and creating a custom Ubuntu image and kernel package.
* :ref:`How-to guides <boards-how-to-guides>` • :ref:`Image Cookbook how-to guides <image-how-to-guides>` — per-board installation for Ubuntu-supported and community-supported hardware, hardware configuration, image creation with ``ubuntu-image``, packaging, and Launchpad setup.
* :ref:`Reference <image-reference>` — specifications for firmware requirements, ``gadget.yaml``, ``image-definition.yaml``, and image-building tools.
* :ref:`Explanation <boards-explanations>` • :ref:`Image Cookbook explanation <image-explanation>` — background on Ubuntu image types, the Raspberry Pi A/B boot mechanism, and the RISC-V boot flow.


Project and community
---------------------

Ubuntu hardware support documentation is part of the Ubuntu documentation ecosystem, with both
guides maintained as a community effort under the Canonical organization
on GitHub.


Get involved
~~~~~~~~~~~~

Use the issue tracker to report problems, browse the source in the GitHub
repository, or consult the contribution guidelines before opening a pull
request.

* `Issue tracker <https://github.com/canonical/ubuntu-hw-support/issues>`_
* `GitHub repository <https://github.com/canonical/ubuntu-hw-support>`_
* :ref:`Contribution guidelines <how-to-contribute>`


Governance and policies
~~~~~~~~~~~~~~~~~~~~~~~

* `Ubuntu Code of Conduct <https://ubuntu.com/community/ethos/code-of-conduct>`_
