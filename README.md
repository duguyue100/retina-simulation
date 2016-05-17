# Simulation of the Retina with OpenCV

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](http://doge.mit-license.org)

This project is our final project to _Computer Simulation for Sensory Systems_.

Detailed software setup can be found from [WIKI](https://github.com/duguyue100/retina-simulation/wiki/Software-Setup)

## Updates

+ :star: Update dataset module [WIKI](https://github.com/duguyue100/retina-simulation/wiki/simretina-Python-API) [2016-05-09]

## Requirements

__We highly recommend installing [Anaconda](https://anaconda.org/) as your default Python distribution in order to avoid
unnecessary messes.__

+ OpenCV3: `conda install -c menpo opencv3=3.1.0` (for image and video processing)
+ FFMPEG: `conda install -c soft-matter ffmpeg=2.2.4` (for supporting video analysis)
+ PyAV: `conda install -c soft-matter pyav=v0.2.3.post0` (for reading videos)

Note that above requirements are installed with `conda` - the package management system
provided along with `Anaconda`. Make sure you installed them before installing the package

## Installation

__Assumed you've installed above requirements__

Get the bleeding edge by:

```
pip install git+git://github.com/duguyue100/retina-simulation.git
```

## Contacts

Yuhuang Hu  
Email: yuhuang.hu@uzh.ch
