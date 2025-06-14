import sys

from qtpy import QtWidgets
from .ui.console import ManualControl

def launch_gui():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    mc = ManualControl()

    with open('bpod_gui/qss/manual_control_interface.qss') as f:
        style = f.read()
        mc.setStyleSheet(style)

    # launcher = Launcher()
    # launcher.show()
    mc.show()
    app.exec()
