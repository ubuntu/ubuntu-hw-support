.. SPDX-License-Identifier: CC-BY-SA-4.0

.. _firmware-requirements:

Firmware requirements
=====================

UEFI support
------------

Ubuntu boots via UEFI. The requirements specified in the
`Embedded Base Boot Requirements (EBBR) specification
<https://github.com/arm-software/ebbr>`_
must be fulfilled.

Either a device-tree or ACPI tables must be provided.

U-Boot
''''''

In U-Boot the following configuration settings are needed:

* CONFIG_EFI_LOADER=y
* CONFIG_CMD_EFICONFIG=y
* CONFIG_CMD_BOOTEFI_BOOTMGR=y
* CONFIG_BOOTMETH_EFI_BOOTMGR=y (or deprecated CONFIG_DISTRO_DEFAULTS=y)

* CONFIG_CMD_NVEDIT_EFI=y
* CONFIG_EFI_CMD_EFIDEBUG=y
* CONFIG_HEXDUMP=y

Device-tree
-----------

Ideally the device-tree provided by the firmware is a full description of the
device and can directly be used to boot the Linux kernel. As device-trees in
Linux change of the years, differences between the firmware device-tree and the
Linux device-tree arise.

To provide full device functionality, Ubuntu tries to load a kernel device-tree
matching both the device and the kernel version. This requires that the
following properties provided in the device's device-tree exactly match the
corresponding kernel definitions:

* /compatible - This property is used by systemd-boot or stubble for matching.
* /model      - This property is used by flash-kernel for matching.

Kernel device-trees often lack memory reservations (e.g. for OpenSBI) and
other required information, like MAC addresses of network interfaces. Therefore,
a firmware using device-trees should implement the
`EFI_DT_FIXUP_PROTOCOL <https://github.com/U-Boot-EFI/EFI_DT_FIXUP_PROTOCOL>`_.
As of 26.04, Ubuntu is still using version v0.05 of the protocol with GUID
e617d64c-fe08-46da-f4dc-bbd5870c7300. It is advisable to also implement the
newer version with GUID 60ed6ba9-dfef-4799-ac7b-75e0f833456c.

SMBIOS
------

An SMBIOS table should be present. It needs to provide accurate data to manage
the infrastructure. This includes:

* Platform Firmware Information (Type 0)

  * Vendor
  * Firmware version
  * Firmware release date

* System Information (Type 1)

  * Manufacturer
  * Product name
  * Version
  * Serial number

* Processor Information (Type 4)

  * Processor version

EDK II
''''''

In EDK II the following driver is needed:

* MdeModulePkg/Universal/SmbiosDxe/SmbiosDxe.inf

U-Boot
''''''

The following configuration setting is needed:

* CONFIG_GENERATE_SMBIOS_TABLE=y

Network booting
---------------

During network booting the GRUB binary is discovered via PXE booting.
The GRUB configuration file (grub.cfg) will contain HTTP(s) URLs for the
Linux kernel and the initial RAM disk.

The following UEFI protocol need to be enabled:

* HTTP Protocol
* HTTP Utilities Protocol
* IPv4 Configuration II Protocol
* Simple Network Protocol

EDK II
''''''

In EDK II the following drivers should be enabled:

+--------------------------+--------------------------------------------------+
| Configuration Flag       | Driver                                           |
+==========================+==================================================+
| NETWORK_HTTP_BOOT_ENABLE | NetworkPkg/DnsDxe/DnsDxe.inf                     |
|                          | NetworkPkg/HttpDxe/HttpDxe.inf                   |
|                          | NetworkPkg/HttpUtilitiesDxe/HttpUtilitiesDxe.inf |
+--------------------------+--------------------------------------------------+
| NETWORK_IP4_ENABLE       | NetworkPkg/ArpDxe/ArpDxe.inf                     |
|                          | NetworkPkg/Dhcp4Dxe/Dhcp4Dxe.inf                 |
|                          | NetworkPkg/Ip4Dxe/Ip4Dxe.inf                     |
|                          | NetworkPkg/Udp4Dxe/Udp4Dxe.inf                   |
|                          | NetworkPkg/Mtftp4Dxe/Mtftp4Dxe.inf               |
+--------------------------+--------------------------------------------------+
| NETWORK_IP6_ENABLE       | NetworkPkg/Dhcp6Dxe/Dhcp6Dxe.inf                 |
|                          | NetworkPkg/Ip6Dxe/Ip6Dxe.inf                     |
|                          | NetworkPkg/Udp6Dxe/Udp6Dxe.inf                   |
|                          | NetworkPkg/Mtftp6Dxe/Mtftp6Dxe.inf               |
+--------------------------+--------------------------------------------------+
| NETWORK_TLS_ENABLE       | CryptoPkg/Library/OpensslLib/OpensslLib.inf      |
|                          | NetworkPkg/TlsDxe/TlsDxe.inf                     |
|                          | NetworkPkg/TlsAuthConfigDxe/TlsAuthConfigDxe.inf |
+--------------------------+--------------------------------------------------+
| NETWORK_PXE_BOOT_ENABLE  | NetworkPkg/UefiPxeBcDxe/UefiPxeBcDxe.inf         |
+--------------------------+--------------------------------------------------+
| NETWORK_SNP_ENABLE       | NetworkPkg/SnpDxe/SnpDxe.inf                     |
+--------------------------+--------------------------------------------------+

U-Boot
''''''

In U-Boot the following configuration settings are needed:

* CONFIG_NET_LWIP=y
* CONFIG_DNS=y
* CONFIG_WGET=y
* CONFIG_EFI_IP4_CONFIG2_PROTOCOL=y
* CONFIG_EFI_HTTP_PROTOCOL=y

For testing these additional settings are recommended:

* CONFIG_CMD_DNS
* CONFIG_CMD_WGET
