# AsmSafone
# Radio Player
# Join @disneygrou


# import logging
from pyrogram import Client, idle

app = Client("RadioPlayer")
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED. JOIN @disneygrou')
idle()
app.stop()
print('\n>>> USERBOT STOPPED. JOIN @disneygrou')
