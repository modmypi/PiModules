
PiModules Python Package
========================

This directory contains the installation scripts and the PiModules(R) Python package that supports PiModules products.

Installation
------------

First you need to install a couple of Python dependencies.  Install python-pip like this:

	sudo apt-get install python-pip

Then install both `jinja2` and `xmltodict` like this:

	sudo pip install jinja2
	sudo pip install xmltodict

Both of the above libraries are used in the sending of email alerts by the file-safe shutdown 
daemon.

Now install the pimodules package:

	sudo python setup.py install

You can record what files are installed by the above process by running it like this:

	sudo python setup.py install --record <filename>

Where <filename> will be a text file containing one line per file installed by the process.

If the `--record` function was used, files can be easily uninstalled in this way:

	cat <filename> | xargs sudo rm

Where `<filename>` was the name of the file recorded in the installation process.

Package Contents
----------------

* daemon.py

Generic Python `daemon` code used by the `picofssd` script, the UPS PIco file-safe shutdown daemon.

Directory Contents
------------------

* ChangeLog

Record of changes to this package and it's files.

* LICENSE

Text of the Gnu General Public License version 3.

* MANIFEST.in

MANIFEST template used by Python setup tools.

* pimodules/

The code is in here.

* README.txt

This file.

* setup.py

Installation file, see `README.md` in the directory above this one.



