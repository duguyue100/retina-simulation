# Simulation of the Retina with OpenCV

[![PyPI](https://img.shields.io/pypi/v/simretina.svg?maxAge=2592000)](https://pypi.python.org/pypi/simretina)
[![PyPI](https://img.shields.io/pypi/pyversions/simretina.svg?maxAge=2592000)](https://pypi.python.org/pypi/simretina)

[![Build Status](https://travis-ci.org/duguyue100/retina-simulation.svg?branch=master)](https://travis-ci.org/duguyue100/retina-simulation)
[![Build status](https://ci.appveyor.com/api/projects/status/s1qiaajjraq6t2i0/branch/master?svg=true)](https://ci.appveyor.com/project/duguyue100/retina-simulation/branch/master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ffa7d1cf03e74bb2adfe60b91fb7479b)](https://www.codacy.com/app/duguyue100/retina-simulation?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=duguyue100/retina-simulation&amp;utm_campaign=Badge_Grade)
[![Requirements Status](https://requires.io/github/duguyue100/retina-simulation/requirements.svg?branch=master)](https://requires.io/github/duguyue100/retina-simulation/requirements/?branch=master)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://raw.githubusercontent.com/duguyue100/retina-simulation/master/LICENSE)


This project is our final project to _Computer Simulation for Sensory Systems_.

Detailed software setup can be found from [WIKI](https://github.com/duguyue100/retina-simulation/wiki/Software-Setup)

## Todos

- [x] Update dataset module [WIKI](https://github.com/duguyue100/retina-simulation/wiki/simretina-Python-API) [2016-05-09]
- [x] update basic processing functions on GUI and retina model [2016-05-17]
- [x] First release of GUI by `PyQtGraph` [2016-05-21]
- [x] Webcam support for the package [2016-05-21]
- [x] Command line support for viewer [2016-05-21]
- [x] External file support [2016-05-21]
- [ ] Redesign GUI to add fast tone transformation
- [ ] `unittest`-based tests
- [x] Travis-CI integration [2016-05-21]
- [x] Replace `PyAV` to `moviepy` for better compatibility. [2016-05-22]
- [x] AppVeyor CI integration [2016-05-22]

## Requirements

__We highly recommend installing [Anaconda](https://anaconda.org/) as your default Python distribution in order to avoid
unnecessary messes.__

+ OpenCV3: `conda install -c menpo opencv3=3.1.0` (for image and video processing)
+ (OPTIONAL) FFMPEG: `conda install -c soft-matter ffmpeg=2.2.4` (for supporting video analysis) (optional: `moviepy` will download FFMPEG at the first time, but you should install it if you need it for other projects.)
+ PyQtGraph: `conda install pyqtgraph` (for GUI viewer)

Note that above requirements are installed with `conda` - the package management system
provided along with `Anaconda`. Make sure you installed them before installing the package

Following packages are listed in `requirements.txt`, they will be installed automatically:

+ `numpy` (for numerical computing)
+ `moviepy` (for read videos)

## Installation

__Assumed you've installed above requirements__

Get the stable release by:

```
pip install simretina
```

Get the bleeding edge by:

```
pip install git+git://github.com/duguyue100/retina-simulation.git \
-r https://raw.githubusercontent.com/duguyue100/retina-simulation/master/requirements.txt
```

## Start Retina Simulation Viewer

__CAUTION: WE FOUND THAT THE VIEWER MAY CRASH RANDOMLY WHILE YOU ARE SWITCHING THE MODE.
WE ARE STILL TESTING THE PROGRAM, BEFORE WE SOLVED IT, YOU CAN SIMPLY RESTART THE VIEWER.__

After you successfully installed the package, you are able to start the
retina viewer from terminal:

```
retina_viewer.py
```

Note that above file is automatically added in your system path once
you installed the package. (Yes, with the extension)

If you didn't install FFMPEG, at the first time, `moviepy` will download FFMPEG
for you.

__FOR WINDOWS USER:__ If you type above command, your system either start the viewer
right away or it will ask for the program that opens the file, you should then find and choose
`python.exe` from your Anaconda installation. If it's not responding, you may want to
open a new console and type above command again. If it still doesn't work, please submit an [issue](https://github.com/duguyue100/retina-simulation/issues).

## Contacts

Yuhuang Hu  
Email: yuhuang.hu@uzh.ch
