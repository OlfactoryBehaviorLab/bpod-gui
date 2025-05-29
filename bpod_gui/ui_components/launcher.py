from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QSize

class Launcher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bpod Launcher")
        self.setMinimumSize(QSize(400, 200))

