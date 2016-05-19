"""This script disovers and tests OpenCV bioinspired module's API.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import cv2
from cv2 import bioinspired

from simretina import dataset, gui

option = "test-bgr2rgb-sequence"

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

if option == "test-bgr2rgb-sequence":
    frames, size = dataset.get_horse_riding()

    new_frames = gui.trans_bgr2rgb_seq(frames)

    for frame in new_frames:
        cv2.imshow("test", frame)
        cv2.waitKey(delay=0)

    print len(new_frames)
