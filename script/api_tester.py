"""This script disovers and tests OpenCV bioinspired module's API.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import cv2
from cv2 import bioinspired

from simretina import dataset

option = "test-retina-class"

if option == "test-builtin-image":
    # testing for builtin dataset
    frame, size = dataset.get_lenna()
    print frame.shape
    print size

if option == "test-builtin-video":
    # testing for builtin video
    frames, size_v = dataset.get_taichi()
    print len(frames)
    print size_v

if option == "test-retina-class":
    frame, size = dataset.get_lenna()
    retina = bioinspired.createRetina(size[:2])
    print type(retina)
