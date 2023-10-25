
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
	('.', ['scripts/picofssd.py','scripts/picofssdxmlconfig'])
]

setup(name='picofssd',
      version='0.2.dev0',
      description=doclines[0],
      long_description = "\n".join(doclines[2:]),
      license='GPL3',
      author='Mike Ray',
      author_email='mike.ray@btinternet.com',
      url='http://pimodules.com',
      platforms=['POSIX'],
      classifiers = list(filter(None, classifiers.split("\n"))),
      install_requires=['fake-rpi','xmltodict','jinja2','rpi.gpio'],
      packages=['scripts'],
      data_files = datafiles
      )
