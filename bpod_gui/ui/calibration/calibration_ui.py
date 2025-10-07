"""Calibration UI Module"""

import logging

from qtpy.QtCore import QSize, Qt
from qtpy.QtWidgets import (
    QDockWidget,
    QWidget,
    QGridLayout,
    QLabel,
    QSizePolicy,
    QFrame,
    QComboBox,
    QTableWidget,
    QHeaderView
)

logger = logging.getLogger(__name__)

class CalibrationUIContainer(QDockWidget):
    def __init__(self):
        super().__init__()
        self.calibration_widget = CalibrationUI()
        self.setWidget(self.calibration_widget)
        self.setFloating(True)


class CalibrationUI(QWidget):
    """CalibrationUI Widget: UI element to create and edit water solenoid calibrations"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Liquid Calibration")
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        self.setMinimumSize(QSize(400, 300))
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        ## == Header ==
        self.title = QLabel()
        self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.title.setText("Liquid Calibration Menu: ")
        self.title.setObjectName("calibration_ui_title")
        self.main_layout.addWidget(self.title, 0, 0, 1, 2)

        self.title_line = QFrame()
        self.title_line.setFrameShape(QFrame.Shape.HLine)
        self.title_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.title_line.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )
        self.title_line.setLineWidth(5)
        self.title_line.setMidLineWidth(5)
        self.title_line.setMinimumWidth(100)

        self.main_layout.addWidget(self.title_line, 0, 2, 1, -1)

        ## == Left Half ==
        self.valve_selection_label = QLabel()
        self.valve_selection_label.setText("Select Valve:")
        self.valve_selection_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self.valve_selector = QComboBox()
        for i in range(8):
            self.valve_selector.addItem(f"Valve {i+1}:")
        self.valve_selector.addItem("New Valve...")

        self.main_layout.addWidget(self.valve_selection_label, 1, 0, 1, 1)
        self.main_layout.addWidget(self.valve_selector, 1, 1, 1, -1)

        ## == Calibration Table ==
        self.calibration_table = QTableWidget(15, 2)
        self.calibration_table.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        self.calibration_table.setHorizontalHeaderLabels(
            [
                "Pulse Time (ms)",
                "Liquid Volume (uL)"
            ]
        )
        self.calibration_table.setVerticalHeaderLabels(
            [f"{i+1}." for i in range(15)]
        )
        v_header = self.calibration_table.verticalHeader()
        v_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        v_header.setStretchLastSection(False)
        h_header = self.calibration_table.horizontalHeader()
        h_header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        h_header.setStretchLastSection(True)

        self.main_layout.addWidget(self.calibration_table, 2, 0, -1, -1)

