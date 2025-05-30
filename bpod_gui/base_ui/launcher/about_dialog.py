from PySide6.QtWidgets import QDialog, QHBoxLayout, QLabel, QVBoxLayout, QPushButton


class About(QDialog):
    """
    Extension of QDialog to serve as a simple about menu
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle('About Bpod GUI')
        self.layout = QVBoxLayout()

        text = QLabel("I'm Mr. Meeseeks! Look at meeeeeee!")
        self.layout.addWidget(text)

        okay_button = QPushButton()
        okay_button.setText('Okay!')
        okay_button.clicked.connect(self.close)
        self.layout.addWidget(okay_button)

        self.setLayout(self.layout)
