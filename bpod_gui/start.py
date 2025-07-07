import sys
import logging
from qtpy import QtWidgets
from bpod_gui.ui.console import ManualControl

logging.basicConfig()
main_logger = logging.getLogger()
main_logger.setLevel(logging.NOTSET)
main_logger.debug("Logging Started!")

def launch_gui():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    mc = ManualControl(main_logger)
    with open("bpod_gui/qss/manual_control_interface.qss") as f:
        style = f.read()
        mc.setStyleSheet(style)

    # launcher = Launcher()
    # launcher.show()
    mc.show()
    app.exec()
