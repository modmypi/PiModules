
"""pimodules: PiModules(R) Product support Python package

A package which contains code to support PiModules products of various kinds.
"""

classifiers = """\
Development Status :: 5 - Testing/Beta
Intended Audience :: PiModules Product Developers
License :: GNU General Public License Version 3
Programming Language :: Python >= 2.7
Topic :: PiModules(R)
Topic :: PiModules(R) Products Python Package
Operating System :: Linux (Raspbian)
"""


from distutils.core import setup

doclines = __doc__.split("\n")

setup(name='pimodules',
      version='0.1dev',
      description=doclines[0],
      long_description = "\n".join(doclines[2:]),
      license='GPL3',
      author='Mike Ray',
      author_email='mike.ray@btinternet.com',
      url='http://pimodules.com',
      platforms=['POSIX'],
      classifiers = filter(None, classifiers.split("\n")),
      packages=['pimodules'],
      )
