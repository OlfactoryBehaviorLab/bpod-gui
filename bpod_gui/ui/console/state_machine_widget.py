from typing import Iterable

from PySide6.QtGui import QColor
from qtpy.QtCore import Qt
from qtpy.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout

from bpod_gui.ui.console.components.LED import LED


class StateMachineWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.num_ports: int = 8

        self.setObjectName("state_machine_widget")
        self.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.behavior_ports_label = QLabel()
        self.behavior_ports_label.setText("Behavior Ports")
        self.behavior_ports_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.behavior_ports_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        self.behavior_ports_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.behavior_ports_label, 0, 0, 1, 2)

        self.behavior_port_controls = BehaviorPortControls(self.num_ports)
        self.grid_layout.addLayout(self.behavior_port_controls, 1, 0, -1, 2)

        self.bnc_in_label = QLabel()
        self.bnc_in_label.setText("BNC In")
        self.bnc_in_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bnc_in_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )
        self.bnc_in_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.bnc_in_label, 0, 4, 1, 1)

        self.bnc_out_label = QLabel()
        self.bnc_out_label.setText("BNC Out")
        self.bnc_out_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bnc_out_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum
        )
        self.bnc_out_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.bnc_out_label, 0, 6, 1, 1)

        self.wire_in_label = QLabel()
        self.wire_in_label.setText("Wire In")
        self.wire_in_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wire_in_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.wire_in_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.wire_in_label, 1, 4, 1, 1)

        self.wire_out_label = QLabel()
        self.wire_out_label.setText("Wire Out")
        self.wire_out_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wire_out_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.wire_out_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.wire_out_label, 1, 6, 1, 1)

class BehaviorPortControls(QGridLayout):
    def __init__(self, num_ports):
        super().__init__()

        self.num_ports = num_ports

        self.populate_ports()



    def populate_ports(self):
        _layouts = []

        _blank = QLabel()
        _blank.setText("")
        _blank.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        _blank.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.addWidget(_blank, 0, 0, 1, 1)

        _valve_controls_label = QLabel()
        _valve_controls_label.setText("VLV")
        _valve_controls_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _valve_controls_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding
        )
        self.addWidget(_valve_controls_label, 1, 0, 1, 1)

        _LED_label = QLabel()
        _LED_label.setText("LED")
        _LED_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _LED_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding
        )
        self.addWidget(_LED_label, 2, 0, 1, 1)

        _poke_label = QLabel()
        _poke_label.setText("Poke")
        _poke_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        _poke_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.MinimumExpanding
        )
        self.addWidget(_poke_label, 3, 0, 1, 1)

        for i in range(self.num_ports):
            _port_label = QLabel()
            _port_label.setText(str(i + 1))
            _port_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            _port_label.setSizePolicy(
                QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
            )
            _port_label.setObjectName(f'port_{i + 1}_label')
            self.addWidget(_port_label, 0, i+1, 1, 1)

            _valve_button = LED()
            _valve_button.setSizePolicy(
                QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
            )
            _valve_button.setObjectName(f'valve_{i+1}')
            self.addWidget(_valve_button, 1, i+1, 1, 1)

            _LED_button = LED()
            _LED_button.setSizePolicy(
                QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
            )
            _LED_button.setObjectName(f'LED_{i+1}')
            self.addWidget(_LED_button, 2, i+1, 1, 1)

            _poke_button = LED()
            _poke_button.setSizePolicy(
                QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
            )
            _poke_button.setObjectName(f'poke_{i+1}')
            self.addWidget(_poke_button, 3, i+1, 1, 1)