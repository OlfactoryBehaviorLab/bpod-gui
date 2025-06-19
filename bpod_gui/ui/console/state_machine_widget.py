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
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.grid_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.behavior_ports_label = QLabel()
        self.behavior_ports_label.setText("Behavior Ports")
        self.behavior_ports_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.behavior_ports_label.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum
        )
        self.behavior_ports_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.behavior_ports_label, 0, 1, 1, self.num_ports)

        self.behavior_port_controls = BehaviorPortControls(self.num_ports)
        self.grid_layout.addLayout(self.behavior_port_controls, 1, 0, -1, 4)
        #
        # self.add_port_numbers()

        self.bnc_in_label = QLabel()
        self.bnc_in_label.setText("BNC In")
        self.bnc_in_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bnc_in_label.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum
        )
        self.bnc_in_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.bnc_in_label, 0, 3, 1, 1)

        self.bnc_out_label = QLabel()
        self.bnc_out_label.setText("BNC Out")
        self.bnc_out_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bnc_out_label.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum
        )
        self.bnc_out_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.bnc_out_label, 0, 4, 1, 1)




class BehaviorPortControls(QGridLayout):
    def __init__(self, num_ports):
        super().__init__()

        self.num_ports = num_ports

        self.valve_controls_label = QLabel()
        self.valve_controls_label.setText("VLV")
        self.valve_controls_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.valve_controls_label.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.valve_controls_label, 1, 0, 1, 1)

        self.LED_label = QLabel()
        self.LED_label.setText("LED")
        self.LED_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LED_label.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.LED_label, 2, 0, 1, 1)

        self.poke_label = QLabel()
        self.poke_label.setText("Poke")
        self.poke_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.poke_label.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.poke_label, 3, 0, 1, 1)

        self.populate_ports()



    def populate_ports(self):
        _port_numbers = []
        _valve_buttons = []
        _LED_buttons = []
        _poke_buttons = []
        for i in range(self.num_ports):
            _port_label = QLabel()
            _port_label.setText(str(i + 1))
            _port_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            _port_label.setSizePolicy(
                QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Maximum
            )
            _port_label.setObjectName(f'port_{i + 1}_label')
            _port_numbers.append(_port_label)

            _valve_button = LED()
            _valve_button.setSizePolicy(
                QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
            )
            _valve_button.setObjectName(f'valve_{i+1}')
            _valve_buttons.append(_valve_button)

            _LED_button = LED()
            _LED_button.setSizePolicy(
                QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
            )
            _LED_button.setObjectName(f'LED_{i+1}')
            _LED_buttons.append(_LED_button)

            _poke_button = LED()
            _poke_button.setSizePolicy(
                QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
            )
            _poke_button.setObjectName(f'poke_{i+1}')
            _poke_buttons.append(_poke_button)
        self._add_items_to_row(_port_numbers, 0, 1)
        self._add_items_to_row(_valve_buttons, 1, 1)
        self._add_items_to_row(_LED_buttons, 2, 1)
        self._add_items_to_row(_poke_buttons, 3, 1)



    def _add_items_to_row(self, items: Iterable, row_number: int, start_column: int):
        for item in items:
            self.addWidget(item, row_number, start_column, 1, 1)
            start_column += 1