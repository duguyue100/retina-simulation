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
viewer_window.resize(win_width, win_height)
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
# TODO: fix the variable names!!!
IPL_wg = QtGui.QWidget()
IPL_layout = QtGui.QFormLayout()
IPL_wg.setLayout(IPL_layout)

# IPL color mode
# TODO: figure out  why the list is not displayed completely
cm_label = QtGui.QLabel("Color Mode:")
cm_wg = ComboBox(items=["Color", "Gray"], default="Color")

# IPL normalize output
ipl_no_layout = QtGui.QHBoxLayout()
ipl_no_label = QtGui.QLabel("Norm. IPL Out:")
ipl_no_yes = QtGui.QRadioButton("Yes")
ipl_no_yes.setChecked(True)
ipl_no_yes.toggled.connect(lambda: gui.ipl_no_state(ipl_no_yes))
ipl_no_no = QtGui.QRadioButton("No")
ipl_no_no.setChecked(False)
ipl_no_yes.toggled.connect(lambda: gui.ipl_no_state(ipl_no_no))
ipl_no_layout.addWidget(ipl_no_yes)
ipl_no_layout.addWidget(ipl_no_no)
ipl_no_layout.addStretch()

# IPL Photoreceptors Local Adaptation Sensititivity
ipl_plas_label = "PR Local Adapt. Sens.:"
ipl_plas_layout = QtGui.QHBoxLayout()
ipl_plas_wg = QtGui.QSlider(QtCore.Qt.Horizontal)
ipl_plas_wg.setMinimum(0)
ipl_plas_wg.setMaximum(100)
ipl_plas_wg.setTickPosition(QtGui.QSlider.TicksBelow)
ipl_plas_wg.setValue(75)
ipl_plas_wg.setTickInterval(5)
ipl_plas_value = QtGui.QLabel(str(ipl_plas_wg.value()/100.))
ipl_plas_layout.addWidget(ipl_plas_wg)
ipl_plas_layout.addWidget(ipl_plas_value)


def ipl_plas_value_change():
    """display value change."""
    global ipl_plas_wg, ipl_plas_value
    ipl_plas_value.setText(str(ipl_plas_wg.value()/100.))
ipl_plas_wg.valueChanged.connect(ipl_plas_value_change)

# IPL layout
IPL_layout.addRow(cm_label, cm_wg)
IPL_layout.addRow(ipl_no_label, ipl_no_layout)
IPL_layout.addRow(ipl_plas_label, ipl_plas_layout)

# IPL Magno Channel Parameters Widget
OPL_wg = QtGui.QWidget()
OPL_layout = QtGui.QFormLayout()
OPL_wg.setLayout(OPL_layout)

# OPL normalize output
opl_no_layout = QtGui.QHBoxLayout()
opl_no_label = QtGui.QLabel("Norm. OPL Out:")
opl_no_yes = QtGui.QRadioButton("Yes")
opl_no_yes.setChecked(True)
opl_no_yes.toggled.connect(lambda: gui.opl_no_state(opl_no_yes))
opl_no_no = QtGui.QRadioButton("No")
opl_no_no.setChecked(False)
opl_no_yes.toggled.connect(lambda: gui.opl_no_state(opl_no_no))
opl_no_layout.addWidget(opl_no_yes)
opl_no_layout.addWidget(opl_no_no)
opl_no_layout.addStretch()

# IPL layout
OPL_layout.addRow(opl_no_label, opl_no_layout)

# set layout
viewer_layout.addWidget(frame_wg, 0, 0, 2, 0)
viewer_layout.addWidget(IPL_wg, 1, 0)
viewer_layout.addWidget(OPL_wg, 1, 1)

# Execute the viewer
viewer_window.show()
viewer_app.exec_()
