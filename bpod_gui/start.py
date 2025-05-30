import sys

from PySide6 import QtWidgets
from .base_ui.launcher import Launcher

def launch_gui():
    app = QtWidgets.QApplication(sys.argv)

    launcher = Launcher()
    launcher.show()

    app.exec()
