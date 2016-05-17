"""GUI related functions.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import cv2
import numpy as np


def bgr2rgb(frame):
    """Convert color span from BGR to RGB.

    Parameters
    ----------
    frame : numpy.ndarray
        a given frame

    Returns
    -------
    new_frame : numpy.ndarray
        a converted frame
    """
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


def trans_bgr2rgb_seq(frames):
    """Transfer BGR sequence to RGB sequence.

    Parameters
    ----------
    frames : list
        a given BGR sequence

    Returns
    -------
    new_frames : list
        a converted RGB sequence
    """
    return [bgr2rgb(frame) for frame in frames]


def create_viewer_field(frames, inter_padding=20, border_padding=40,
                        color=[0, 0, 0]):
    """Create Viewer field by gluing multiple frames together.

    Parameters
    ----------
    frames : list
        list of frames in order, assumed order
        [original BGR frame, Parvo frame, Magno frame]
        P.S. make sure Magno frame is also a BGR image
    inter_padding : int
        spacing between each frame
    border_padding : int
        append border to fused frame
    color : list
        3 value that specify the color of the border

    Returns
    -------
    viewer_frame : numpy.ndarray
        A new frame that fit in viewer's size
    """
    viewer_frame = np.array([])

    for frame in frames:
        temp_frame = cv2.copyMakeBorder(frame, inter_padding, inter_padding,
                                        inter_padding, inter_padding,
                                        cv2.BORDER_CONSTANT, value=color)

        if not viewer_frame.size:
            viewer_frame = temp_frame
        else:
            viewer_frame = np.hstack((viewer_frame, temp_frame))

    viewer_frame = cv2.copyMakeBorder(viewer_frame, inter_padding,
                                      inter_padding, inter_padding,
                                      inter_padding, cv2.BORDER_CONSTANT,
                                      value=color)
    return viewer_frame


def get_viewer_frame(frame, viewer_size):
    """Get viewer frame.

    Parameters
    ----------
    frame : numpy.ndarray

    viewer_size : tuple

    Returns
    -------
    viewer_frame : numpy.ndarray
    """
    return cv2.resize(frame, (viewer_size[1], viewer_size[0]),
                      interpolation=cv2.INTER_CUBIC)
