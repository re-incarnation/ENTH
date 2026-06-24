from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

from app.config import (
    WINDOW_BG,
    WINDOW_OPACITY
)


class PunishmentPanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.setAttribute(
            Qt.WA_StyledBackground,
            True
        )


        self.setStyleSheet(f"""
            QWidget {{
                background-color: {WINDOW_BG};
                border: none;
            }}
        """)


        self.setWindowOpacity(
            WINDOW_OPACITY
        )


        # внутренняя обводка
        self.frame = QWidget(self)

        self.frame.setStyleSheet("""
            QWidget {
                background: transparent;
                border: 1px solid rgba(230,230,230,25);
            }
        """)


        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            1,1,1,1
        )

        layout.addWidget(
            self.frame
        )