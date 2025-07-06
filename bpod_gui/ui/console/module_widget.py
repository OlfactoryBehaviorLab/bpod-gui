from qtpy.QtWidgets import (
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QSizePolicy,
    QTextEdit,
)


class ModuleWidget(QWidget):
    """
    ModuleWidget (inherits from QWidget): Class implements the serial command elements for
    manually controlling misc. Bpod modules
    """

    def __init__(self):
        super().__init__()

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.command_line = QLineEdit()
        self.command_line.setPlaceholderText("Enter a command and press send!")
        self.command_line.setObjectName("command_line")
        self.command_line.setMinimumHeight(30)
        self.command_line.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum
        )
        self.main_layout.addWidget(self.command_line, 0, 0, 1, 3)

        self.send_button = QPushButton()
        self.send_button.setObjectName("send_button")
        self.send_button.setText("Send")
        self.send_button.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        self.main_layout.addWidget(self.send_button, 0, 3, 1, 1)

        self.clear_button = QPushButton()
        self.clear_button.setObjectName("clear_button")
        self.clear_button.setText("Clear")
        self.clear_button.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        self.main_layout.addWidget(self.clear_button, 0, 4, 1, 1)

        self.module_output = QTextEdit()
        self.module_output.setObjectName("module_output")
        self.module_output.setReadOnly(True)
        self.module_output.setPlaceholderText(
            "Rawr, I'm a shark!\n      .            \n\\_____)\\_____\n/--v____ __`<   ><o>\n       )/       \n       '"
        )  # https://www.asciiart.eu/animals/fish
        self.main_layout.addWidget(self.module_output, 1, 0, -1, -1)
