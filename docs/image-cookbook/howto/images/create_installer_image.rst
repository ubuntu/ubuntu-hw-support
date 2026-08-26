.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _create-installer-image:

Create installer image
=======================

Install ``livecd-rootfs``
-------------------------

As of 2026 :lp-pkg:`livecd-rootfs` is the tool used by Canonical to create
both preinstalled images as well as installer images.

You can install it with

.. prompt:: text $ auto

    $ sudo apt update
    $ sudo apt install livecd-rootfs

The package provides three scripts in /usr/share/livecd-rootfs/live-build/auto/:

clean
    Remove build artifacts

config
    Configure build

build
    Execute the build

Build an Ubuntu image
---------------------

Here is an example of building a riscv64 ubuntu-server installer image, **on a native riscv64 host**:

.. prompt:: text $ auto

    sudo /usr/share/livecd-rootfs/live-build/auto/clean

    sudo \
    ARCH=riscv64 \
    PROJECT=ubuntu-server \
    SUBPROJECT=live \
    SUITE=resolute \
    /usr/share/livecd-rootfs/live-build/auto/config

    sudo \
    ARCH=riscv64 \
    PROJECT=ubuntu-server \
    SUBPROJECT=live \
    SUITE=resolute \
    /usr/share/livecd-rootfs/live-build/auto/build

The output of this build is file 'livecd.ubuntu-server.iso*.

.. note::

    **Cross-building** a ``riscv64`` image from an ``amd64`` host is currently **not** supported.

Customizing the build
---------------------

Which image is built is controlled by environment variables.

+---------------+----------+-----------------------------------------------------------------------------+
| Variable      | Required | Usage                                                                       |
+===============+==========+=============================================================================+
| ARCH          | required | Ubuntu architecture (e.g. risc       v64)                                   |
+---------------+----------+-----------------------------------------------------------------------------+
| EXTRA_PPAS    | optional | A space separated string, e.g. ``"user1/ppa1 user1/ppa2 user2/ppa3"``.      |
|               |          | The PPA string may contain a pin priority, e.g. ``"user1/ppa1:300"``.       |
+---------------+----------+-----------------------------------------------------------------------------+
| EXTRA_SNAPS   | optional |                                                                             |
+---------------+----------+-----------------------------------------------------------------------------+
| IMAGEFORMAT   | optional | *ext2*, *ext3*, *ext4*, *plain*, *ubuntu-image*, *none*                     |
+---------------+----------+-----------------------------------------------------------------------------+
| IMAGE_TARGETS | optional | *disk-image*, *qcow2*, *squashfs*, *tarball*, *vmdk*                        |
+---------------+----------+-----------------------------------------------------------------------------+
| MIRROR        | optional | Mirror used for installing packages. If not set, is selected automatically. |
+---------------+----------+-----------------------------------------------------------------------------+
| PROJECT       | required | *ubuntu-cpc*, *ubuntu-server*, *ubuntustudio*, *ubuntu*, *kubuntu*, ...     |
+---------------+----------+-----------------------------------------------------------------------------+
| PROPOSED      | optional | ``PROPOSED=1`` selects the proposed pocket for packages                     |
+---------------+----------+-----------------------------------------------------------------------------+
| SEEDMIRROR    | internal | Defaults to https://people.canonical.com/~ubuntu-archive/seeds/             |
+---------------+----------+-----------------------------------------------------------------------------+
| SUBARCH       | optional | Used only for ``$IMAGEFORMAT="ubuntu-image"``                               |
+---------------+----------+-----------------------------------------------------------------------------+
| SUBPROJECT    | optional | E.g. *live* (for ubuntu-server), *minimized* (for minimized images)         |
+---------------+----------+-----------------------------------------------------------------------------+
| SUITE         | required | Ubuntu release, e.g. *resolute* for Ubuntu 26.04                            |
+---------------+----------+-----------------------------------------------------------------------------+

Here are some useful property combinations:

+----------------------------+---------------+------------+-------------+
| Image                      | PROJECT       | SUBPROJECT | IMAGEFORMAT |
+============================+===============+============+=============+
| RISC-V preinstalled server | ubuntu-cpc    | generic    | ext4        |
+----------------------------+---------------+------------+-------------+
| Ubuntu server installer    | ubuntu-server | live       |             |
+----------------------------+---------------+------------+-------------+
| Ubuntu desktop             | ubuntu        | live       |             |
+----------------------------+---------------+------------+-------------+
| Xubuntu desktop            | xubuntu       | live       |             |
+----------------------------+---------------+------------+-------------+
| Xubuntu minimal desktop    | xubuntu       | minimal    |             |
+----------------------------+---------------+------------+-------------+

For a full overview consult the livecd-rootfs source code available at
https://git.launchpad.net/ubuntu/+source/livecd-rootfs.

There are significant changes between the livecd-rootfs packages of different
Ubuntu releases.
