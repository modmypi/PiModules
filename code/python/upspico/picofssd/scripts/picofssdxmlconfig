#!/usr/bin/python

import argparse
import xmltodict
import getpass
import base64
from pimodules import configuration


def get_yesno(help, prompt):
	"""
	Accepts either 'y' or 'n' at the command-line
	"""
	print help
	yn = None
	while yn not in ['y','n']:
		yn = raw_input(prompt) or 'x'
		if yn not in ['y','n']:
			print "Please answer 'y' or 'n'"

	return yn == 'y'

def is_correct(prompt, strval):
	"""
	Asks the user whether a value entered is correct
	"""
	yn = None
	while yn not in ['y','n']:
		yn = raw_input(format("You entered %s for the %s, is this correct? " % (strval, prompt))).lower()
		if yn not in ['y','n']:
			print "Please answer 'y' or 'n'"

	return yn == 'y'

def enter_string(help, prompt, default=None, twice=True):
	"""
	Accepts a string value at the command line, asks the user to confirm whether it is the correct
	value	and optionally does the accept twice and compares the two occurrences
	"""
	print help
	default = default or ''
	savedefault = default
	while True:
		if default:
			pt = format("Enter the value for the %s [ %s ]: " % (prompt, default))
			str1 = raw_input(pt) or default
		else:
			pt = format("Enter the value for the %s: " % prompt)
			str1 = raw_input(pt)
			if not str1:
				print "You cannot enter a zero-length string"
				continue

		if is_correct(prompt, str1):
			if not twice:
				return str1
			else:
				if str1 != default:
					default = ''

			if default:
				pt = format("Re-enter the value for the %s (%s): " % (prompt, default))
				str2 = raw_input(pt) or default
			else:
				pt = format("Re-enter the value for the %s: " % prompt)
				str2 = raw_input(pt)

			if str1 == str2:
				break
			else:
				print "Values do not match"

	return str2



def enter_integer(help, prompt, default=None, twice=True):
	"""
	Accepts a string at the command-line. Checks whether the string is a valid
	integer, optionally accepting it twice and comparing the two strings to make sure
	they are the same
	"""
	print help
	default = default or ''
	savedefault = default
	while True:
		if default:
			pt = format("Enter the value for the %s [ %s ]: " % (prompt, default))
			str1 = raw_input(pt) or default
		else:
			pt = format("Enter the value for the %s: " % prompt)
			str1 = raw_input(pt)
			if not str1:
				print "You cannot enter a zero-length string"
				continue
		try:
			integer = int(str1)
		except ValueError:
			print "You must enter a valid integer"
			continue
		except TypeError:
			print "You must enter a valid integer"
			continue

		if is_correct(prompt, str1):
			if not twice:
				return str1
			else:
				if str1 != default:
					default = ''

			if default:
				pt = format("Re-enter the value for the %s (%s): " % (prompt, default))
				str2 = raw_input(pt) or default
			else:
				pt = format("Re-enter the value for the %s: " % prompt)
				str2 = raw_input(pt)

			if str1 == str2:
				break
			else:
				print "Values do not match"

	return str2


def double_enter_password(help, prompt):
	"""
	Accepts a password entered at the command-line and checks both instances
	are the same
	"""
	print help
	while True:
		pt = format("Enter the value for the %s: " % prompt)
		str1 = getpass.getpass(pt)
		pt = format("Re-enter the value for the %s: " % prompt)
		str2 = getpass.getpass(pt)

		if str1 == str2:
			break
		else:
			print "Values do not match"

	return str2


def get_choice(help, prompt, choices, show=False):
	"""
	Accepts a string at the command-line. Choice entered must be one of the choices in the list. Optionally shows the choices
	available in the prompt
	"""
	print help
	choice = ''
	if show:
		prompt += '(' + ','.join(choices) + ')'

	while choice.lower() not in choices:
		try:
			choice = raw_input(prompt).lower()
		except EOFError:
			raise KeyboardInterrupt

	return choice


#-- main program

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-d", "--default",
		help="Start from a fresh XML configuration, do not initialize values from existing XML file",
		action="store_true", default=False)
group.add_argument("-i", "--input-xml",
		help="Read initial configuration values from an existing file")
parser.add_argument("-o", "--output-xml",
		help="Output XML configuration file",
		default='picofssd.xml', required=True)

args = parser.parse_args()

if args.default:
	configdict = configuration.read_config_xml(configuration.DEFAULT_FSSD_XML_CONFIG, True)
else:
		configdict = configuration.read_config_xml(args.input_xml, False)


configsubdict = configdict['root']['fssd:config']['fssd:alerts']['fssd:email']

help = """

Follow the prompts and enter strings for the XML configuration which drives
the UPS PIco file-safe shutdown daemon.

Default values read from the previous XML configuration are shown in square brackets.  Just press enter
to accept a default value.

"""

enabled = get_yesno(help, "Do you want to enable the email alert? ('y', 'n'): ")
configsubdict['fssd:enabled'] = enabled


help = """

Email server.  This is usually something like 'mail.domain.com', where 'domain' reflects the company providing the
email account.

"""

server = configsubdict['fssd:server']
server = enter_string(help, "mail server", default=server,twice=True)
configsubdict['fssd:server'] = server

help = """

Email account user name. This is the user name used to log into the email server.  This is usually
the full email address of the account holder.

"""

username = configsubdict['fssd:username']
username = enter_string(help, "email user name (this is usually the full email address)", default=username, twice=True)
configsubdict['fssd:username'] = username


help = """

Email address of the originator (sender) of the email.  This is usually the same as the user name if
the full email address is used as the server's log in string given above.

"""

sender = configsubdict['fssd:sender-email-address']
sender = enter_string(help, "Sender's email address", default=sender, twice=True)
configsubdict['fssd:sender-email-address'] = sender

help = """

The password for the email server and the email account.

"""

password = double_enter_password(help, "password")
configsubdict['fssd:sender-password'] = base64.b64encode(password)


help = """

The recipient's email address to which the daemon should send an email alert.

"""

recipient = configsubdict['fssd:recipient-email-address']
recipient = enter_string(help, "destination email address", default=recipient, twice=True)
configsubdict['fssd:recipient-email-address'] = recipient


help = """

The security method employed by the email SMTP server.  Permitted methods are SSL (secure server layer)
or TLS (transport level security).

"""

security = get_choice(help, "Enter server security method ", ['ssl', 'tls'], True)
configsubdict['fssd:security'] = security

help = """

The port number the email server uses.  If security was 'SSL', this is probably 465.

The value entered must be a valid integer.

"""

strport = configsubdict['fssd:port']
try:
	port = int(strport)
except ValueError:
	strport = ''
except TypeError:
	strport = ''
strport = enter_integer(help, "port number", default=strport, twice=True)
configsubdict['fssd:port'] = strport


help = """

Absolute path to the template used to generate the subject of the email message
sent by the file-safe shutdown daemon to indicate power failure as detected
by the UPS PIco

"""

prompt =" absolute path to the email subject template"
subject_template = configsubdict['fssd:subject-template']
subject_template = enter_string(help, prompt, default=subject_template, twice=False)
configsubdict['fssd:subject-template'] = subject_template

help = """

Absolute path to the template used to generate the body of the email message
sent by the file-safe shutdown daemon to indicate power failure as detected
by the UPS PIco

"""

prompt =" absolute path to the email body template"
body_template = configsubdict['fssd:body-template']
body_template = enter_string(help, prompt, default=body_template, twice=False)
configsubdict['fssd:body-template'] = body_template





configuration.write_config_xml(args.output_xml, configdict)



