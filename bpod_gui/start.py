import sys
import logging
from pathlib import Path
from qtpy import QtWidgets
from bpod_gui.ui.console import ManualControl

from bpod_gui.ui.calibration import calibration_ui
logging.basicConfig()
main_logger = logging.getLogger()
main_logger.setLevel(logging.NOTSET)
main_logger.debug("Logging Started!")

def launch_gui():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    mc = ManualControl(main_logger)
    calibration_widget = calibration_ui.CalibrationUI()

    stylesheets = get_stylesheets(Path("bpod_gui/qss"))
    apply_stylesheet(app, stylesheets, "base")
    apply_stylesheet(mc, stylesheets, "manual_control_interface")

    # mc.show()
    calibration_widget.show()
    app.exec()

def get_stylesheets(style_sheet_dir: Path):
    stylesheets = {}

    if style_sheet_dir.exists():
        all_stylesheets_glob = style_sheet_dir.glob('*.qss')
        for stylesheet_path in all_stylesheets_glob:
            stylesheets[stylesheet_path.stem] = stylesheet_path
    else:
        raise FileExistsError(f"Style sheet dir {style_sheet_dir} does not exist!")

    return stylesheets


def apply_stylesheet(widget: QtWidgets.QWidget, stylesheets: dict[str, Path], to_apply: str):
    if to_apply in stylesheets:
        with open(stylesheets[to_apply]) as f:
            style = f.read()
            widget.setStyleSheet(style)
    else:
        main_logger.error("%s not found in stylesheets directory!", to_apply)
