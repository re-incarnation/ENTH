from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QApplication
)

from PySide6.QtCore import Qt

from app.titlebar import TitleBar
from app.tray import create_tray

from app.config import (
    APP_NAME,
    WINDOW_BG,
    WINDOW_OPACITY
)

from app.punishment_panel import PunishmentPanel
from app.settings_panel import SettingsPanel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        self.left_open = False
        self.bottom_open = False

        self.old_pos = None



        # =========================
        # MAIN WINDOW
        # =========================

        self.setWindowTitle(APP_NAME)


        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )


        self.setGeometry(
            300,
            200,
            400,
            500
        )


        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {WINDOW_BG};
            }}
        """)


        self.setWindowOpacity(
            WINDOW_OPACITY
        )



        # =========================
        # ROOT
        # =========================

        self.root = QWidget()

        self.setCentralWidget(
            self.root
        )


        self.layout = QVBoxLayout(
            self.root
        )


        self.layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        self.titlebar = TitleBar(self)

        self.layout.addWidget(
            self.titlebar
        )


        self.layout.addStretch()



        # =========================
        # BUTTONS
        # =========================

        self.btn_punish = QPushButton(
            "Наказание"
        )

        self.btn_skip = QPushButton(
            "Скип"
        )

        self.btn_history = QPushButton(
            "История"
        )

        self.btn_settings = QPushButton(
            "Настройки"
        )


        for btn in [
            self.btn_punish,
            self.btn_skip,
            self.btn_history,
            self.btn_settings
        ]:

            btn.setFixedHeight(28)

            btn.setStyleSheet("""
                QPushButton {
                    background-color: rgba(40,40,40,180);
                    color:white;
                    border-radius:0px;
                    border:1px solid rgba(255,255,255,15);
                }

                QPushButton:hover {
                    background-color: rgba(70,70,70,200);
                }
            """)



        self.btn_punish.clicked.connect(
            self.toggle_left
        )


        self.btn_settings.clicked.connect(
            self.toggle_bottom
        )



        row1 = QHBoxLayout()
        row2 = QHBoxLayout()



        row1.addWidget(
            self.btn_punish
        )

        row1.addWidget(
            self.btn_skip
        )


        row2.addWidget(
            self.btn_history
        )

        row2.addWidget(
            self.btn_settings
        )


        self.layout.addLayout(
            row1
        )

        self.layout.addLayout(
            row2
        )



        # =========================
        # PANELS
        # =========================


        self.left_panel = PunishmentPanel()


        self.left_panel.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )


        self.left_panel.setWindowOpacity(
            WINDOW_OPACITY
        )


        self.left_panel.resize(
            300,
            250
        )


        self.left_panel.hide()



        self.bottom_panel = SettingsPanel()


        self.bottom_panel.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )


        self.bottom_panel.setWindowOpacity(
            WINDOW_OPACITY
        )


        self.bottom_panel.resize(
            400,
            220
        )


        self.bottom_panel.hide()



        # =========================
        # TRAY
        # =========================

        self.tray = create_tray(
            self
        )



    # =========================
    # PANEL POSITIONS
    # =========================

    def update_panels(self):

        geo = self.frameGeometry()


        x = geo.x()
        y = geo.y()

        w = geo.width()
        h = geo.height()



        if self.left_open:

            self.left_panel.move(
                x - self.left_panel.width(),
                y + h - self.left_panel.height()
            )



        if self.bottom_open:

            self.bottom_panel.move(
                x,
                y + h
            )



    # =========================
    # TOGGLES
    # =========================

    def toggle_left(self):

        self.left_open = not self.left_open


        if self.left_open:

            self.update_panels()

            self.left_panel.show()

            self.left_panel.raise_()


        else:

            self.left_panel.hide()



    def toggle_bottom(self):

        self.bottom_open = not self.bottom_open


        if self.bottom_open:

            self.update_panels()

            self.bottom_panel.show()

            self.bottom_panel.raise_()


        else:

            self.bottom_panel.hide()



    # =========================
    # FOLLOW WINDOW
    # =========================

    def moveEvent(self, event):

        self.update_panels()



    def resizeEvent(self, event):

        self.update_panels()



    # =========================
    # DRAG
    # =========================

    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.old_pos = (
                event.globalPosition()
                .toPoint()
            )



    def mouseMoveEvent(self, event):

        if self.old_pos:

            delta = (
                event.globalPosition()
                .toPoint()
                -
                self.old_pos
            )


            self.move(
                self.x() + delta.x(),
                self.y() + delta.y()
            )


            self.old_pos = (
                event.globalPosition()
                .toPoint()
            )



    def mouseReleaseEvent(self, event):

        self.old_pos = None



    # =========================
    # TRAY
    # =========================

    def hide_to_tray(self):

        self.hide()



    def toggle_window(self):

        if self.isVisible():

            self.hide()

        else:

            self.show()

            self.raise_()



    def exit_app(self):

        self.tray.hide()

        self.left_panel.close()

        self.bottom_panel.close()

        QApplication.quit()



    def closeEvent(self, event):

        event.ignore()

        self.hide_to_tray()