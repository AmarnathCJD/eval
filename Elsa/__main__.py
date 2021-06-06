from Elsa import tbot, ubot, pbot
from sys import exit

try:
 tbot.start()
 ubot.start()
 pbot.start()
 print("Userbot Started!")
except:
 print("Failed to starts clients")
 exit()

tbot.run_until_disconnected()
ubot.run_until_disconnected()
