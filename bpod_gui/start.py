import sys

from PySide6 import QtWidgets
from .ui.launcher import Launcher

def launch_gui():
    app = QtWidgets.QApplication(sys.argv)

    launcher = Launcher()
    launcher.show()

    app.exec()
