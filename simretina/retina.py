"""Wrapper for cv2.bioinspired module.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import cv2
import numpy as np
from cv2 import bioinspired


def init_retina(size):
    """Initialize a retina by given parameters.

    Parameters
    ----------
    size : tuple
        The size of the retina receptive field (height, width)
    """
    if len(size) != 2:
        raise ValueError("Invalid size setting.")

    return bioinspired.createRetina((size[1], size[0]))


def get_opl_frame(retina, frame, get_parvo=True, get_magno=True,
                  color_mode="color"):
    """Get Parvo frame by given retina model and original image.

    Parameters
    ----------
    retina : cv2.bioinspired_Retina
        the retina model
    frame : numpy.ndarray
        a frame
    color_mode : string
        indicate color mode, the options are "color", "grey"

    Returns
    -------
    parvo_frame : numpy.ndarray
        a BGR colored parvo frame
    magno_frame ; numpy.ndarray
        a BGR colored magno frame
    """
    retina.run(frame)

    parvo_frame = retina.getParvo()
    magno_frame = retina.getMagno()

    if color_mode == "grey":
        parvo_frame = grey2color(parvo_frame)

    magno_frame = grey2color(magno_frame)

    if get_parvo is False and get_magno is True:
        return magno_frame
    elif get_parvo is True and get_magno is False:
        return parvo_frame
    elif get_parvo is True and get_magno is True:
        return parvo_frame, magno_frame


def grey2color(frame):
    """Transform a grey frame to color frame by duplication.

    Parameters
    ----------
    frame : numpy.ndarray
        a grey frame

    Returns
    -------
    new_frame : numpy.ndarray
        a color frame by duplicating the frame to each color channel.
    """
    if frame.ndim != 2:
        raise ValueError("Input frame is not a grey frame.")

    return np.transpose(np.tile(frame, (3, 1, 1)), (1, 2, 0))
