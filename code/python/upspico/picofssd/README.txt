
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

To install the `picofssd` script:

	sudo python setup.py install

You will need to install the `pimodules` Python package as well. See `../../pimodules/README.md`.

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

* setup.cfg

Config file used by the Python setup tools.

* setup.py

The Python setup tools setup script.

