from qtpy.QtCore import Qt
from qtpy.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout

class StateMachineWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setObjectName('state_machine_widget')
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.behavior_ports_label = QLabel()
        self.behavior_ports_label.setText('Behavior Ports')
        self.behavior_ports_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.behavior_ports_label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        self.behavior_ports_label.setProperty('type', 'smw_underlined_header')
        self.grid_layout.addWidget(self.behavior_ports_label, 0, 0, 1, 2)

        self.bnc_in_label = QLabel()
        self.bnc_in_label.setText('BNC In')
        self.bnc_in_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bnc_in_label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        self.bnc_in_label.setProperty('type', 'smw_underlined_header')
        self.grid_layout.addWidget(self.bnc_in_label, 0, 2, 1, 1)

        self.bnc_out_label = QLabel()
        self.bnc_out_label.setText('BNC Out')
        self.bnc_out_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bnc_out_label.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum)
        self.bnc_out_label.setProperty('type', 'smw_underlined_header')
        self.grid_layout.addWidget(self.bnc_out_label, 0, 3, 1, 1)
