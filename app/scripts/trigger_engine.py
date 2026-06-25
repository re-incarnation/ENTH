from PySide6.QtCore import QObject, Signal

from app.scripts.trigger_matcher import TriggerMatcher
from app.scripts.trigger_queue import TriggerQueue


class TriggerEngine(QObject):

    trigger_found = Signal(object)


    def __init__(
        self,
        rules_path,
        queue_path
    ):

        super().__init__()


        self.matcher = TriggerMatcher(
            rules_path
        )


        self.queue = TriggerQueue(
            queue_path
        )



    def process(
        self,
        event
    ):


        player = event.get(
            "player",
            "Unknown"
        )


        message = event.get(
            "message",
            ""
        )



        trigger = self.matcher.match(
            player,
            message
        )



        if trigger:


            self.queue.add(
                trigger
            )

            self.trigger_found.emit(
                trigger
            )


            return trigger



        return None



    def process_debug(
        self,
        player,
        message
    ):


        return self.process({

            "player": player,

            "message": message

        })