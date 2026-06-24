from PySide6.QtWidgets import QSystemTrayIcon, QMenu
from PySide6.QtGui import QAction, QIcon, QPixmap
from PySide6.QtCore import Qt


def create_tray(window):
    pixmap = QPixmap(32, 32)
    pixmap.fill(Qt.black)

    tray = QSystemTrayIcon(window)
    tray.setIcon(QIcon(pixmap))
    tray.setVisible(True)

    menu = QMenu()

    show_action = QAction("Show / Hide", window)
    show_action.triggered.connect(window.toggle_window)

    exit_action = QAction("Exit", window)
    exit_action.triggered.connect(window.exit_app)

    menu.addAction(show_action)
    menu.addAction(exit_action)

    tray.setContextMenu(menu)

    tray.activated.connect(
        lambda r: window.toggle_window()
        if r == QSystemTrayIcon.Trigger
        else None
    )

    return tray