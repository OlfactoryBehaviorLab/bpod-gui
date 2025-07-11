from qtpy import QtCore
from qtpy.QtWidgets import (
    QWidget,
    QFrame,
    QSizePolicy,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QScrollArea,
    QPushButton,
)

class CalibrationWidget(QWidget):
    """
    CalibrationWidget (inherits from QWidget): Interface to create, manage, and edit water solenoid calibration


    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Water Calibration")
        self.setObjectName("calibration_menu")
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

