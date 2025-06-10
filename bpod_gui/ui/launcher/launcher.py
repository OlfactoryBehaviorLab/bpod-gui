import sys

from PySide6.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget, QSizePolicy, QMenuBar
from PySide6.QtCore import QSize

from .about_dialog import About

class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bpod Launcher")
        self.setFixedSize(QSize(400, 200))

        self.main_layout = QGridLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.main_layout)
        self.protocol_button = QPushButton()
        self.manual_control_button = QPushButton()
        self.configure_button = QPushButton()
        self.protocol_button.setText('Launch Protocol!')
        self.manual_control_button.setText('Manual Control')
        self.configure_button.setText('Configuration')
        self.protocol_button.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.manual_control_button.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.configure_button.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        self.manual_control_button.setMinimumSize(QSize(60, 60))
        self.configure_button.setMinimumSize(QSize(60, 60))
        self.main_layout.addWidget(self.protocol_button, 0, 0, 1, -1)
        # Top Left grid and span the first row and both columns
        self.main_layout.addWidget(self.manual_control_button, 1, 0)
        self.main_layout.addWidget(self.configure_button, 1, 1)

        self.about_dialog = About(self)

        menubar = QMenuBar()
        file_menu = menubar.addMenu(u'&File')
        exit_action = file_menu.addAction(u'&Exit')
        exit_action.triggered.connect(sys.exit)  # We may have cleanup to do here later

        about_menu = menubar.addAction(u'&About')
        about_menu.triggered.connect(self.about_dialog.open)  # Launch about dialog
        self.setMenuBar(menubar)

    def __dummy__(self):
        pass