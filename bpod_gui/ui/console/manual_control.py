from qtpy.QtCore import Qt
from qtpy.QtWidgets import QDockWidget, QWidget, QMainWindow, QGridLayout, QLabel, QSizePolicy, QFrame, QVBoxLayout
from bpod_gui import __version__
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
        self.setWindowTitle('Manual Control')
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        ## Row 1
        self.title = QLabel()
        self.title.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.title.setText('Bpod Console ')
        self.title.setObjectName('manual_control_title')
        self.main_layout.addWidget(self.title, 0, 0, 1, 2)

        self.title_line = QFrame()
        self.title_line.setFrameShape(QFrame.Shape.HLine)
        self.title_line.setFrameShadow(QFrame.Shadow.Sunken)
        self.title_line.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        self.title_line.setLineWidth(5)
        self.title_line.setMidLineWidth(5)
        self.title_line.setMinimumWidth(100)

        self.main_layout.addWidget(self.title_line, 0, 2, 1, -1)

        ## Row 2

        # Live Info
        self.live_info_layout = QVBoxLayout()
        self.live_info_header = QLabel()
        self.live_info_header.setText('  Live Info  ')
        self.live_info_header.setObjectName('live_info_header')
        self.live_info_layout.addWidget(self.live_info_header)

        self.current_state_header = QLabel()
        self.current_state_header.setText('Current State')
        self.current_state_display = QLabel()
        self.current_state_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_state_display.setText('---')
        self.current_state_display.setProperty('type', 'live-info')

        self.live_info_layout.addWidget(self.current_state_header)
        self.live_info_layout.addWidget(self.current_state_display)

        self.previous_state_header = QLabel()
        self.previous_state_header.setText('Previous State')
        self.previous_state_display = QLabel()
        self.previous_state_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.previous_state_display.setText('---')
        self.previous_state_display.setProperty('type', 'live-info')

        self.live_info_layout.addWidget(self.previous_state_header)
        self.live_info_layout.addWidget(self.previous_state_display)

        self.last_event_header = QLabel()
        self.last_event_header.setText('Last Event')
        self.last_event_display = QLabel()
        self.last_event_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.last_event_display.setText('---')
        self.last_event_display.setProperty('type', 'live-info')

        self.live_info_layout.addWidget(self.last_event_header)
        self.live_info_layout.addWidget(self.last_event_display)

        self.session_time_header = QLabel()
        self.session_time_header.setText('Session Time')
        self.session_time_display = QLabel()
        self.session_time_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.session_time_display.setText('0:00:00')
        self.session_time_display.setProperty('type', 'live-info')

        self.live_info_layout.addWidget(self.session_time_header)
        self.live_info_layout.addWidget(self.session_time_display)

        self.port_header = QLabel()
        self.port_header.setText('Port')
        self.port_display = QLabel()
        self.port_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.port_display.setText('PORT_HERE')
        self.port_display.setProperty('type', 'live-info')

        self.live_info_layout.addWidget(self.port_header)
        self.live_info_layout.addWidget(self.port_display)

        self.gui_version = QLabel()
        self.gui_version.setText(f"v{VERSION}")
        self.gui_version.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.gui_version.setObjectName('version')

        self.live_info_layout.addWidget(self.gui_version)

        self.main_layout.addLayout(self.live_info_layout, 1, 0, -1, 1)
