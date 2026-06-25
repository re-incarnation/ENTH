import json
import os


class TriggerStore:


    def __init__(self, path):

        self.path = path

        folder = os.path.dirname(path)

        if folder and not os.path.exists(folder):
            os.makedirs(folder)



    def save(self, trigger):

        with open(
            self.path,
            "a",
            encoding="utf-8"
        ) as file:

            file.write(
                json.dumps(
                    trigger.to_dict(),
                    ensure_ascii=False
                )
                +
                "\n"
            )



    def load(self):

        result = []


        if not os.path.exists(
            self.path
        ):
            return result



        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as file:


            for line in file:


                try:

                    result.append(
                        json.loads(line)
                    )


                except:

                    pass



        return result