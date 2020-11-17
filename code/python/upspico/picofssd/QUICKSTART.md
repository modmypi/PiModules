
Installation
------------

See README.txt in this directory for dependencies.

	sudo python3 setup.py install
	cd ../../package
	sudo python3 setup.py install
	sudo update-rc.d picofssd defaults #TODO change to upstart!
	sudo update-rc.d picofssd enable

After dependancies have been installed and the Pi has been rebooted the daemon should start.

XML Configuration File
----------------------

The file-safe shutdown daemon requires an XML configuration file to run.  It controls the email
alert settings that the daemon uses to know how to send an email when it detects a shutdown has been
requested by the UPS PIco.

A script is installed by the installation process which can be used to create this XML file.

It's name is:

	picofssdxmlconfig

When run it will ask for a number of settings that will be written to the XML file.

To run it to create a new XML file:

	picofssdxmlconfig -d -o picofssd.xml

The `-d` switch tells the script to start with a fresh `--default` configuration.

The `-o` switch names the output file.

When the script has been run and a file has been generated it should be moved to:

	/etc/pimodules/picofssd/picofssd.xml

Or it can create this file directly like this:

	sudo picofssdxmlconfig -d -o /etc/pimodules/picofssd/picofssd.xml

You can also read from an existing XML configuration file and create a new one, keeping some of the
settings from the old file and only changing your choice of settings.  To do this:

	picofssdxmlconfig -i oldfile.xml -o newfile.xml

Settings will be read from the old file and presented for you to either keep or replace and write
forward to the new file.

Here is an explanation of the settings you will be asked to enter.

* Enable email alerts

Enter 'y' or 'n'. No will disable email alerts.

* Email server

The name of the email server you intend to use to send the email.

* Log in user name

The log in name required by the server.  Usually your full email address.

* Sender email address

Often the same value you entered for the user name above.

* Recipient email address

The email address to which the alert email should be sent.

* Password

The password required by the email server.

The password is stored on the filesystem encrypted and decryypted by the daemon when it sends an
email.

* Security method

Method of security used by the email server.

Options are 'ssl' or 'tls'.

* Absolute path to the email subject template

A file name of the `jinja2` template used by the daemon to generate the text for the email subject.

* Absolute path to the email body template

Absolute path to a `jinja2` template used by the daemon to generate the email message body.

In most cases you will be asked to confirm each entry and asked to enter each twice to make sure you
entered them correctly.
