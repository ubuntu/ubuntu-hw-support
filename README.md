[![Documentation Status](https://readthedocs.com/projects/canonical-ubuntu-hardware-supportubuntu/badge/?version=latest)](https://canonical-ubuntu-hardware-supportubuntu.readthedocs-hosted.com/?badge=latest)


# Ubuntu hardware support documentation

Documentation for installing Ubuntu on a variety of (typically non-PC) hardware, including Raspberry Pi and RISC-V boards, as well for spinning Ubuntu-based images for hardware that is not yet supported by the Ubuntu distribution.

Currently, the repository hosts two documentation sets that used to be published separately. Eventually, the plan is for all the content to be consolidated into one coherent collection of docs.


## Project homepage

The project Git repository is located at [github.com/ubuntu/ubuntu-hw-support](https://github.com/canonical/ubuntu-hw-support/).

The generated documentation is hosted at [ubuntu.com/hardware/docs](https://ubuntu.com/hardware/docs/).

The continuous integration results are available at [ubuntu-hw-support/actions](https://github.com/ubuntu/ubuntu-hw-support/actions/).


## RISC-V image cookbook

The RISC-V image cookbook is meant to help users to spin Ubuntu based images for hardware that is not yet supported by the Ubuntu distribution.

It guides you through these steps of your project:

* Collect requirements
* Set up Launchpad
* Build packages
* Build the image
* Test the image


## Ubuntu boards docs

Formerly hosted on the Ubuntu wiki, this is the guide to installation and usage of Ubuntu on a variety of single board computers (SBCs).


## Building

To build and check the docs:

    cd docs/
    make html
    make spellcheck
    make linkcheck
    make vale

To serve the HTML pages locally on `http://127.0.0.1:8080`:

    make serve


## How to contribute

Contributions in the form of pull requests are welcome. The documentation is written in reStructuredText under the popular Sphinx documentation system. Note that all contributors need to have signed the [Canonical CLA](https://canonical.com/legal/contributors), and all commits need to be signed with your GPG key.

See [`docs/contributing.rst`](https://github.com/canonical/ubuntu-hw-support/blob/main/docs/contributing.rst).


## License

[CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/)
