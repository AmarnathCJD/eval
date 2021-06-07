from telethon import TelegramClient
from pyrogram import Client
from telethon.sessions import StringSession

OWNER_ID = int(1743998809)
BOT_TOKEN = "1822801497:AAGVZ2MkfNPDrTm9MY5vXalC8dM92ccBKNE"
API_KEY = 1822414
API_HASH = "46f1888d3f68396bad08c92ac4d7f00a"
TL_STRING = "1BVtsOHcBuwX-oDpd9cAmJnSYYuxVxIZp0-t2dGqofrI9fPIpvfWAkDHEAbAlBtyM63TPW3d9F7tYQ5HmvhPkEeELOpxdHorZzNFUWkKHOrgjwyOENYiVGQ5L1siHAyN_JlhtyLYr76kZtOnE70Kihsz9JPZ_Z7XziC_5HBQE1c00alBK7Otd56ce2lMazGBORZF3FIIc1v9fuUjG4TFxtY81379SgP380b0cDISFSjoAc6ml-AHh_r84zVRunRJ4Z-aSiraqoClsO5rZCafM4FvDUkSTHNGRItkarPiNJfTZK8VrY1EJUWMqbAu_py2xNOXERVhd3Ys1I8onyQaGhN2KMYk7Dfg="
tbot = TelegramClient(StringSession(TL_STRING), API_KEY, API_HASH, bot_token=TOKEN
ubot = TelegramClient(None, API_KEY, API_HASH)
pbot = Client("Evelyn", bot_token=TOKEN, api_id=API_KEY, api_hash=API_HASH)
