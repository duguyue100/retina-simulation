"""GUI related functions.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import numpy as np


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
    print len(frames)
