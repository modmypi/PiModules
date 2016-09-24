
UPSPIco(R) File-safe Shutdown Daemon
====================================

This is a Python daemon script which is intended for use with the PiModules(R) UPSPIco, an 
uninterruptable power supply which plugs into the GPIO bus of a Raspberry Pi(TM).

The purpose of the UPSPIco product, and this daemon, is to provide a period of continued operation 
of the Pi in the event of failure or disconnection of the external power supply connected to a 
Raspberry Pi.

Name
----

The name of the script, `picofssd` is derived from the hardware product name and the function:

UPS PIco file-safe shutdown daemon = `picofssd`.

Installation
------------

You will need to have installed the `pimodules` Python package. See 
`../../package/README.md`.

You will also need to have installed the Python dependencies outlined in the README.txt file in the 
above named directory, these are `jinja2` and `xmltodict`.

Now install the `picofssd` script:

	sudo python setup.py install



Hardware Installation
---------------------

For instructions for installation of the PiModules(R) UPSPIco, see the documentation provided with the hardware.

Enabling the Daemon
-------------------

Once the script has been installed, it can be installed to the `SysVInit` system like this:

	sudo update-rc.d picofssd defaults

And enabled to run at boot time like this:

	sudo update-rc.d picofssd enable

Now when the Pi is rebooted the daemon should start.

To disable the daemon so that it does not start at boot time:

	sudo update-rc.d picofssd disable

And to remove it from SysVInit:

	sudo update-rc.d picofssd remove

To start the daemon without rebooting:

	sudo /etc/init.d/picofssd start

To stop it:

	sudo /etc/init.d/picofssd stop

There is no `restart` or `reload` facility.


Dependancy Installation
-----------------------

Running the file-safe shutdown daemon requires the installation of some dependancies.

Here is how to install those dependancies and an explanation of each.

The fastest way is just to follow these commands:

	sudo apt-get install -y python-dev python-pip python-serial python-smbus python-jinja2 
	sudo pip install psutil
	sudo pip install xmltodict

And here is a longer explanation of the purpose of each dependancy:

* python-dev

Some development libraries required by some of the other code.

* python-pip

The Python package installer, used to install some of the other pure Python dependancies.

* python-serial

Required by scripts used to update the UPS PIco firmware, but not actually used by the file-safe 
shutdown daemon.

* python-smbus

Used by scripts that read values from the UPS PIco over the serial i2C bus.

* python-jinja2 

A templating engine used by the file-safe shutdown daemon to generate alert emails.

* psutil

Used by scripts that update the PIco firmware.

* xmltodict

An XML to Python dictionary and vice-versa library used by the file-safe shutdown daemon to read and 
write it's XML configuration files.

Directory Contents
------------------

* ChangeLog

Change history.

* default/

Default daemon SysVInit configuration to go to `/etc/default/`

* doc/

Documentation.

* init.d/

Files to go to `/etc/init.d` to support SysVInit startup of fssd.

* LICENSE

Text of the Gnu General Public License version 3.

* MANIFEST.in

MANIFEST template used by the Python setup tools.

* README.txt

This file.

* scripts/

Python script which is the file-safe shutdown daemon.

* tools/

Contains some odd files not installed by the installation process.

* setup.cfg

Config file used by the Python setup tools.

* setup.py

The Python setup tools setup script.

