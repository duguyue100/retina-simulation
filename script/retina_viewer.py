#!/usr/bin/env python
"""A Retina Viewer powered by OpenCV GUI utilities.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

import cv2
from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.widgets.RawImageWidget import RawImageWidget
from pyqtgraph.widgets.FileDialog import FileDialog
from pyqtgraph.widgets.ComboBox import ComboBox

from simretina import dataset, gui, retina

# global parameters
win_width = 1280
win_height = 800

frame_wid = 400
frame_height = 300

# background image
bg_frame = gui.get_background_frame((frame_wid, frame_height))
bg_frame = bg_frame.astype("uint8")
frame = bg_frame.copy()
frames = []

# init viewer application
viewer_app = QtGui.QApplication([])

# define window and set layout
viewer_window = QtGui.QWidget()
viewer_window.setWindowTitle("Retina Simulation")
viewer_window.setFixedSize(win_width, win_height)
viewer_layout = QtGui.QGridLayout()
viewer_window.setLayout(viewer_layout)

# Frame widgets
frame_wg = QtGui.QWidget()
frame_layout = QtGui.QHBoxLayout()
frame_wg.setLayout(frame_layout)
draw_frame = RawImageWidget()
draw_frame.setImage(bg_frame)
draw_parvo = RawImageWidget()
draw_parvo.setImage(bg_frame)
draw_magno = RawImageWidget()
draw_magno.setImage(bg_frame)

frame_layout.addWidget(draw_frame)
frame_layout.addWidget(draw_parvo)
frame_layout.addWidget(draw_magno)

# IPL and OPL Parvo Parameters Widget
PARVO_wg = QtGui.QWidget()
PARVO_layout = QtGui.QFormLayout()
PARVO_layout.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
PARVO_layout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
PARVO_layout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
PARVO_layout.setLabelAlignment(QtCore.Qt.AlignLeft)
PARVO_wg.setLayout(PARVO_layout)

# PARVO color mode
cm_label = QtGui.QLabel("Color Mode:")
cm_wg = ComboBox(items=["Color", "Gray"], default="Color")
cm_wg.setFixedSize(150, 30)

# PARVO normalize output
p_no_layout = QtGui.QHBoxLayout()
p_no_label = QtGui.QLabel("Norm. PARVO Out:")
p_no_yes = QtGui.QRadioButton("Yes")
p_no_yes.setChecked(True)
p_no_no = QtGui.QRadioButton("No")
p_no_no.setChecked(False)
p_no_layout.addWidget(p_no_yes)
p_no_layout.addWidget(p_no_no)
p_no_layout.addStretch()

# Photoreceptors Local Adaptation Sensititivity
p_plas_label = "PR Local Adapt. Sens.:"
p_plas_layout = QtGui.QHBoxLayout()
p_plas_wg = QtGui.QSlider(QtCore.Qt.Horizontal)
p_plas_wg.setFixedSize(150, 30)
p_plas_wg.setMinimum(0)
p_plas_wg.setMaximum(100)
p_plas_wg.setTickPosition(QtGui.QSlider.TicksBelow)
p_plas_wg.setValue(75)
p_plas_wg.setTickInterval(1)
p_plas_value = QtGui.QLabel(str(p_plas_wg.value()/100.))
p_plas_layout.addWidget(p_plas_wg)
p_plas_layout.addWidget(p_plas_value)


def p_plas_value_change():
    """display value change."""
    global p_plas_wg, p_plas_value
    p_plas_value.setText(str(p_plas_wg.value()/100.))
p_plas_wg.valueChanged.connect(p_plas_value_change)

# Photoreceptors Temporal Constant
p_ptc_label = "PR Temp Constant:"
p_ptc_layout = QtGui.QHBoxLayout()
p_ptc_wg = QtGui.QLineEdit()
p_ptc_wg.setText("0.9")
p_ptc_unit = QtGui.QLabel("frames")
p_ptc_layout.addWidget(p_ptc_wg)
p_ptc_layout.addWidget(p_ptc_unit)

# Photoreceptors Spatial Constant
p_psc_label = "PR Spatial Constant:"
p_psc_layout = QtGui.QHBoxLayout()
p_psc_wg = QtGui.QLineEdit()
p_psc_wg.setText("0.53")
p_psc_unit = QtGui.QLabel("pixels")
p_psc_layout.addWidget(p_psc_wg)
p_psc_layout.addWidget(p_psc_unit)

# Horizontal Cells Gain
p_hcg_label = "Hor Cells Gagin:"
p_hcg_layout = QtGui.QHBoxLayout()
p_hcg_wg = QtGui.QSlider(QtCore.Qt.Horizontal)
p_hcg_wg.setFixedSize(150, 30)
p_hcg_wg.setMinimum(0)
p_hcg_wg.setMaximum(100)
p_hcg_wg.setTickPosition(QtGui.QSlider.TicksBelow)
p_hcg_wg.setValue(0)
p_hcg_wg.setTickInterval(1)
p_hcg_value = QtGui.QLabel(str(p_hcg_wg.value()/100.))
p_hcg_layout.addWidget(p_hcg_wg)
p_hcg_layout.addWidget(p_hcg_value)


def p_hcg_value_change():
    """display value change."""
    global p_hcg_wg, p_hcg_value
    p_hcg_value.setText(str(p_hcg_wg.value()/100.))
p_hcg_wg.valueChanged.connect(p_hcg_value_change)

# Hcells Temporal Constant
p_htc_label = "Hcells Temporal Constant:"
p_htc_layout = QtGui.QHBoxLayout()
p_htc_wg = QtGui.QLineEdit()
p_htc_wg.setText("0.5")
p_htc_unit = QtGui.QLabel("frames")
p_htc_layout.addWidget(p_htc_wg)
p_htc_layout.addWidget(p_htc_unit)

# Hcells Spatial Constant
p_hsc_label = "Hcells Spatial Constant:"
p_hsc_layout = QtGui.QHBoxLayout()
p_hsc_wg = QtGui.QLineEdit()
p_hsc_wg.setText("7")
p_hsc_unit = QtGui.QLabel("pixels")
p_hsc_layout.addWidget(p_hsc_wg)
p_hsc_layout.addWidget(p_hsc_unit)

# Ganglion Cells Sensitivity
p_gcs_label = "Gang. Cells Sens.:"
p_gcs_layout = QtGui.QHBoxLayout()
p_gcs_wg = QtGui.QSlider(QtCore.Qt.Horizontal)
p_gcs_wg.setFixedSize(150, 30)
p_gcs_wg.setMinimum(60)
p_gcs_wg.setMaximum(100)
p_gcs_wg.setTickPosition(QtGui.QSlider.TicksBelow)
p_gcs_wg.setValue(75)
p_gcs_wg.setTickInterval(1)
p_gcs_value = QtGui.QLabel(str(p_gcs_wg.value()/100.))
p_gcs_layout.addWidget(p_gcs_wg)
p_gcs_layout.addWidget(p_gcs_value)


def p_gcs_value_change():
    """display value change."""
    global p_gcs_wg, p_gcs_value
    p_gcs_value.setText(str(p_gcs_wg.value()/100.))
p_gcs_wg.valueChanged.connect(p_gcs_value_change)

# IPL and OPL Parvo layout
PARVO_layout.addRow(cm_label, cm_wg)
PARVO_layout.addRow(p_no_label, p_no_layout)
PARVO_layout.addRow(p_plas_label, p_plas_layout)
PARVO_layout.addRow(p_ptc_label, p_ptc_layout)
PARVO_layout.addRow(p_psc_label, p_psc_layout)
PARVO_layout.addRow(p_hcg_label, p_hcg_layout)
PARVO_layout.addRow(p_htc_label, p_htc_layout)
PARVO_layout.addRow(p_hsc_label, p_hsc_layout)
PARVO_layout.addRow(p_gcs_label, p_gcs_layout)

# IPL Magno Channel Parameters Widget
MAGNO_wg = QtGui.QWidget()
MAGNO_layout = QtGui.QFormLayout()
MAGNO_layout.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
MAGNO_layout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
MAGNO_layout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
MAGNO_layout.setLabelAlignment(QtCore.Qt.AlignLeft)
MAGNO_wg.setLayout(MAGNO_layout)

# IPL Magno normalize output
m_no_layout = QtGui.QHBoxLayout()
m_no_label = QtGui.QLabel("Norm. OPL Out:")
m_no_yes = QtGui.QRadioButton("Yes")
m_no_yes.setChecked(True)
m_no_no = QtGui.QRadioButton("No")
m_no_no.setChecked(False)
m_no_layout.addWidget(m_no_yes)
m_no_layout.addWidget(m_no_no)
m_no_layout.addStretch()

# Parasol Cells Beta
m_pcb_label = "Parasol Cells Beta:"
m_pcb_wg = QtGui.QLineEdit()
m_pcb_wg.setText("0")

# Parasol Cells Tau
m_pct_label = "Parasol Cells Tau:"
m_pct_layout = QtGui.QHBoxLayout()
m_pct_wg = QtGui.QLineEdit()
m_pct_wg.setText("0")
m_pct_unit = QtGui.QLabel("frames")
m_pct_layout.addWidget(m_pct_wg)
m_pct_layout.addWidget(m_pct_unit)

# Parasol Cells K
m_pck_label = "Parasol Cells K:"
m_pck_layout = QtGui.QHBoxLayout()
m_pck_wg = QtGui.QLineEdit()
m_pck_wg.setText("7")
m_pck_unit = QtGui.QLabel("pixels")
m_pck_layout.addWidget(m_pck_wg)
m_pck_layout.addWidget(m_pck_unit)

# Amacrin Cells Temporal Cut Frequency
m_actcf_label = "Amacrin Cells Temp Cut Freq.:"
m_actcf_layout = QtGui.QHBoxLayout()
m_actcf_wg = QtGui.QLineEdit()
m_actcf_wg.setText("2")
m_actcf_unit = QtGui.QLabel("frames")
m_actcf_layout.addWidget(m_actcf_wg)
m_actcf_layout.addWidget(m_actcf_unit)

# V0 Compression Parameter
m_vcp_label = "V0 Compression Para.:"
m_vcp_layout = QtGui.QHBoxLayout()
m_vcp_wg = QtGui.QSlider(QtCore.Qt.Horizontal)
m_vcp_wg.setFixedSize(150, 30)
m_vcp_wg.setMinimum(60)
m_vcp_wg.setMaximum(100)
m_vcp_wg.setTickPosition(QtGui.QSlider.TicksBelow)
m_vcp_wg.setValue(95)
m_vcp_wg.setTickInterval(1)
m_vcp_value = QtGui.QLabel(str(m_vcp_wg.value()/100.))
m_vcp_layout.addWidget(m_vcp_wg)
m_vcp_layout.addWidget(m_vcp_value)


def m_vcp_value_change():
    """display value change."""
    global m_vcp_wg, m_vcp_value
    m_vcp_value.setText(str(m_vcp_wg.value()/100.))
m_vcp_wg.valueChanged.connect(m_vcp_value_change)

# Local Adapt Integration Tau
m_lait_label = "Local Adapt Integ. Tau:"
m_lait_wg = QtGui.QLineEdit()
m_lait_wg.setText("0")

# Local Adapt Integration K
m_laik_label = "Local Adapt Integ. K:"
m_laik_wg = QtGui.QLineEdit()
m_laik_wg.setText("7")

# IPL Magno layout
MAGNO_layout.addRow(m_no_label, m_no_layout)
MAGNO_layout.addRow(m_pcb_label, m_pcb_wg)
MAGNO_layout.addRow(m_pct_label, m_pct_layout)
MAGNO_layout.addRow(m_pck_label, m_pck_layout)
MAGNO_layout.addRow(m_actcf_label, m_actcf_layout)
MAGNO_layout.addRow(m_vcp_label, m_vcp_layout)
MAGNO_layout.addRow(m_lait_label, m_lait_wg)
MAGNO_layout.addRow(m_laik_label, m_laik_wg)

# Utility widgets
UTIL_wg = QtGui.QWidget()
UTIL_layout = QtGui.QFormLayout()
UTIL_layout.setRowWrapPolicy(QtGui.QFormLayout.DontWrapRows)
UTIL_layout.setFieldGrowthPolicy(QtGui.QFormLayout.FieldsStayAtSizeHint)
UTIL_layout.setFormAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
UTIL_layout.setLabelAlignment(QtCore.Qt.AlignLeft)
UTIL_wg.setLayout(UTIL_layout)

# Display mode: image, video, webcam, external image, external video
dis_label = QtGui.QLabel("Operation Mode:")
dis_wg = ComboBox(items=["Image", "Image (External)", "Video",
                         "Video (External)", "Webcam"], default="Image")
dis_wg.setFixedSize(200, 30)

# Default example: lenna, dog, horse riding, taichi

exp_label = QtGui.QLabel("Builtin Examples:")
exp_wg = ComboBox(items=["None", "Lenna (Image)", "Dog (Image)",
                         "Horse Riding (Video)", "TaiChi (Video)"],
                  default="None")
exp_wg.setFixedSize(200, 30)
exp_wg_prev = exp_wg.currentText()

# Exit button
exit_wg = QtGui.QPushButton("Exit")
exit_wg.setFixedSize(200, 30)
exit_wg.setCheckable(True)
exit_wg.clicked.connect(lambda: gui.exit_wg_state(exit_wg, viewer_app))

# File chooser
file_button = QtGui.QPushButton("Open Image/Video")
file_button.setFixedSize(200, 30)
file_button.setCheckable(True)
file_chooser = FileDialog()
file_chooser.setFileMode(QtGui.QFileDialog.ExistingFile)
file_chooser.selectNameFilter("Image files (*.jpg *.jpeg *.png *.tiff)")
file_name = ""
file_name_prev = ""


def select_file():
    """select file."""
    global file_name
    file_name = file_chooser.getOpenFileName()
file_button.clicked.connect(select_file)

# Utitlity Layout
UTIL_layout.addRow(dis_label, dis_wg)
UTIL_layout.addRow(exp_label, exp_wg)
UTIL_layout.addRow(file_button, exit_wg)

# set layout
manual_wg = QtGui.QWidget()
manual_layout = QtGui.QHBoxLayout()
manual_wg.setLayout(manual_layout)
manual_layout.addWidget(UTIL_wg)
manual_layout.addWidget(PARVO_wg)
manual_layout.addWidget(MAGNO_wg)

viewer_layout.addWidget(frame_wg, 0, 0)
viewer_layout.addWidget(manual_wg, 1, 0)

# setup retina
eye = retina.init_retina(bg_frame.shape[:2])

# get parameter collection
cm_state = gui.color_mode_option(cm_wg)
p_no_state = gui.no_state(p_no_yes, p_no_no)
p_plas_wg_val = p_plas_wg.value()/100.
p_ptc_wg_val = gui.line_edit_val(p_ptc_wg, 0.9)
p_psc_wg_val = gui.line_edit_val(p_psc_wg, 0.53)
p_hcg_wg_val = p_hcg_wg.value()/100.
p_htc_wg_val = gui.line_edit_val(p_htc_wg, 0.5)
p_hsc_wg_val = gui.line_edit_val(p_hsc_wg, 7.)
p_gcs_wg_val = p_gcs_wg.value()/100.

m_no_state = gui.no_state(m_no_yes, m_no_no)
m_pcb_wg_val = gui.line_edit_val(m_pcb_wg, 0.)
m_pct_wg_val = gui.line_edit_val(m_pct_wg, 0.)
m_pck_wg_val = gui.line_edit_val(m_pck_wg, 7.)
m_actcf_wg_val = gui.line_edit_val(m_actcf_wg, 2.)
m_vcp_wg_val = m_vcp_wg.value()/100.
m_lait_wg_val = gui.line_edit_val(m_lait_wg, 0.)
m_laik_wg_val = gui.line_edit_val(m_laik_wg, 7.)

eye_para_dict = retina.create_para_dict(
                    color_mode=cm_state,
                    normalise_output_parvo=p_no_state,
                    photoreceptors_local_adaptation_sensitivity=p_plas_wg_val,
                    photoreceptors_temporal_constant=p_ptc_wg_val,
                    photoreceptors_spatial_constant=p_psc_wg_val,
                    horizontal_cells_gain=p_hcg_wg_val,
                    hcells_temporal_constant=p_htc_wg_val,
                    hcells_spatial_constant=p_hsc_wg_val,
                    ganglion_cells_sensitivity=p_gcs_wg_val,
                    normalise_output_magno=m_no_state,
                    parasol_cells_beta=m_pcb_wg_val,
                    parasol_cells_tau=m_pct_wg_val,
                    parasol_cells_k=m_pck_wg_val,
                    amacrin_cells_temporal_cut_frequency=m_actcf_wg_val,
                    v0_compression_parameter=m_vcp_wg_val,
                    local_adapt_integration_tau=m_lait_wg_val,
                    local_adapt_integration_k=m_laik_wg_val)

eye_para_dict_old = eye_para_dict
retina.apply_para_dict(eye, eye_para_dict)
retina.clear_buffers(eye)

frame_idx = 0
frame_len = 0
vid_stream = None


def update():
    """Update viewer status."""
    global eye_para_dict_old, eye_para_dict, file_name, \
        exp_wg_prev, file_name_prev, eye, frame, frames, \
        frame_idx, frame_len, vid_stream
    # capture current states
    cm_state = gui.color_mode_option(cm_wg)
    p_no_state = gui.no_state(p_no_yes, p_no_no)
    p_plas_wg_val = p_plas_wg.value()/100.
    p_ptc_wg_val = gui.line_edit_val(p_ptc_wg, 0.9)
    p_psc_wg_val = gui.line_edit_val(p_psc_wg, 0.53)
    p_hcg_wg_val = p_hcg_wg.value()/100.
    p_htc_wg_val = gui.line_edit_val(p_htc_wg, 0.5)
    p_hsc_wg_val = gui.line_edit_val(p_hsc_wg, 7.)
    p_gcs_wg_val = p_gcs_wg.value()/100.

    m_no_state = gui.no_state(m_no_yes, m_no_no)
    m_pcb_wg_val = gui.line_edit_val(m_pcb_wg, 0.)
    m_pct_wg_val = gui.line_edit_val(m_pct_wg, 0.)
    m_pck_wg_val = gui.line_edit_val(m_pck_wg, 7.)
    m_actcf_wg_val = gui.line_edit_val(m_actcf_wg, 2.)
    m_vcp_wg_val = m_vcp_wg.value()/100.
    m_lait_wg_val = gui.line_edit_val(m_lait_wg, 0.)
    m_laik_wg_val = gui.line_edit_val(m_laik_wg, 7.)

    # setup current paramete dictionary
    eye_para_dict = retina.create_para_dict(
                     color_mode=cm_state,
                     normalise_output_parvo=p_no_state,
                     photoreceptors_local_adaptation_sensitivity=p_plas_wg_val,
                     photoreceptors_temporal_constant=p_ptc_wg_val,
                     photoreceptors_spatial_constant=p_psc_wg_val,
                     horizontal_cells_gain=p_hcg_wg_val,
                     hcells_temporal_constant=p_htc_wg_val,
                     hcells_spatial_constant=p_hsc_wg_val,
                     ganglion_cells_sensitivity=p_gcs_wg_val,
                     normalise_output_magno=m_no_state,
                     parasol_cells_beta=m_pcb_wg_val,
                     parasol_cells_tau=m_pct_wg_val,
                     parasol_cells_k=m_pck_wg_val,
                     amacrin_cells_temporal_cut_frequency=m_actcf_wg_val,
                     v0_compression_parameter=m_vcp_wg_val,
                     local_adapt_integration_tau=m_lait_wg_val,
                     local_adapt_integration_k=m_laik_wg_val)

    if not retina.compare_para_dict(eye_para_dict_old, eye_para_dict):
        eye_para_dict_old = eye_para_dict
        retina.apply_para_dict(eye, eye_para_dict)
        retina.clear_buffers(eye)

    if dis_wg.currentText() == "Image":
        if vid_stream is not None:
            vid_stream.release()
            vid_stream = None
        exp_wg_curr = exp_wg.currentText()
        if exp_wg_curr != exp_wg_prev:
            # if example sequence is changed
            # then read new frame and set external frame as empty
            if exp_wg_curr != "None":
                # if current example is not empty
                if exp_wg_curr == "Lenna (Image)":
                    frame = dataset.get_lenna(size=False)
                elif exp_wg_curr == "Dog (Image)":
                    frame = dataset.get_dog(size=False)

                frame = gui.resize(frame, (frame_wid, frame_height),
                                   ratio_keep=True)
                eye = retina.init_retina(frame.shape[:2])
                retina.apply_para_dict(eye, eye_para_dict)
                retina.clear_buffers(eye)
            exp_wg_prev = exp_wg_curr
        elif exp_wg_curr == exp_wg_prev:
            if exp_wg_curr in ["None", "Horse Riding (Video)",
                               "TaiChi (Video)"]:
                frame = bg_frame
    elif dis_wg.currentText() == "Video":
        if vid_stream is not None:
            vid_stream.release()
            vid_stream = None
        exp_wg_curr = exp_wg.currentText()
        if exp_wg_curr != exp_wg_prev:
            if exp_wg_curr == "Horse Riding (Video)":
                t_frames = dataset.get_horse_riding(size=False)
            elif exp_wg_curr == "TaiChi (Video)":
                t_frames = dataset.get_taichi(size=False)
            else:
                t_frames = [bg_frame]

            frames = []
            for frame in t_frames:
                frames.append(gui.resize(frame, (frame_wid, frame_height),
                                         ratio_keep=True))
            eye = retina.init_retina(frames[0].shape[:2])
            retina.apply_para_dict(eye, eye_para_dict)
            retina.clear_buffers(eye)
            frame = frames[0]
            frame_idx = 0
            frame_len = len(frames)
            exp_wg_prev = exp_wg_curr
        elif exp_wg_curr == exp_wg_prev:
            if exp_wg_curr in ["None", "Lenna (Image)", "Dog (Image)"]:
                frame = bg_frame
            else:
                frame = frames[frame_idx]
                frame_idx += 1
                if frame_idx == (frame_len-1):
                    frame_idx = 0
    elif dis_wg.currentText() == "Webcam":
        exp_wg.setCurrentIndex(0)
        if vid_stream is None:
            vid_stream = cv2.VideoCapture(0)
        _, frame = vid_stream.read()
        frame = gui.resize(frame, (frame_wid, frame_height),
                           ratio_keep=True)
        eye_size = eye.getInputSize()
        if eye_size[0] != frame.shape[1] or eye_size[1] != frame.shape[0]:
            eye = retina.init_retina(frame.shape[:2])
            retina.apply_para_dict(eye, eye_para_dict)
            retina.clear_buffers(eye)
    elif dis_wg.currentText() == "Image (External)":
        exp_wg.setCurrentIndex(0)
        if vid_stream is not None:
            vid_stream.release()
            vid_stream = None
        if file_name != file_name_prev:
            if file_name != "":
                if dataset.check_image_file(str(file_name)):
                    frame = cv2.imread(str(file_name))
                else:
                    frame = bg_frame
            elif file_name == "":
                frame = bg_frame

            frame = gui.resize(frame, (frame_wid, frame_height),
                               ratio_keep=True)
            eye = retina.init_retina(frame.shape[:2])
            retina.apply_para_dict(eye, eye_para_dict)
            retina.clear_buffers(eye)

            file_name_prev = file_name
        elif file_name == file_name_prev:
            if file_name == "":
                frame = bg_frame
    elif dis_wg.currentText() == "Video (External)":
        exp_wg.setCurrentIndex(0)
        if vid_stream is not None:
            vid_stream.release()
            vid_stream = None
        if file_name != file_name_prev:
            if file_name != "":
                if dataset.check_video_file(str(file_name)):
                    t_frames = dataset.get_video(str(file_name), size=False)
                else:
                    t_frames = [bg_frame]

            frames = []
            for frame in t_frames:
                frames.append(gui.resize(frame, (frame_wid, frame_height),
                                         ratio_keep=True))
            eye = retina.init_retina(frames[0].shape[:2])
            retina.apply_para_dict(eye, eye_para_dict)
            retina.clear_buffers(eye)
            frame = frames[0]
            frame_idx = 0
            frame_len = len(frames)
            file_name_prev = file_name
        elif file_name == file_name_prev:
            if file_name == "":
                frame = bg_frame
            else:
                frame = frames[frame_idx]
                frame_idx += 1
                if frame_idx == (frame_len-1):
                    frame_idx = 0

    color_frame = frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if cm_state is False:
        parvo_frame, magno_frame = retina.get_opl_frame(eye, gray_frame,
                                                        color_mode="gray")
        dis_frame = retina.gray2color(gray_frame)
    else:
        dis_frame = color_frame
        parvo_frame, magno_frame = retina.get_opl_frame(eye, dis_frame)

    origin_frame = gui.cv2pg(dis_frame, frame_height, frame_wid)
    parvo_frame = gui.cv2pg(parvo_frame, frame_height, frame_wid)
    magno_frame = gui.cv2pg(magno_frame, frame_height, frame_wid)
    draw_frame.setImage(origin_frame)
    draw_parvo.setImage(parvo_frame)
    draw_magno.setImage(magno_frame)
    viewer_app.processEvents()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)

# Execute the viewer
viewer_window.show()
viewer_app.exec_()
