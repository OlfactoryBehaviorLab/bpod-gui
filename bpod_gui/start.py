import sys

from qtpy import QtWidgets
from .ui.launcher import Launcher

def launch_gui():
    app = QtWidgets.QApplication(sys.argv)

    launcher = Launcher()
    launcher.show()

    app.exec()
