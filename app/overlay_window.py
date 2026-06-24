from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PySide6.QtCore import Qt

from app.titlebar import TitleBar
from app.tray import create_tray
from app.config import APP_NAME


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(APP_NAME)
        self.setGeometry(300, 200, 350, 500)

        self.setWindowFlag(Qt.FramelessWindowHint, True)
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)

        self.setWindowOpacity(0.85)

        self.old_pos = None

        # =========================
        # ROOT
        # =========================
        self.root = QWidget(self)
        self.setCentralWidget(self.root)

        self.layout = QVBoxLayout(self.root)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # TOP
        self.titlebar = TitleBar(self)
        self.layout.addWidget(self.titlebar)

        # PUSH DOWN
        self.layout.addStretch()

        # =========================
        # BOTTOM PANEL
        # =========================
        self.bottom_panel = QWidget()
        self.bottom_panel.setFixedHeight(115)

        bottom_layout = QVBoxLayout(self.bottom_panel)
        bottom_layout.setContentsMargins(10, 10, 10, 10)
        bottom_layout.setSpacing(8)

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        row1.setSpacing(8)
        row2.setSpacing(8)

        btn_punish = QPushButton("Наказание")
        btn_skip = QPushButton("Скип")
        btn_history = QPushButton("История")
        btn_settings = QPushButton("Настройки")

        buttons = [btn_punish, btn_skip, btn_history, btn_settings]

        for btn in buttons:
            btn.setFixedHeight(28)  # 🔥 было 26 → стало 28
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: rgba(40, 40, 40, 200);
                    color: white;
                    border: 1px solid rgba(255, 255, 255, 20);
                    border-radius: 5px;
                    font-size: 11px;
                }

                QPushButton:hover {
                    background-color: rgba(60, 60, 60, 220);
                }

                QPushButton:pressed {
                    background-color: rgba(25, 25, 25, 220);
                }
            """)

        row1.addWidget(btn_punish)
        row1.addWidget(btn_skip)

        row2.addWidget(btn_history)
        row2.addWidget(btn_settings)

        bottom_layout.addLayout(row1)
        bottom_layout.addLayout(row2)

        self.layout.addWidget(self.bottom_panel)

        # TRAY
        self.tray = create_tray(self)

    # DRAG
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

    # CONTROL
    def hide_to_tray(self):
        self.hide()

    def toggle_window(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
            self.raise_()
            self.activateWindow()

    def exit_app(self):
        self.tray.setVisible(False)
        self.close()

        from PySide6.QtWidgets import QApplication
        QApplication.quit()

    def closeEvent(self, event):
        event.ignore()
        self.hide_to_tray()