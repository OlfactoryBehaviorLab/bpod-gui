from qtpy.QtCore import Qt
from qtpy.QtWidgets import QWidget, QSizePolicy, QLabel, QGridLayout, QFrame
from bpod_gui.ui.console.components.LED import LED


class StateMachineWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.num_ports: int = 8

        self.setObjectName("state_machine_widget")
        self.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)

        self.behavior_ports_label = QLabel()
        self.behavior_ports_label.setText("Behavior Ports")
        self.behavior_ports_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.behavior_ports_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.behavior_ports_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.behavior_ports_label, 0, 0, 1, 2)

        self.behavior_port_controls = BehaviorPortControls(self.num_ports)
        self.grid_layout.addLayout(self.behavior_port_controls, 1, 0, -1, 2)

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.Shape.VLine)
        self.separator.setFrameShadow(QFrame.Shadow.Raised)
        self.separator.setLineWidth(5)
        self.grid_layout.addWidget(self.separator, 0, 3, -1, 1)

        self.bnc_in_label = QLabel()
        self.bnc_in_label.setText("BNC In")
        self.bnc_in_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bnc_in_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.bnc_in_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.bnc_in_label, 0, 4, 1, 3)

        self.bnc_out_label = QLabel()
        self.bnc_out_label.setText("BNC Out")
        self.bnc_out_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bnc_out_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )

        self.IOControls = IOControls()
        self.grid_layout.addLayout(self.IOControls, 1, 4, 1, -1)

        self.bnc_out_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.bnc_out_label, 0, 6, 1, 1)

        self.wire_in_label = QLabel()
        self.wire_in_label.setText("Wire In")
        self.wire_in_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wire_in_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.wire_in_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.wire_in_label, 2, 4, 1, 1)

        self.wire_out_label = QLabel()
        self.wire_out_label.setText("Wire Out")
        self.wire_out_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wire_out_label.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.wire_out_label.setProperty("type", "smw_underlined_header")
        self.grid_layout.addWidget(self.wire_out_label, 2, 6, 1, 1)

        self.wire_controls = WireControls()
        self.grid_layout.addLayout(self.wire_controls, 3, 4, -1, -1)

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


class IOControls(QGridLayout):
    def __init__(self):
        super().__init__()

        self.input_1_label = QLabel()
        self.input_1_label.setText("1")
        self.input_1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_1_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.input_1_label, 0, 0, 1, 1)

        self.input_2_label = QLabel()
        self.input_2_label.setText("2")
        self.input_2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.input_2_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.input_2_label, 0, 1, 1, 1)

        self.output_1_label = QLabel()
        self.output_1_label.setText("1")
        self.output_1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_1_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.output_1_label, 0, 3, 1, 1)

        self.output_2_label = QLabel()
        self.output_2_label.setText("2")
        self.output_2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.output_2_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.output_2_label, 0, 4, 1, 1)

        self.input_1_button = LED()
        self.input_1_button.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.input_1_button.setObjectName('input_1_button')
        self.addWidget(self.input_1_button, 1, 0, 1, 1)

        self.input_2_button = LED()
        self.input_2_button.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.input_2_button.setObjectName('input_2_button')
        self.addWidget(self.input_2_button, 1, 1, 1, 1)

        self.output_1_button = LED()
        self.output_1_button.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.output_1_button.setObjectName('output_1_button')
        self.addWidget(self.output_1_button, 1, 3, 1, 1)

        self.output_2_button = LED()
        self.output_2_button.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.output_2_button.setObjectName('output_2_button')
        self.addWidget(self.output_2_button, 1, 4, 1, 1)

class WireControls(QGridLayout):
    def __init__(self):
        super().__init__()

        self.wire_in_1_label = QLabel()
        self.wire_in_1_label.setText("1")
        self.wire_in_1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wire_in_1_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.wire_in_1_label, 0, 0, 1, 1)

        self.wire_in_2_label = QLabel()
        self.wire_in_2_label.setText("2")
        self.wire_in_2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wire_in_2_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.wire_in_2_label, 0, 1, 1, 1)

        self.wire_in_3_label = QLabel()
        self.wire_in_3_label.setText("3")
        self.wire_in_3_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wire_in_3_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.wire_in_3_label, 2, 0, 1, 1)

        self.wire_in_4_label = QLabel()
        self.wire_in_4_label.setText("4")
        self.wire_in_4_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wire_in_4_label.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum
        )
        self.addWidget(self.wire_in_4_label, 2, 1, 1, 1)

        self.wire_in_1_button = LED()
        self.wire_in_1_button.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.wire_in_1_button.setObjectName('wire_in_1_button')
        self.addWidget(self.wire_in_1_button, 1, 0, 1, 1)

        self.wire_in_2_button = LED()
        self.wire_in_2_button.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.wire_in_2_button.setObjectName('wire_in_2_button')
        self.addWidget(self.wire_in_2_button, 1, 1, 1, 1)

        self.wire_in_3_button = LED()
        self.wire_in_3_button.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.wire_in_3_button.setObjectName('wire_in_3_button')
        self.addWidget(self.wire_in_3_button, 3, 0, 1, 1)

        self.wire_in_4_button = LED()
        self.wire_in_4_button.setSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum
        )
        self.wire_in_4_button.setObjectName('wire_in_4_button')
        self.addWidget(self.wire_in_4_button, 3, 1, 1, 1)
