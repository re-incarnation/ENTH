from PySide6.QtCore import QObject, Signal, QTimer

from app.scripts.log_parser import MinecraftLogParser
from app.config import SETTINGS


class LogMonitor(QObject):

    message = Signal(str)
    event = Signal(dict)

    def __init__(self):

        super().__init__()

        self.parser = MinecraftLogParser(
            SETTINGS.get(
                "path_lattest_log",
                ""
            )
        )

        self.timer = QTimer(
            self
        )

        self.timer.timeout.connect(
            self.scan
        )

        self.timer.start(
            300
        )

    def scan(self):

        for msg in self.parser.get_messages():

            self.message.emit(
                msg["message"]
            )

            self.event.emit(
                msg
            )