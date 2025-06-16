from qtpy import QtWidgets, QtGui, QtCore
from qtpy.QtCore import Qt


class LED(QtWidgets.QAbstractButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setCheckable(True)

    def sizeHint(self) -> QtCore.QSize:
        return QtCore.QSize(35, 35)

    def paintEvent(self, e) -> None:
        # base
        size = min(self.size().toTuple())
        w_line = round(size / 25) * 2
        painter = QtGui.QPainter(self)
        painter.setRenderHints(QtGui.QPainter.RenderHint.Antialiasing)
        color = QtGui.QColor("red")
        painter.setPen(
            QtGui.QPen(color.darker(110 if self.isChecked() else 150), w_line)
        )
        if self.isChecked():
            painter.setBrush(QtGui.QBrush(color))
        else:
            gradient = QtGui.QRadialGradient(size / 2, size / 5 * 4, size * 0.5)
            gradient.setColorAt(0, color)
            gradient.setColorAt(1, color.darker(150))
            painter.setBrush(QtGui.QBrush(gradient))
        painter.drawEllipse(w_line / 2, w_line / 2, size - w_line, size - w_line)

        # glow
        if self.isChecked():
            painter.setPen(QtGui.QPen(Qt.PenStyle.NoPen))
            gradient = QtGui.QRadialGradient(size / 2, size / 2, size / 2)
            gradient.setColorAt(0, QtGui.QColor("white"))
            gradient.setColorAt(0.3, QtGui.QColor("yellow"))
            gradient.setColorAt(1, QtGui.QColor("transparent"))
            painter.setBrush(QtGui.QBrush(gradient))
            painter.drawEllipse(0, 0, size, size)

        # reflection
        painter.setPen(QtGui.QPen(Qt.PenStyle.NoPen))
        gradient = QtGui.QLinearGradient(0, 0, 0, size * 0.5)
        gradient.setColorAt(0, QtGui.QColor("white"))
        gradient.setColorAt(1, QtGui.QColor("transparent"))
        painter.setBrush(QtGui.QBrush(gradient))
        painter.drawEllipse(size * 0.2, w_line, size * 0.6, size * 0.5)
