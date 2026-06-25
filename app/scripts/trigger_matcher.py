import json
import re
from pathlib import Path

from app.scripts.trigger_models import (
    TriggerEvent,
    SEVERITY_YELLOW,
    SEVERITY_RED
)


class TriggerMatcher:


    def __init__(self, rules_path):

        self.rules_path = Path(
            rules_path
        )

        self.rules = {}
        self.exceptions = []

        self.load()



    def load(self):

        if not self.rules_path.exists():
            return


        with open(
            self.rules_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)


        self.rules = data.get(
            "rules",
            {}
        )


        self.exceptions = (
            data
            .get("exceptions", {})
            .get("allowed_words", [])
        )



    def is_exception(
        self,
        text
    ):

        text = text.lower()


        for word in self.exceptions:

            if word.lower() in text:

                return True


        return False



    def check_rule(
        self,
        rule
    ):

        result = []


        result += rule.get(
            "phrases",
            []
        )


        result += rule.get(
            "projects",
            []
        )


        result += rule.get(
            "masked",
            []
        )


        result += rule.get(
            "words",
            []
        )


        result += rule.get(
            "roots",
            []
        )


        result += rule.get(
            "money_words",
            []
        )


        return result



    def match(
        self,
        player,
        message
    ):


        if not message:

            return None



        if self.is_exception(
            message
        ):

            return None



        text = message.lower().strip()


        text = re.sub(
            r"[^а-яa-z0-9ё\s]",
            " ",
            text
        )




        for rule_id, rule in self.rules.items():



            triggers = self.check_rule(
                rule
            )


            for trigger in triggers:


                trigger = trigger.lower().strip()


                if len(trigger) < 3:

                    continue



                if trigger in text:


                    severity = SEVERITY_YELLOW


                    return TriggerEvent.create(

                        player=player,

                        message=message,

                        rule_id=rule_id,

                        rule_name=rule.get(
                            "name",
                            ""
                        ),

                        severity=severity

                    )


        return None