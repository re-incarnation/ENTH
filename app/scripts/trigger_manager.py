from PySide6.QtCore import QObject, Signal

from app.scripts.trigger_engine import TriggerEngine


class TriggerManager(QObject):

    trigger_added = Signal(object)


    def __init__(
        self,
        rules,
        queue
    ):

        super().__init__()


        self.engine = TriggerEngine(
            rules,
            queue
        )


        self.engine.trigger_found.connect(
            self.on_trigger
        )



    def process(
        self,
        data
    ):

        self.engine.process(
            data
        )



    def on_trigger(
        self,
        trigger
    ):

        self.trigger_added.emit(
            trigger
        )