from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QColor, QPen

from app.config import WINDOW_BG, WINDOW_OPACITY


class DebugPanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.setWindowOpacity(
            WINDOW_OPACITY
        )

        self.setAttribute(
            Qt.WA_TranslucentBackground
        )


        self.setStyleSheet("""
            QLineEdit {
                background: rgba(20,20,20,120);
                color:white;
                border:1px solid rgba(255,255,255,25);
                padding:5px;
            }
        """)


        root = QVBoxLayout(self)


        root.setContentsMargins(
            12,
            10,
            12,
            10
        )


        root.setSpacing(
            12
        )


        title = QLabel(
            "Test Request"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        title.setStyleSheet("""
            color:white;
            font-size:15px;
            font-weight:bold;
            background:transparent;
        """)


        root.addWidget(
            title
        )


        separator = QLabel(
            "────────────────────"
        )

        separator.setAlignment(
            Qt.AlignCenter
        )

        separator.setStyleSheet("""
            color:rgba(255,255,255,80);
            background:transparent;
        """)


        root.addWidget(
            separator
        )


        self.text_input = QLineEdit()

        self.text_input.setPlaceholderText(
            "Text"
        )


        root.addWidget(
            self.text_input
        )


        self.rule_input = QLineEdit()

        self.rule_input.setPlaceholderText(
            "Rule"
        )


        root.addWidget(
            self.rule_input
        )



        root.addStretch()



        self.console_btn = QPushButton(
            "Console"
        )


        self.push_btn = QPushButton(
            "Push"
        )


        for btn in [
            self.console_btn,
            self.push_btn
        ]:

            btn.setFixedWidth(
                135
            )

            btn.setFixedHeight(
                34
            )


            btn.setStyleSheet("""
                QPushButton {
                    background: rgba(50,50,50,160);
                    color:white;
                    border:1px solid rgba(255,255,255,30);
                }

                QPushButton:hover {
                    background:rgba(75,75,75,180);
                }
            """)



        root.addWidget(
            self.console_btn,
            alignment=Qt.AlignCenter
        )


        root.addWidget(
            self.push_btn,
            alignment=Qt.AlignCenter
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