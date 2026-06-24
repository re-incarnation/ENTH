import json
import os


APP_NAME = "ENTH"

APP_VERSION = "0.3.0"

GITHUB_LINK = ""


# =====================
# UI
# =====================

WINDOW_BG = "#1f1f1f"

WINDOW_OPACITY = 0.88


# =====================
# SETTINGS
# =====================

CONFIG_FILE = "app/settings.json"


DEFAULT_SETTINGS = {
    "sound": True,
    "path_lattest_log": ""
}



def load_settings():

    if not os.path.exists(CONFIG_FILE):

        save_settings(DEFAULT_SETTINGS.copy())


    with open(
        CONFIG_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)



def save_settings(data):

    with open(
        CONFIG_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )



SETTINGS = load_settings()



SOUND = SETTINGS.get(
    "sound",
    True
)


PATH_LATTEST_LOG = SETTINGS.get(
    "path_lattest_log",
    ""
)

RULES_URL = "https://github.com"

SPECIAL_URL = "https://openai.com"