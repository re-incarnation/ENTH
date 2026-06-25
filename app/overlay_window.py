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
from app.debug_panel import DebugPanel
from app.console_panel import ConsolePanel
from app.scripts.log_monitor import LogMonitor


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()


        self.left_open = False
        self.bottom_open = False
        self.debug_open = False

        self.old_pos = None

        self.log_monitor = LogMonitor()



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
                border: 1px solid rgba(230,230,230,35);
            }}
        """)


        self.setWindowOpacity(
            WINDOW_OPACITY
        )



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

        self.layout.addSpacing(
            6
        )


        self.layout.addStretch()



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


        self.layout.setSpacing(6)
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

        self.debug_panel = DebugPanel()


        self.debug_panel.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )


        self.debug_panel.setWindowOpacity(
            WINDOW_OPACITY
        )


        self.debug_panel.resize(
            300,
            255
        )


        self.debug_panel.hide()

        self.debug_panel.console_btn.clicked.connect(
            self.toggle_console
        )

        self.console_panel = ConsolePanel()

        self.log_monitor.message.connect(
            self.console_panel.add_message
        )


        self.console_panel.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint
        )


        self.console_panel.resize(
            1000,
            400
        )


        self.console_panel.hide()


        self.console_open = False


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
        self.bottom_panel.main_window = self


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



        self.tray = create_tray(
            self
        )



    def update_panels(self):

        geo = self.frameGeometry()

        x = geo.x()
        y = geo.y()

        h = geo.height()


        if self.console_open:

            self.console_panel.move(
                self.x() + self.width(),
                self.y()
            )

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

        if hasattr(self, "debug_panel") and self.debug_panel.isVisible():

            self.debug_panel.move(
                x - self.debug_panel.width(),
                y + h
            )



    def toggle_left(self):

        self.left_open = not self.left_open


        if self.left_open:

            self.update_panels()

            self.left_panel.show()

            self.left_panel.raise_()

        else:

            self.left_panel.hide()

    def toggle_debug(self):

        if self.debug_panel.isVisible():

            self.debug_panel.hide()

        else:

            geo = self.frameGeometry()


            self.debug_panel.move(
                geo.x() - self.debug_panel.width(),
                geo.y() + self.height()
            )


            self.debug_panel.show()

            self.debug_panel.raise_()

    def toggle_bottom(self):

        self.bottom_open = not self.bottom_open


        if self.bottom_open:

            self.update_panels()

            self.bottom_panel.show()

            self.bottom_panel.raise_()

        else:

            self.bottom_panel.hide()



    def moveEvent(self, event):

        self.update_panels()



    def resizeEvent(self, event):

        self.update_panels()



    def mousePressEvent(self, event):

        if event.button() == Qt.LeftButton:

            self.old_pos = event.globalPosition().toPoint()



    def mouseMoveEvent(self, event):

        if self.old_pos:

            delta = (
                event.globalPosition().toPoint()
                -
                self.old_pos
            )

            self.move(
                self.x() + delta.x(),
                self.y() + delta.y()
            )


            self.old_pos = event.globalPosition().toPoint()



    def mouseReleaseEvent(self, event):

        self.old_pos = None



    def hide_to_tray(self):

        if hasattr(self, "left_panel"):

            self.left_panel.setVisible(False)
            self.left_open = False


        if hasattr(self, "bottom_panel"):

            self.bottom_panel.setVisible(False)
            self.bottom_open = False


        if hasattr(self, "debug_panel"):

            self.debug_panel.setVisible(False)


        if hasattr(self, "console_panel"):

            self.console_panel.setVisible(False)
            self.console_open = False


        self.hide()



    def toggle_window(self):

        if self.isVisible():

            self.hide()

        else:

            self.show()
            self.raise_()



    def exit_app(self):

        self.tray.hide()

        self.hide_to_tray()

        self.console_panel.close()

        QApplication.quit()



    def closeEvent(self, event):

        self.hide_to_tray()

        event.ignore()

    def toggle_console(self):

        self.console_open = not self.console_open


        if self.console_open:

            geo = self.frameGeometry()


            self.console_panel.move(
                geo.x() + self.width(),
                geo.y()
            )


            self.console_panel.show()
            self.console_panel.raise_()

        else:

            self.console_panel.hide()