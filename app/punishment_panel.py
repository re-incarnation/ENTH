from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit
)

from app.config import WINDOW_BG, WINDOW_OPACITY


class PunishmentPanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.setWindowOpacity(
            WINDOW_OPACITY
        )


        self.setStyleSheet("""
            QWidget {
                background: transparent;
            }
        """)


        root = QVBoxLayout(self)

        root.setContentsMargins(
            0,
            0,
            0,
            0
        )


        self.frame = QWidget()


        self.frame.setStyleSheet(f"""
            QWidget {{
                background-color: {WINDOW_BG};
                border:1px solid rgba(230,230,230,35);
            }}
        """)


        root.addWidget(
            self.frame
        )


        layout = QVBoxLayout(
            self.frame
        )


        layout.setContentsMargins(
            12,
            12,
            12,
            12
        )


        layout.setSpacing(
            18
        )


        # ==================
        # TYPES
        # ==================

        top = QHBoxLayout()

        top.addStretch()


        self.ban_btn = QPushButton("Ban")
        self.mute_btn = QPushButton("Mute")
        self.warn_btn = QPushButton("Warn")


        for btn in [
            self.ban_btn,
            self.mute_btn,
            self.warn_btn
        ]:

            btn.setFixedWidth(70)

            btn.setStyleSheet("""
                QPushButton {
                    background: rgba(50,50,50,160);
                    color:white;
                    border:1px solid rgba(255,255,255,25);
                    padding:6px;
                }

                QPushButton:hover {
                    background:rgba(75,75,75,180);
                }
            """)

            top.addWidget(btn)

            top.addSpacing(15)


        top.addStretch()


        layout.addLayout(top)



        # ==================
        # REASON
        # ==================

        self.reason = QLineEdit()

        self.reason.setPlaceholderText(
            "Reason"
        )

        layout.addWidget(
            self.reason
        )



        # ==================
        # TIME
        # ==================

        self.time_box = QWidget()

        self.time_layout = QHBoxLayout(
            self.time_box
        )

        self.time_layout.addStretch()


        self.time_buttons = []


        self.time_layout.addStretch()


        layout.addWidget(
            self.time_box
        )


        self.time_box.hide()



        # ==================
        # COPY
        # ==================

        bottom = QHBoxLayout()

        bottom.addStretch()


        self.copy_btn = QPushButton(
            "Copy"
        )

        self.copy_btn.setFixedWidth(
            90
        )

        bottom.addWidget(
            self.copy_btn
        )


        bottom.addStretch()


        layout.addLayout(bottom)



        self.ban_btn.clicked.connect(
            lambda: self.select_type("ban")
        )

        self.mute_btn.clicked.connect(
            lambda: self.select_type("mute")
        )

        self.warn_btn.clicked.connect(
            lambda: self.select_type("warn")
        )



    def select_type(self, mode):

        for btn in self.time_buttons:
            btn.deleteLater()


        self.time_buttons.clear()


        if mode == "ban":

            times = ["1d","3d","7d"]


        elif mode == "mute":

            times = ["1h","3h","7h"]


        else:

            times = []


        if not times:

            self.time_box.hide()

            return


        for t in times:

            btn = QPushButton(t)

            btn.setFixedWidth(
                45
            )


            self.time_layout.insertWidget(
                len(self.time_buttons)+1,
                btn
            )


            self.time_buttons.append(
                btn
            )


        self.time_box.show()