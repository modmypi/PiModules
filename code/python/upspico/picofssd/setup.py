
"""picofssd: UPSPIco file-safe shutdown daemon

This script is intended for use with the PiModules(R) UPSPIco
uninterruptible power supply for use with a Raspberry Pi computer.
"""

classifiers = """\
Development Status :: 5 - Testing/Beta
Intended Audience :: PiModules UPS PiCo Product developers and partners (change to customers when published)
License :: GNU General Public License Version 3
Programming Language :: Python >= 2.7
Topic :: PiModules(R)
Topic :: UPS PIco support daemon
Operating System :: Linux (Raspbian)
"""


from setuptools import setup

doclines = __doc__.split("\n")



datafiles=[
	('/etc/pimodules/picofssd', ['etc/pimodules/picofssd/emailAlertBody.template', 'etc/pimodules/picofssd/emailAlertSubject.template', 'etc/pimodules/picofssd/picofssd.xml']),
	('/etc/default', ['default/picofssd']),
	('/etc/systemd/system', ['systemd/picofssd.service'])
]

setup(name='picofssd',
      version='0.1dev',
      description=doclines[0],
      long_description = "\n".join(doclines[2:]),
      license='GPL3',
      author='Mike Ray',
      author_email='mike.ray@btinternet.com',
      url='http://pimodules.com',
      platforms=['POSIX'],
      classifiers = list(filter(None, classifiers.split("\n"))),
      scripts=['scripts/picofssd', 'scripts/picofssdxmlconfig'],
      data_files = datafiles
      )
