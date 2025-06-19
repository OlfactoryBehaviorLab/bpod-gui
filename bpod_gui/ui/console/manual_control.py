from qtpy.QtCore import Qt, QSize
from qtpy.QtWidgets import (
    QDockWidget,
    QWidget,
    QGridLayout,
    QLabel,
    QSizePolicy,
    QFrame,
    QVBoxLayout,
    QTabWidget,
    QLayout,
    QPushButton,
)
from bpod_gui import __version__
from .state_machine_widget import StateMachineWidget
from .module_widget import ModuleWidget

VERSION = __version__


class ManualControlContainer(QDockWidget):
    def __init__(self):
        super().__init__()
        self.mc_widget = ManualControl()
        self.setWidget(self.mc_widget)
        self.setFloating(True)


class ManualControl(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Manual Control")
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        ## Row 1
        self.title = QLabel()
        self.title.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.title.setText("Bpod Console ")
        self.title.setObjectName("manual_control_title")
        self.main_layout.addWidget(self.title, 0, 0, 1, 2)

        self.title_line = QFrame()
        self.title_line.setFrameShape(QFrame.Shape.HLine)
        self.title_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.title_line.setSizePolicy(
            QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum
        )
        self.title_line.setLineWidth(5)
        self.title_line.setMidLineWidth(5)
        self.title_line.setMinimumWidth(200)

        self.main_layout.addWidget(self.title_line, 0, 2, 1, -1)

        ## ===Row 2===
        # Column 1: Live Info
        self.live_info_layout = LiveInfoColumn()
        self.main_layout.addLayout(self.live_info_layout, 1, 0, -1, 1)

        # Middle Columns: Tabbed Controls

        self.central_tabbed_container = QTabWidget()
        self.state_machine_widget = StateMachineWidget()
        self.central_tabbed_container.addTab(self.state_machine_widget, "State Machine")
        # These are placeholders; will dynamically fill later
        self.central_tabbed_container.addTab(ModuleWidget(), "Module 1")
        self.central_tabbed_container.addTab(ModuleWidget(), "Module 2")
        self.central_tabbed_container.addTab(ModuleWidget(), "Module 3")
        self.main_layout.addWidget(self.central_tabbed_container, 1, 1, -1, 3)

        # Rightmost Column: Misc. Controls
        self.controls_layout = ControlsColumn()
        self.main_layout.addLayout(self.controls_layout, 1, 4, -1, 1)

    @staticmethod
    def apply_size_policy_to_layout(
        layout: QLayout,
        horizontal_policy: QSizePolicy.Policy,
        vertical_policy: QSizePolicy.Policy,
    ) -> None:
        """
        Iterates over widgets in the provided QLayout and calls **setSizePolicy** on
        each widget using the horizontal_policy and vertical_policy parameters.
        :param layout: QLayout
        :param horizontal_policy: QSizePolicy.Policy
        :param vertical_policy: QSizePolicy.Policy
        """
        for i in range(layout.count()):
            layout.itemAt(i).widget().setSizePolicy(horizontal_policy, vertical_policy)

    @staticmethod
    def apply_max_width_to_layout(layout: QLayout, max_width: int) -> None:
        """
        Iterates over the widgets in the provided QLayout and calls **setMaximumWidth** on
        each widget using the max_width parameter.

        :param layout: QLayout
        :param max_width: int
        """
        for i in range(layout.count()):
            layout.itemAt(i).widget().setMaximumWidth(max_width)


class LiveInfoColumn(QVBoxLayout):

    def __init__(self):
        super().__init__()
        self.live_info_header = QLabel()
        self.live_info_header.setText("  Live Info  ")
        self.live_info_header.setProperty("type", "header")
        self.live_info_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.addWidget(self.live_info_header)

        self.current_state_header = QLabel()
        self.current_state_header.setText("Current State")
        self.current_state_display = QLabel()
        self.current_state_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_state_display.setText("---")
        self.current_state_display.setProperty("type", "live-info")
        self.addWidget(self.current_state_header)
        self.addWidget(self.current_state_display)

        self.previous_state_header = QLabel()
        self.previous_state_header.setText("Previous State")
        self.previous_state_display = QLabel()
        self.previous_state_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.previous_state_display.setText("---")
        self.previous_state_display.setProperty("type", "live-info")
        self.addWidget(self.previous_state_header)
        self.addWidget(self.previous_state_display)

        self.last_event_header = QLabel()
        self.last_event_header.setText("Last Event")
        self.last_event_display = QLabel()
        self.last_event_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.last_event_display.setText("---")
        self.last_event_display.setProperty("type", "live-info")
        self.addWidget(self.last_event_header)
        self.addWidget(self.last_event_display)

        self.session_time_header = QLabel()
        self.session_time_header.setText("Session Time")
        self.session_time_display = QLabel()
        self.session_time_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.session_time_display.setText("0:00:00")
        self.session_time_display.setProperty("type", "live-info")
        self.addWidget(self.session_time_header)
        self.addWidget(self.session_time_display)

        self.port_header = QLabel()
        self.port_header.setText("Port")
        self.port_display = QLabel()
        self.port_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.port_display.setText("PORT_HERE")
        self.port_display.setProperty("type", "live-info")
        self.addWidget(self.port_header)
        self.addWidget(self.port_display)

        self.gui_version = QLabel()
        self.gui_version.setText(f"v{VERSION}")
        self.gui_version.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.gui_version.setObjectName("version")
        self.addWidget(self.gui_version)

        ManualControl.apply_size_policy_to_layout(
            self,
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum,
        )
        ManualControl.apply_max_width_to_layout(self, 150)

class ControlsColumn(QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.config_layout = QGridLayout()
        self.config_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.config_header = QLabel()
        self.config_header.setText("  Config  ")
        self.config_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.config_header.setProperty("type", "header")
        self.addWidget(self.config_header)

        self.refresh_button = QPushButton()
        self.refresh_button.setText("R")
        self.refresh_button.setToolTip("Refresh Module Information")
        self.refresh_button.setMaximumSize(QSize(30, 30))
        self.settings_button = QPushButton()
        self.settings_button.setText("S")
        self.settings_button.setMaximumSize(QSize(30, 30))
        self.settings_button.setToolTip("Open settings menu")
        self.USB_button = QPushButton()
        self.USB_button.setText("U")
        self.USB_button.setMaximumSize(QSize(30, 30))
        self.USB_button.setToolTip("Configure module USB ports")
        self.sys_info_button = QPushButton()
        self.sys_info_button.setText("I")
        self.sys_info_button.setMaximumSize(QSize(30, 30))
        self.sys_info_button.setToolTip("Open system information")

        self.config_layout.addWidget(self.refresh_button, 1, 0, 1, 1)
        self.config_layout.addWidget(self.settings_button, 1, 1, 1, 1)
        self.config_layout.addWidget(self.USB_button, 2, 0, 1, 1)
        self.config_layout.addWidget(self.sys_info_button, 2, 1, 1, 1)

        self.addLayout(self.config_layout)

        self.session_controls_layout = QVBoxLayout()
        self.session_controls_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.session_controls_header = QLabel()
        self.session_controls_header.setText("  Session  ")
        self.session_controls_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.session_controls_header.setProperty("type", "header")
        self.session_controls_layout.addWidget(self.session_controls_header)

        self.session_play_pause_button = QPushButton()
        self.session_play_pause_button.setText("Play")
        self.session_play_pause_button.setMaximumSize(QSize(90, 90))
        self.session_play_pause_button.setSizePolicy(QSizePolicy.Policy.MinimumExpanding,
                                                     QSizePolicy.Policy.MinimumExpanding)
        self.session_controls_layout.addWidget(self.session_play_pause_button)

        self.session_stop_button = QPushButton()
        self.session_stop_button.setText("Stop")
        self.session_stop_button.setMaximumSize(QSize(90, 90))
        self.session_stop_button.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.session_controls_layout.addWidget(self.session_stop_button)

        self.addLayout(self.session_controls_layout)
