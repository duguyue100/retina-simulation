"""This script disovers and tests OpenCV bioinspired module's API.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import cv2
from moviepy.video.io.ffmpeg_reader import FFMPEG_VideoReader

from simretina import dataset, gui, retina

option = "test-movie-py"

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

if option == "test-bgr2rgb-sequence":
    frames, size = dataset.get_horse_riding()

    new_frames = gui.trans_bgr2rgb_seq(frames)

    for frame in new_frames:
        cv2.imshow("test", frame)
        cv2.waitKey(delay=0)

    print len(new_frames)

if option == "test-ratio-keep-resize":
    frame, size = dataset.get_lenna()
    frame = gui.resize(frame, (400, 300), ratio_keep=True)
    print frame.shape

if option == "test-dict-compare":
    para_dict_old = {}
    para_dict_old["a"] = 1
    para_dict_old["b"] = 2

    para_dict_new = {}
    para_dict_new["a"] = 1
    para_dict_new["b"] = 2

    print retina.compare_para_dict(para_dict_old, para_dict_new)

if option == "test-setup-function":
    eye = retina.init_retina((300, 200))

    print type(eye.setupOPLandIPLParvoChannel)
    print type(eye.setupIPLMagnoChannel)
    print eye.getInputSize()

if option == "test-movie-py":
    video = FFMPEG_VideoReader("./simretina/retina-data/HorseRiding.avi")

    frame = video.read_frame()

    for i in xrange(video.nframes):
        frame = video.read_frame()
        cv2.imshow("test", frame)
        cv2.waitKey(0)
