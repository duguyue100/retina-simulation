"""A Retina Viewer powered by OpenCV GUI utilities.

Author: Yuhuang Hu
Email : yuhuang.hu@uzh.ch
"""

from pyqtgraph.Qt import QtGui, QtCore
from pyqtgraph.widgets.RawImageWidget import RawImageWidget
from pyqtgraph.widgets.FileDialog import FileDialog
from pyqtgraph.widgets.ComboBox import ComboBox

from simretina import dataset, gui

# global parameters
win_width = 1280
win_height = 800

frame_wid = 400
frame_height = 300

# example image

lenna, size = dataset.get_lenna()
lenna = gui.cv2pg(lenna, frame_height, frame_wid)

# init viewer application
viewer_app = QtGui.QApplication([])

# define window and set layout
viewer_window = QtGui.QWidget()
viewer_window.setWindowTitle("Retina Simulation")
viewer_window.setFixedSize(win_width, win_height)
viewer_layout = QtGui.QGridLayout()
viewer_window.setLayout(viewer_layout)

# define widgets

# file dialog
file_chooser = FileDialog()

# Frame widgets
frame_wg = QtGui.QWidget()
frame_layout = QtGui.QHBoxLayout()
frame_wg.setLayout(frame_layout)
draw_frame = RawImageWidget()
draw_frame.setImage(lenna)
draw_parvo = RawImageWidget()
draw_parvo.setImage(lenna)
draw_magno = RawImageWidget()
draw_magno.setImage(lenna)

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
# TODO: figure out  why the list is not displayed completely
cm_label = QtGui.QLabel("Color Mode:")
cm_wg = ComboBox(items=["Color", "Gray"], default="Color")
cm_wg.setFixedSize(150, 30)

# PARVO normalize output
p_no_layout = QtGui.QHBoxLayout()
p_no_label = QtGui.QLabel("Norm. PARVO Out:")
p_no_yes = QtGui.QRadioButton("Yes")
p_no_yes.setChecked(True)
p_no_yes.toggled.connect(lambda: gui.p_no_state(pl_no_yes))
p_no_no = QtGui.QRadioButton("No")
p_no_no.setChecked(False)
p_no_yes.toggled.connect(lambda: gui.p_no_state(p_no_no))
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
m_no_yes.toggled.connect(lambda: gui.m_no_state(m_no_yes))
m_no_no = QtGui.QRadioButton("No")
m_no_no.setChecked(False)
m_no_yes.toggled.connect(lambda: gui.m_no_state(m_no_no))
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
    p_gcs_value.setText(str(m_vcp_wg.value()/100.))
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

# set layout
viewer_layout.addWidget(frame_wg, 0, 0, 2, 0)
viewer_layout.addWidget(PARVO_wg, 1, 0)
viewer_layout.addWidget(MAGNO_wg, 1, 1)

# Execute the viewer
viewer_window.show()
viewer_app.exec_()
