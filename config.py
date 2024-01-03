import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6890844798:AAE5XeMUyeP2tIzE7ztAM2Cp8jnCZ7VHh5w")

    APP_ID = int(os.environ.get("APP_ID", 26142667))

    API_HASH = os.environ.get("API_HASH", "f12bdac17aae755867fd8ddb6abd942d")

    