import os
import re



class MinecraftLogParser:


    def __init__(self, logs_folder):

        self.logs_folder = logs_folder
        self.position = 0



    def decode_line(self, raw):

        encodings = [
            "utf-8",
            "cp1251",
            "cp866"
        ]


        for enc in encodings:

            try:
                return raw.decode(
                    enc
                )

            except UnicodeDecodeError:
                pass


        return raw.decode(
            "utf-8",
            errors="ignore"
        )



    def get_latest_log(self):

        if not self.logs_folder:

            return None


        path = os.path.join(
            self.logs_folder,
            "latest.log"
        )


        if os.path.isfile(path):

            return path


        return None



    def update_folder(self, folder):

        self.logs_folder = folder
        self.position = 0



    def read_new_lines(self):

        log_file = self.get_latest_log()


        if not log_file:

            return []


        try:

            with open(
                log_file,
                "rb"
            ) as file:


                file.seek(
                    self.position
                )


                raw_lines = file.readlines()


                self.position = file.tell()


                lines = []


                for raw in raw_lines:

                    lines.append(
                        self.decode_line(
                            raw
                        )
                    )


                return lines


        except Exception:

            return []



    def parse_chat(self, line):


        if (
            "ChatComponent" not in line
            or
            "[CHAT]" not in line
        ):

            return None



        text = line.split(
            "[CHAT]",
            1
        )[1].strip()



        if not text:

            return None



        # системный чат пропускаем

        if text.startswith(
            "[System]"
        ):

            return None



        ignored = [
            "---------------",
            "----------------",
            "��������",
            "����"
        ]


        for word in ignored:

            if word in text:

                return None



        return {
            "type": "player_chat",
            "message": text
        }



    def get_messages(self):

        result = []


        lines = self.read_new_lines()


        for line in lines:


            msg = self.parse_chat(
                line
            )


            if msg:

                result.append(
                    msg
                )


        return result