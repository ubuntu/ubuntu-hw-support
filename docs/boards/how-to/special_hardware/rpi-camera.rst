.. _using-the-camera-on-raspberry-pi:

Using the camera on Raspberry Pi
================================

Since Ubuntu 25.04, all `Raspberry Pi`_ models with a CSI port can use the
camera stack.


Connecting a camera module
--------------------------

You can follow the Raspberry Pi's official documentation to `connect a
supported camera module`_ to your Raspberry Pi.

.. warning::
    We do not recommend connecting a camera module while the Raspberry Pi is running,
    and you may experience erratic behavior or unintended reboots if you try it.
    Please plug the camera module while the Raspberry Pi is powered off.


libcamera-apps
--------------

Right after installing Ubuntu on your Raspberry Pi and connecting a camera
module to it, you can use the various applications provided by the
`libcamera-apps` package to test the camera. We will show the usage of 2 of the
applications here: ``cam`` and ``qcam``.


cam
~~~

.. note::
    We recommend setting the ``LIBCAMERA_LOG_LEVELS`` to 4 using
    ``export LIBCAMERA_LOG_LEVELS=*:4`` to avoid cluttering the terminal with logs.

The cam_ utility can be used for basic testing. You can list the connected
cameras using ``cam -l``.

.. terminal::
    :user: ubuntu
    :host: ubuntu

    cam -l

    Available cameras:
    1: 'imx500' (/base/axi/pcie@120000/rp1/i2c@80000/imx500@1a)

You can also capture frames using ``cam`` in the PPM format.

.. terminal::
    :user: ubuntu
    :host: ubuntu

    cam -c 1 --capture --file=frame.ppm

    Using camera /base/axi/pcie@120000/rp1/i2c@80000/imx500@1a as cam0
    cam0: Capture 1 frames
    1237.987399 (0.00 fps) cam0-stream0 seq: 000007 bytesused: 1920000


qcam
~~~~

qcam is a GUI application provided by libcamera that can be used to test the
camera. You can use it by just typing ``qcam`` in the terminal.

.. image:: /images/qcam-dropdown-demo.png
    :alt: The qcam camera selection window, showing a drop-down list of
          available cameras, and brief information about the selected camera

Once you have selected a camera and "OK", the application will show a preview
from the camera.

.. image:: /images/qcam-demo.png
    :alt: The main qcam viewfinder window, showing a preview from the camera
          at the bottom of the window, and a button toolbar at the top with
          actions to stop the preview, save stills, and a label indicating the
          selected camera

- The red cross at the top left exits ``qcam``.

- For Raspberry Pi models supporting more than one camera module, you can
  select another camera by clicking on the text box that shows the camera name.

- You can use the ``Stop Capture`` button to turn off the camera viewfinder,
  and toggle it again to start it.

- The blue arrow can be used to take a snapshot of the current viewfinder image
  as a PNG.

- The ``Save Raw`` button can be used to capture a RAW image.


Supported camera modules
------------------------

We support all the official Raspberry Pi camera modules listed on the
`Raspberry Pi camera hardware spec`_.

Also, the current ``libcamera`` in Ubuntu supports the following camera
sensors:

- IMX219
- IMX283
- IMX290
- IMX296
- IMX327
- IMX378
- IMX415
- IMX462
- IMX477
- IMX500
- IMX519
- IMX708
- OV5647
- OV64A40
- OV7251
- OV9281
- SE327M12


rpicam-apps
-----------

.. warning::

    While the AI Camera module is supported in Ubuntu, the post-processing
    stages require the ``imx500-firmware`` package, which can't be included in
    Ubuntu due to licensing issues. So anything in the `AI camera
    documentation`_ might not work out of the box.

    We are working on fixing the licensing issues with the involved parties.
    Until then, see `Workaround for the IMX500 (AI Camera)`_ below.

You can install :lp-pkg:`rpicam-apps` on your Raspberry Pi with the following
command::

    sudo apt install rpicam-apps

After this, you can use rpicam-apps on Ubuntu the exact same way as you would
on Raspberry Pi OS. To do that, you can follow the `rpicam-apps
documentation`_.


picamera2
---------

You can also use ``picamera2`` to control the camera modules using Python.
While ``picamera2`` is not in the Ubuntu archive yet, you can install it from a
`PPA`_.

::

    sudo apt install ffmpeg python3-picamera2


You can use ``picamera2`` on Ubuntu the same way as you would on Raspberry Pi
OS. Raspberry Pi have created extensive `documentation for picamera2`_. You can
follow it to learn how to use ``picamera2`` on Ubuntu.

.. warning::

    Chapter 9.8 and 9.9 of the ``picamera2`` manual linked above make use of
    the Hailo and IMX500 AI accelerator. The Hailo AI accelerator is not
    supported on Ubuntu, and the IMX500 AI accelerator requires the
    ``imx500-firmware`` package, which can't be included in Ubuntu due to
    licensing issues. So anything in those chapters might not work out of the
    box. We are working on fixing the licensing issues with the involved
    parties.


Workaround for the IMX500 (AI Camera)
-------------------------------------

.. warning::

    While the steps given below will allow you to use the IMX500 camera module
    on Ubuntu,  the ``imx500-firmware`` package is not maintained in Ubuntu
    (yet).

While ``imx500-firmware`` is not available in Ubuntu, you can still get its
deb from Raspberry Pi's `Debian pool`_.

::

    wget https://archive.raspberrypi.org/debian/pool/main/i/imx500-firmware/imx500-firmware_0.FF17.8_all.deb && sudo dpkg -i imx500-firmware_0.FF17.8_all.deb

After this, you can install the ``imx500-all`` package from the `imx500-picam`_
PPA.

::

    sudo apt install ffmpeg
    sudo add-apt-repository ppa:r41k0u/imx500-picam
    sudo apt install imx500-all

That's all! Now you can follow Raspberry Pi's `AI camera documentation`_ to use
it on Ubuntu.

.. figure:: /images/imx500-demo.png
    :alt: rpicam-hello MobileNet application window showing a preview of a
          keyboard with a person's hand over the cursor keys. Around the
          keyboard, an outline is drawn with the label "keyboard 67%"
          indicating the AI module has recognized this portion of the image as
          containing a keyboard.

    Object detection demo using the IMX500 camera module on Ubuntu.

.. LINKS
.. _Raspberry Pi: https://www.raspberrypi.com/
.. _Raspberry Pi camera hardware spec: https://www.raspberrypi.com/documentation/accessories/camera.html#hardware-specification
.. _connect a supported camera module: https://www.raspberrypi.com/documentation/accessories/camera.html
.. _cam: https://libcamera.org/getting-started.html#basic-testing-with-cam-utility
.. _AI camera documentation: https://www.raspberrypi.com/documentation/accessories/ai-camera.html
.. _rpicam-apps documentation: https://www.raspberrypi.com/documentation/computers/camera_software.html#rpicam-apps
.. _PPA: https://help.ubuntu.com/stable/ubuntu-help/addremove-ppa.html.en
.. _documentation for picamera2: https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
.. _Debian pool: https://archive.raspberrypi.org/debian/pool/main/i/imx500-firmware/
.. _imx500-picam: https://launchpad.net/~r41k0u/+archive/ubuntu/imx500-picam
