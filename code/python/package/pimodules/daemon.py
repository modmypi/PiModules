
import sys
import os
import time
import atexit
import logging
import logging.handlers
import contextlib

from signal import SIGTERM



class Daemon(object):
	"""
	A forking daemon

	Usage: subclass the Daemon class and override the run() method
	"""
	def __init__(self, pidfile, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
		self.log = logging.getLogger(__name__)
		self.log.setLevel(logging.DEBUG)
		handler = logging.handlers.SysLogHandler(address = '/dev/log')
		formatter = logging.Formatter('%(module)s[%(process)s]: <%(levelname)s>: %(message)s')
		handler.setFormatter(formatter)
		self.log.addHandler(handler)

		self.stdin = stdin
		self.stdout = stdout
		self.stderr = stderr

		self.pidfile = pidfile


	def redirect_stream(self, system_stream, target_stream):
		""" Redirect a system stream to a specified file.
			:param standard_stream: A file object representing a standard I/O stream.
			:param target_stream: The target file object for the redirected stream, or ``None`` to specify the null device.
			:return: ``None``.
			`system_stream` is a standard system stream such as
			``sys.stdout``. `target_stream` is an open file object that
			should replace the corresponding system stream object.
			If `target_stream` is ``None``, defaults to opening the
			operating system's null device and using its file descriptor.
			"""
		if target_stream is None:
			target_fd = os.open(os.devnull, os.O_RDWR)
		else:
			target_fd = os.open(target_stream, os.O_RDWR)
		system_stream.flush()
		os.dup2(target_fd, system_stream.fileno())

	def daemonize(self):
		"""
		do the UNIX double-fork magic, see Stevens' "Advanced
		Programming in the UNIX Environment" for details (ISBN 0201563177)
		http://www.erlenstar.demon.co.uk/unix/faq_2.html#SEC16
		"""

		try:
			pid = os.fork()
			if pid > 0:
				# exit first parent
				sys.exit(0)
		except OSError as e:
			sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
			sys.exit(1)

		# decouple from parent environment
		os.chdir("/")
		os.setsid()
		os.umask(0)

		# do second fork
		try:
			pid = os.fork()
			if pid > 0:
				# exit from second parent
				sys.exit(0)
		except OSError as e:
			sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
			sys.exit(1)

		# redirect standard file descriptors
		self.redirect_stream(sys.stdin, self.stdin)
		self.redirect_stream(sys.stdout, self.stdout)
		self.redirect_stream(sys.stderr, self.stderr)

		# write pidfile
		atexit.register(self.deletePidFile)
		pid = str(os.getpid())
		open(self.pidfile,'w+').write("%s\n" % pid)

	def deletePidFile(self):
		os.remove(self.pidfile)

	def start(self, daemonize=True):
		"""
		Start the daemon
		"""

		self.daemon = daemonize


		if daemonize:
			# Check for a pidfile to see if the daemon is already running
			try:
				pf = open(self.pidfile,'r')
				pid = int(pf.read().strip())
				pf.close()
			except IOError:
				pid = None

		if daemonize:
			if pid:
				message = "pidfile %s already exist. Daemon already running?\n"
				sys.stderr.write(message % self.pidfile)
				sys.exit(1)

		# Start the daemon
		if daemonize:
			self.daemonize()

		self.run()

	def stop(self):
		"""
		Stop the daemon
		"""

		if self.daemon:
			# Get the pid from the pidfile
			try:
				pf = file(self.pidfile,'r')
				pid = int(pf.read().strip())
				pf.close()
			except IOError:
				print('could not get pid')
				pid = None

		if self.daemon:
			if not pid:
				message = "pidfile %s does not exist. Daemon not running?\n"
				sys.stderr.write(message % self.pidfile)
				return # not an error in a restart

		if self.daemon:
			# Try killing the daemon process
			try:
				while 1:
					os.kill(pid, SIGTERM)
					time.sleep(0.1)
			except OSError as err:
				err = str(err)
				if err.find("No such process") > 0:
					if os.path.exists(self.pidfile):
						os.remove(self.pidfile)
				else:
					print(str(err))
					sys.exit(1)

	def restart(self):
		"""
		Restart the daemon
		"""
		self.stop()
		self.start()

	def run(self):
		"""
		You should override this method when you subclass Daemon. It will be called after the process has been
		daemonized by start() or restart().
		"""

		raise NotImplementedError
