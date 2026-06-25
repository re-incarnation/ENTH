import json
from pathlib import Path


class TriggerQueue:

    def __init__(
        self,
        path="app/trigger_queue.json"
    ):

        self.path = Path(path)

        if not self.path.exists():
            self.save([])



    def load(self):

        try:

            with open(
                self.path,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except:

            return []



    def save(
        self,
        data
    ):

        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )



    def add(
        self,
        trigger
    ):

        items = self.load()

        items.append(
            trigger.to_dict()
        )

        self.save(
            items
        )



    def active(self):

        return [
            x for x in self.load()
            if x.get("status") == "new"
        ]



    def skip(
        self,
        trigger_id
    ):

        items = self.load()


        for item in items:

            if item.get("id") == trigger_id:

                item["status"] = "skipped"


        self.save(
            items
        )