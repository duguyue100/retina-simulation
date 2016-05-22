"""Utility functions and pre-load examples.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import os
from os.path import join
import cv2
from moviepy.video.io.ffmpeg_reader import FFMPEG_VideoReader

from simretina import package_data_path


def check_image_file(file_name):
    """Check if given file is a image file.

    Parameters
    ----------
    file_name : string
        a given file path (absolute path)

    Returns
    -------
    status : bool
        True if it's a image file, False if it isn't
    """
    if not os.path.isfile(file_name):
        raise ValueError("The given file is not existed!")

    fn, fex = os.path.splitext(file_name)
    if fex not in [".jpg", ".jpe", ".jpeg", ".jp2", ".png", ".bmp", ".dib",
                   ".pbm", ".pgm", ".ppm", ".sr", ".ras", ".tiff", ".tif"]:
        return False
    else:
        return True


def check_video_file(file_name):
    """Check if given file is a video file.

    Parameters
    ----------
    file_name : string
        a given file path (absolute path)

    Returns
    -------
    status : bool
        True if it's a video file, False if it isn't
    """
    if not os.path.isfile(file_name):
        raise ValueError("The given file is not existed!")

    fn, fex = os.path.splitext(file_name)
    if fex not in [".avi", ".mp4"]:
        return False
    else:
        return True


def get_image(image_path, color=True, size=True):
    """Get image by given image path.

    Parameters
    ----------
    image_path : string
        target image absolute path
    color : bool
        if color is True then return a color frame with BGR encoding.
        if color is False then return a grey scale frame.
    size : bool
        if size is True then return the size of the frame.
        if size is False then just return the frame.

    Returns
    -------
    frame : numpy.ndarray
        a frame that contains target image.
    size : tuple
        size of the frame (optional).
    """
    frame = cv2.imread(image_path)

    if color is False:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if size is True:
        return frame, frame.shape
    else:
        return frame


def get_video(vid_path, color=True, size=True):
    """Get video by given video path.

    Parameters
    ----------
    image_path : string
        target image absolute path
    color : bool
        if color is True then return color frames with BGR encoding.
        if color is False then return grey scale frames.
    size : bool
        if size is True then return the size of the frame.
        if size is False then just return the frame.

    Returns
    -------
    frames : list
        a list of frames that contains the video
    size : tuple
        size of the frame (optional).
    """
    vid_container = FFMPEG_VideoReader(vid_path)

    frames = []
    for i in range(vid_container.nframes):
        frame_t = vid_container.read_frame()
        frame_t = cv2.cvtColor(frame_t, cv2.COLOR_RGB2BGR)
        if color is False:
            frame_t = cv2.cvtColor(frame_t, cv2.COLOR_BGR2GRAY)
        frames.append(frame_t)

    if size is True:
        return frames, frames[0].shape
    else:
        return frames


def get_lenna(color=True, size=True):
    """Get Lenna image.

    Parameters
    ----------
    color : bool
        if color is True then return a color frame with BGR encoding.
        if color is False then return a grey scale frame.
    size : bool
        if size is True then return the size of the frame.
        if size is False then just return the frame.

    Returns
    -------
    frame : numpy.ndarray
        a frame that contains Lenna image.
    size : tuple
        size of the frame (optional).
    """
    lenna_path = join(package_data_path, "lenna.png")
    if not os.path.isfile(lenna_path):
        raise ValueError("The Lenna image is not existed!")

    return get_image(lenna_path, color=color, size=size)


def get_dog(color=True, size=True):
    """Get dog image.

    The picture of dog is retrieved from Caltech-256 datasets which
    you can find from [here](www.vision.caltech.edu/Image_Datasets/Caltech256/)

    Parameters
    ----------
    color : bool
        if color is True then return a color frame with BGR encoding.
        if color is False then return a grey scale frame.
    size : bool
        if size is True then return the size of the frame.
        if size is False then just return the frame.

    Returns
    -------
    frame : numpy.ndarray
        a frame that contains dog image.
    size : tuple
        size of the frame (optional).
    """
    dog_path = join(package_data_path, "dog.jpg")
    if not os.path.isfile(dog_path):
        raise ValueError("The Dog image is not existed!")

    return get_image(dog_path, color=color, size=size)


def get_yuhuang(color=True, size=True):
    """Get Yuhuang Hu's photo.

    Parameters
    ----------
    color : bool
        if color is True then return a color frame with BGR encoding.
        if color is False then return a grey scale frame.
    size : bool
        if size is True then return the size of the frame.
        if size is False then just return the frame.

    Returns
    -------
    frame : numpy.ndarray
        a frame that contains Yuhuang Hu's photo.
    size : tuple
        size of the frame (optional).
    """
    yh_path = join(package_data_path, "yuhuang-hu-photo.png")
    if not os.path.isfile(yh_path):
        raise ValueError("The Yuhuang Hu's photo is not existed!")

    return get_image(yh_path, color=color, size=size)


def get_horse_riding(color=True, size=True):
    """Get Horse Riding video sequence.

    The video is retrieved from UCF-101 dataet which is
    available from [here](crcv.ucf.edu/data/UCF101.php)

    Parameters
    ----------
    color : bool
        if color is True then return color frames with BGR encoding.
        if color is False then return grey scale frames.
    size : bool
        if size is True then return the size of the frame.
        if size is False then just return the frame.

    Returns
    -------
    frame : list
        list of frames that contains Horse Riding video.
    size : tuple
        size of the frame (optional).
    """
    hr_path = join(package_data_path, "HorseRiding.avi")
    if not os.path.isfile(hr_path):
        raise ValueError("The Horse Riding video is not existed!")
    return get_video(hr_path, color=color, size=size)


def get_taichi(color=True, size=True):
    """Get Tai Chi video sequence.

    The video is retrieved from UCF-101 dataet which is
    available from [here](crcv.ucf.edu/data/UCF101.php)

    Parameters
    ----------
    color : bool
        if color is True then return color frames with BGR encoding.
        if color is False then return grey scale frames.
    size : bool
        if size is True then return the size of the frame.
        if size is False then just return the frame.

    Returns
    -------
    frame : list
        list of frames that contains Tai Chi video.
    size : tuple
        size of the frame (optional).
    """
    tc_path = join(package_data_path, "TaiChi.avi")
    if not os.path.isfile(tc_path):
        raise ValueError("The Tai Chi video is not existed!")
    return get_video(tc_path, color=color, size=size)
