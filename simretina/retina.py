"""Wrapper for cv2.bioinspired module.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

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


def clear_buffers(retina):
    """Open the eyes after long peroid."""
    retina.clearBuffers()


def get_opl_frame(retina, frame, get_parvo=True, get_magno=True,
                  color_mode="color"):
    """Get Parvo frame by given retina model and original image.

    Parameters
    ----------
    retina : cv2.bioinspired_Retina
        the retina model
    frame : numpy.ndarray
        a frame
    get_parvo : bool
        return parvo frames if True, otherwise False
    get_magno : bool
        return magno frames if True, otherwise False
    color_mode : string
        indicate color mode, the options are "color", "gray"

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

    if color_mode == "gray":
        parvo_frame = gray2color(parvo_frame)

    magno_frame = gray2color(magno_frame)

    if get_parvo is False and get_magno is True:
        return magno_frame
    elif get_parvo is True and get_magno is False:
        return parvo_frame
    elif get_parvo is True and get_magno is True:
        return parvo_frame, magno_frame


def gray2color(frame):
    """Transform a gray frame to color frame by duplication.

    Parameters
    ----------
    frame : numpy.ndarray
        a gray frame

    Returns
    -------
    new_frame : numpy.ndarray
        a color frame by duplicating the frame to each color channel.
    """
    if frame.ndim != 2:
        raise ValueError("Input frame is not a gray frame.")

    return np.transpose(np.tile(frame, (3, 1, 1)), (1, 2, 0))


def get_opl_frames(retina, frames, get_parvo=True, get_magno=True,
                   reopen_eye=True, color_mode="color"):
    """Get provo and magno frames from a sequence of frames.

    Parameters
    ----------
    retina : cv2.bioinspired_Retina
        the retina model
    frame : list
        a list of given frames
    get_parvo : bool
        return parvo frames if True, otherwise False
    get_magno : bool
        return magno frames if True, otherwise False
    reopen_eye : bool
        clear buffers if True, else False
    color_mode : string
        indicate color mode, the options are "color", "grey"
    """
    if len(frames) == 0 or not isinstance(frames, list):
        raise ValueError("No video frame is entered")

    if reopen_eye is True:
        clear_buffers(retina)

    if get_parvo is True:
        parvo_frames = []
    if get_magno is True:
        magno_frames = []

    for frame in frames:
        out_frames = get_opl_frame(retina, frame, get_parvo=get_parvo,
                                   get_magno=get_magno, color_mode=color_mode)

        if get_parvo is True and get_magno is True:
            parvo_frames.append(out_frames[0])
            magno_frames.append(out_frames[1])
        elif get_parvo is True and get_magno is False:
            parvo_frames.append(out_frames)
        elif get_parvo is False and get_magno is True:
            magno_frames.append(out_frames)

    if get_parvo is True and get_magno is True:
        return parvo_frames, magno_frames
    elif get_parvo is True and get_magno is False:
        return parvo_frames
    elif get_parvo is False and get_magno is True:
        return magno_frames


def create_para_dict(color_mode,
                     normalise_output_parvo,
                     photoreceptors_local_adaptation_sensitivity,
                     photoreceptors_temporal_constant,
                     photoreceptors_spatial_constant,
                     horizontal_cells_gain,
                     hcells_temporal_constant,
                     hcells_spatial_constant,
                     ganglion_cells_sensitivity,
                     normalise_output_magno,
                     parasol_cells_beta,
                     parasol_cells_tau,
                     parasol_cells_k,
                     amacrin_cells_temporal_cut_frequency,
                     v0_compression_parameter,
                     local_adapt_integration_tau,
                     local_adapt_integration_k):
    """Create parameters dictionary.

    Parameters
    ----------
    color_mode : bool
        specifies if (True) color is processed of not (False) to then
        processing gray level image
    normalise_output_parvo : bool
        specifies if (True) output is rescaled between 0 and 255 of
        not (False)
    photoreceptors_local_adaptation_sensitivity : float
        the photoreceptors sensitivity renage is 0-1 (more log compression
        effect when value increases)
    photoreceptors_temporal_constant : float
        the time constant of the first order low pass filter of
        the photoreceptors, use it to cut high temporal
        frequencies (noise or fast motion), unit is frames,
        typical value is 1 frame
    photoreceptors_spatial_constant : float
        the spatial constant of the first order low pass filter of
        the photoreceptors, use it to cut high spatial frequencies
        (noise or thick contours), unit is pixels, typical value is 1 pixel
    horizontal_cells_gain : float
        gain of the horizontal cells network, if 0, then the mean value of
        the output is zero, if the parameter is near 1, then,
        the luminance is not filtered and is still reachable at the output,
        typicall value is 0
    hcells_temporal_constant : float
        the time constant of the first order low pass filter of the
        horizontal cells, use it to cut low temporal
        frequencies (local luminance variations), unit is frames,
        typical value is 1 frame, as the photoreceptors
    hcells_spatial_constant : float
        the spatial constant of the first order low pass filter of
        the horizontal cells, use it to cut low spatial frequencies
        (local luminance), unit is pixels, typical value is 5 pixel,
        this value is also used for local contrast computing when computing
        the local contrast adaptation at the ganglion cells level
        (Inner Plexiform Layer parvocellular channel model)
    ganglion_cells_sensitivity : float
        the compression strengh of the ganglion cells local adaptation output,
        set a value between 0.6 and 1 for best results, a high value
        increases more the low value sensitivity... and the output saturates
        faster, recommended value: 0.7
    normalise_output_magno : bool
        specifies if (true) output is rescaled between 0 and 255 of not (false)
    parasol_cells_beta : float
        the low pass filter gain used for local contrast adaptation at
        the IPL level of the retina (for ganglion cells local adaptation),
        typical value is 0
    parasol_cells_tau : float
        the low pass filter time constant used for local contrast adaptation
        at the IPL level of the retina (for ganglion cells local adaptation),
        unit is frame, typical value is 0 (immediate response)
    parasol_cells_k : float
        the low pass filter spatial constant used for local contrast
        adaptation at the IPL level of the retina (for ganglion cells
        local adaptation), unit is pixels, typical value is 5
    amacrin_cells_temporal_cut_frequency : float
        the time constant of the first order high pass fiter of
        the magnocellular way (motion information channel), unit is
        frames, typical value is 1.2
    v0_compression_parameter : float
        the compression strengh of the ganglion cells local adaptation output,
        set a value between 0.6 and 1 for best results, a high value increases
        more the low value sensitivity... and the output saturates faster,
        recommended value: 0.95
    local_adapt_integration_tau : float
        specifies the temporal constant of the low pas filter involved in
        the computation of the local "motion mean" for the local adaptation
        computation
    local_adapt_integration_k : float
        specifies the spatial constant of the low pas filter involved in
        the computation of the local "motion mean" for the local adaptation
        computation

    Returns
    -------
    para_dict : dictionary
        A paramter dictionary
    """
    para_dict = {}
    para_dict["color_mode"] = color_mode
    para_dict["normalise_output_parvo"] = normalise_output_parvo
    para_dict["photoreceptors_local_adaptation_sensitivity"] = \
        photoreceptors_local_adaptation_sensitivity
    para_dict["photoreceptors_temporal_constant"] = \
        photoreceptors_temporal_constant
    para_dict["photoreceptors_spatial_constant"] = \
        photoreceptors_spatial_constant
    para_dict["horizontal_cells_gain"] = \
        horizontal_cells_gain
    para_dict["hcells_temporal_constant"] = hcells_temporal_constant
    para_dict["hcells_spatial_constant"] = hcells_spatial_constant
    para_dict["ganglion_cells_sensitivity"] = ganglion_cells_sensitivity
    para_dict["normalise_output_magno"] = normalise_output_magno
    para_dict["parasol_cells_beta"] = parasol_cells_beta
    para_dict["parasol_cells_tau"] = parasol_cells_tau
    para_dict["parasol_cells_k"] = parasol_cells_k
    para_dict["amacrin_cells_temporal_cut_frequency"] = \
        amacrin_cells_temporal_cut_frequency
    para_dict["v0_compression_parameter"] = v0_compression_parameter
    para_dict["local_adapt_integration_tau"] = local_adapt_integration_tau
    para_dict["local_adapt_integration_k"] = local_adapt_integration_k

    return para_dict


def compare_para_dict(para_dict_old, para_dict_new):
    """Compare two parameter dictionaries.

    Parameters
    ----------
    para_dict_old : dictionary
        old parameter dictionary
    para_dict_new : dictionary
        new parameter dictionary

    Returns
    -------
    status : bool
        True if same, False if different
    """
    shared_item = set(para_dict_old.items()) & set(para_dict_new.items())

    if len(shared_item) == len(para_dict_old):
        return True
    else:
        return False


def apply_para_dict(retina, para_dict):
    """Applay parameter dictionary on a given retina model.

    Parameters
    ----------
    retina : cv2.bioinspired_Retina
        the retina model
    para_dict : dictionary
        a given retina dicionary

    Returns
    -------
    retina : cv2.bioinspired_Retina
        An updated retina model
    """
    retina.setupIPLMagnoChannel(
        para_dict["normalise_output_magno"],
        para_dict["parasol_cells_beta"],
        para_dict["parasol_cells_tau"],
        para_dict["parasol_cells_k"],
        para_dict["amacrin_cells_temporal_cut_frequency"],
        para_dict["v0_compression_parameter"],
        para_dict["local_adapt_integration_tau"],
        para_dict["local_adapt_integration_k"])

    retina.setupOPLandIPLParvoChannel(
        para_dict["color_mode"],
        para_dict["normalise_output_parvo"],
        para_dict["photoreceptors_local_adaptation_sensitivity"],
        para_dict["photoreceptors_temporal_constant"],
        para_dict["photoreceptors_spatial_constant"],
        para_dict["horizontal_cells_gain"],
        para_dict["hcells_temporal_constant"],
        para_dict["hcells_spatial_constant"],
        para_dict["ganglion_cells_sensitivity"])
