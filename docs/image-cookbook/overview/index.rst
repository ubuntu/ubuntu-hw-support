.. SPDX-License-Identifier: CC-BY-SA-4.0
owner Giorgi Meskhidze 
.. _image-overview:

Overview
========

The Image Cookbook is meant to help users to spin Ubuntu based images
for hardware that is not yet supported by the Ubuntu distribution.

It will guide you through these steps of your project:

* Collect requirements
* Setup Launchpad
* Build packages
* Build the image
* Test the image

.. note::

   **This documentation is still in draft status.**

Collect requirements
--------------------

For getting started you will have to create an overview of which aspects
of current Ubuntu does not fulfill your needs. Typical items are:

* vendor Linux kernel
* vendor Xorg and Mesa packages
* vendor U-Boot required on the image
* additional packages
* configuration files

Next identify the licenses and other legal requirements like non-disclosure
agreements of the extra required packages.

If source code must not be disclosed to the public,
private personal package archives (PPAs) on Launchpad can be used.

Here is a typical workflow:

.. image:: /images/workflow.png
   :alt: Typical workflow

The produced image will take all packages that are not device specific from the
Ubuntu archive. This ensures that devices will receive all package updates.

All device specific packages will be taken from the public PPA. It will be the
device PPA owner's obligation to ensure security updates.

Setup Launchpad
---------------

Please, follow in sequence these chapters:

.. vale off

* :doc:`../howto/launchpad/create_user`
* :doc:`../howto/launchpad/create_team`
* :doc:`../howto/launchpad/create_ppa`

.. vale on

Build packages
--------------

This process is described in:

.. vale off

* :doc:`../howto/packaging/package`
* :doc:`../howto/launchpad/upload_ppa`
* :doc:`../howto/launchpad/consume_ppa`
* :doc:`../howto/packaging/repackage`

.. vale on

Build the image
---------------

The image creation process is described in:

* :doc:`../tutorial/create_image`
* :doc:`../howto/images/create_image`

Test the image
--------------

A checklist for images is available at:

* :doc:`../reference/image_checklist`
