from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPen

from app.config import WINDOW_BG, WINDOW_OPACITY


class ConsolePanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.setWindowOpacity(
            WINDOW_OPACITY
        )


        self.setAttribute(
            Qt.WA_TranslucentBackground
        )


        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            12,
            12,
            12,
            12
        )


        label = QLabel(
            "Console"
        )

        label.setAlignment(
            Qt.AlignTop
        )


        label.setStyleSheet("""
            color:white;
            font-size:15px;
            font-weight:bold;
        """)


        layout.addWidget(
            label
        )



    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(
            QPainter.Antialiasing
        )


        painter.fillRect(
            self.rect(),
            QColor(WINDOW_BG)
        )


        pen = QPen(
            QColor(230,230,230,60)
        )

        pen.setWidth(
            1
        )


        painter.setPen(
            pen
        )


        painter.drawRect(
            0,
            0,
            self.width()-1,
            self.height()-1
        )