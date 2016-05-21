"""Setup script for the simretina package.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

from setuptools import setup

classifiers = """
Development Status :: 4 - Beta
Intended Audience :: Science/Research
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python :: 2.7
Topic :: Utilities
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Simulation
Topic :: Scientific/Engineering :: Image Processing
Topic :: Software Development :: Libraries :: Python Modules
License :: OSI Approved :: MIT License
"""

try:
    from simretina import __about__
    about = __about__.__dict__
except ImportError:
    about = dict()
    exec(open("simretina/__about__.py").read(), about)

setup(
    name='simretina',
    version=about['__version__'],

    author=about['__author__'],
    author_email=about['__author_email__'],

    url=about['__url__'],

    packages=['simretina'],
    package_data={'simretina': ['retina-data/*.*']},
    scripts=['script/retina_viewer.py'],

    classifiers=list(filter(None, classifiers.split('\n'))),
    description='Simulation of the Retina with OpenCV.',
    long_description=open('README.md').read()
)
