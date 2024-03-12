class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1910728581"
    sudo_users = "1910728581"
    GROUP_ID = -1002106866999
    TOKEN = "6578686182:AAEUthIVEi3rmiWqkztldBAaLs38ZwyeyFo"
    mongo_url = "mongodb+srv://Hackx:Hackx@hackx.6flteju.mongodb.net/?retryWrites=true&w=majority&appName=Hackx"
    PHOTO_URL = ["https://graph.org/file/d4c3e0cfdea337d761f6f.jpg", "https://graph.org/file/d4c3e0cfdea337d761f6f.jpg"]
    SUPPORT_CHAT = "GAURAV_BOTS"
    UPDATE_CHAT = "GAURAV_BOTS"
    BOT_USERNAME = "Infinite_waifus_bot"
    CHARA_CHANNEL_ID = "-1002007169772"
    api_id = 28837889
    api_hash = "9d5e9c5b8abcf8b7b930abd259de254e"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
