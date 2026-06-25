from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QFileDialog,
    QLineEdit,
    QLabel,
    QCheckBox
)

from PySide6.QtCore import Qt

import os
import webbrowser

from app.config import (
    WINDOW_BG,
    WINDOW_OPACITY,
    SETTINGS,
    save_settings,
    RULES_URL,
    SPECIAL_URL
)


class SettingsPanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowOpacity(
            WINDOW_OPACITY
        )

        self.setStyleSheet(f"""
            QWidget {{
                background-color: {WINDOW_BG};
                color: white;
            }}

            QPushButton {{
                background-color: rgba(50,50,50,160);
                color: white;
                border: 1px solid rgba(255,255,255,20);
                padding: 5px;
                min-height: 28px;
            }}

            QPushButton:hover {{
                background-color: rgba(75,75,75,180);
            }}

            QLineEdit {{
                background-color: rgba(20,20,20,120);
                color: white;
                border: 1px solid rgba(255,255,255,25);
                padding: 5px;
            }}
        """)


        root = QVBoxLayout(self)


        self.frame = QWidget()

        self.frame.setStyleSheet(f"""
            QWidget {{
                background-color: {WINDOW_BG};
                border: 1px solid rgba(230,230,230,25);
            }}
        """)


        root.setContentsMargins(
            2,2,2,2
        )

        root.addWidget(
            self.frame
        )


        content = QVBoxLayout(
            self.frame
        )

        content.setContentsMargins(
            10,
            10,
            10,
            10
        )

        content.setSpacing(
            12
        )


        # ======================
        # SOUND SWITCH
        # ======================

        sound_row = QHBoxLayout()

        self.sound = QCheckBox(
            "Sound"
        )

        self.sound.setFixedWidth(
            120
        )

        self.sound.setChecked(
            SETTINGS.get(
                "sound",
                True
            )
        )

        self.sound.stateChanged.connect(
            self.save_sound
        )

        self.sound.setStyleSheet("""
            QCheckBox {
                color:white;
                spacing:8px;
            }

            QCheckBox::indicator {
                width:18px;
                height:18px;
                border-radius:9px;
                background:rgba(180,40,40,220);
                border:1px solid rgba(255,255,255,80);
            }

            QCheckBox::indicator:checked {
                background:rgba(50,220,90,220);
                border:1px solid rgba(255,255,255,120);
            }
        """)


        self.rules_btn = QPushButton(
            "Rules"
        )

        self.rules_btn.setFixedWidth(
            120
        )

        self.rules_btn.clicked.connect(
            lambda: webbrowser.open(
                RULES_URL
            )
        )


        sound_row.addStretch()

        sound_row.addWidget(
            self.sound
        )

        sound_row.addSpacing(
            25
        )

        sound_row.addWidget(
            self.rules_btn
        )

        sound_row.addStretch()


        content.addLayout(
            sound_row
        )


        # ======================
        # SECOND ROW
        # ======================

        row2 = QHBoxLayout()


        self.debug_btn = QPushButton(
            "Debug"
        )

        self.debug_btn.clicked.connect(
            self.open_debug
        )

        self.debug_btn.setFixedWidth(
            120
        )


        self.special_btn = QPushButton(
            "Special"
        )

        self.special_btn.setFixedWidth(
            120
        )


        self.special_btn.clicked.connect(
            lambda: webbrowser.open(
                SPECIAL_URL
            )
        )


        row2.addStretch()

        row2.addWidget(
            self.debug_btn
        )

        row2.addSpacing(
            25
        )

        row2.addWidget(
            self.special_btn
        )

        row2.addStretch()


        content.addLayout(
            row2
        )


        content.addSpacing(
            10
        )


        # ======================
        # PATH
        # ======================

        title = QLabel(
            "Корневая папка"
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        content.addWidget(
            title
        )


        path_row = QHBoxLayout()


        self.path_edit = QLineEdit()

        self.path_edit.setReadOnly(
            True
        )

        self.path_edit.setText(
            SETTINGS.get(
                "path_lattest_log",
                ""
            )
        )


        self.change_btn = QPushButton(
            "Изменить"
        )


        self.change_btn.clicked.connect(
            self.change_path
        )


        path_row.addWidget(
            self.path_edit
        )

        path_row.addWidget(
            self.change_btn
        )


        content.addLayout(
            path_row
        )


        self.open_btn = QPushButton(
            "Открыть директорию"
        )


        self.open_btn.clicked.connect(
            self.open_folder
        )


        content.addWidget(
            self.open_btn
        )



    def save_sound(self):

        SETTINGS["sound"] = (
            self.sound.isChecked()
        )

        save_settings(
            SETTINGS
        )



    def change_path(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Выберите папку"
        )

        if folder:

            SETTINGS["path_lattest_log"] = folder

            self.path_edit.setText(
                folder
            )

            save_settings(
                SETTINGS
            )



    def open_folder(self):

        folder = SETTINGS.get(
            "path_lattest_log",
            ""
        )

        if folder and os.path.exists(
            folder
        ):

            os.startfile(
                folder
            )

    def open_debug(self):

        if hasattr(self, "main_window"):

            self.main_window.toggle_debug()