from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QPushButton, QWidget, QSizePolicy
from PySide6.QtCore import Qt


class TitleBar(QFrame):
    def __init__(self, window):
        super().__init__()

        self.window = window
        self.setFixedHeight(38)

        self.setStyleSheet("""
            QFrame {
                background-color: rgba(20, 20, 20, 180);
            }
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0)

        left = QWidget()
        left.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        title = QLabel("ENTH")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            color: white;
            font-weight: bold;
            font-size: 14px;
        """)

        right = QWidget()
        right.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)

        close_btn = QPushButton("✕")
        close_btn.setFixedSize(26, 26)

        close_btn.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 17px;
                border: none;
                background: transparent;
            }
            QPushButton:hover {
                color: #dddddd;
            }
        """)

        close_btn.clicked.connect(window.hide_to_tray)

        layout.addWidget(left)
        layout.addWidget(title)
        layout.addWidget(right)
        layout.addWidget(close_btn)