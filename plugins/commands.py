"""
RadioPlayer, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import sys
import signal
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import USERNAME, FFMPEG_PROCESSES, mp
from config import Config

CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "👋🏻 **Hi Dude [{}](tg://user?id={})**,\n\nI'm **CS MUSIC BOT 💥😉** \nI Can Play Radio / Music / YouTube Live In Channel & Group 24x7 Nonstop. Made with ❤️ By @iAmLiKu1 😉!"
HELP_TEXT = """
🎧 **Need Help ?** 
__(Join @@seriesprovider1 For Support)__

🏷️ **Common Commands** :

\u2022 `/play` - reply to an audio or youTube link to play it or use /play [song name]
\u2022 `/help` - shows help for commands
\u2022 `/playlist` - shows the current playlist
\u2022 `/current` - shows playing time of current track
\u2022 `/song` [song name] - download the song as audio track

🏷️ **Admin Commands** :

\u2022 `/skip` [n] - skip current or n where n >= 2
\u2022 `/join` - join the voice chat
\u2022 `/leave` - leave the voice chat
\u2022 `/stop` - stop playing music
\u2022 `/radio` - start radio stream
\u2022 `/stopradio` - stop radio stream
\u2022 `/replay` - play from the beginning
\u2022 `/clean` - remove unused RAW PCM files
\u2022 `/pause` - pause playing music
\u2022 `/resume` - resume playing music
\u2022 `/mute` - mute the vc userbot
\u2022 `/unmute` - unmute the vc userbot
\u2022 `/restart` - restart the bot

© **Powered By** : 
**iAmLiKu1 | @iAmLiku1** 👑
"""


@Client.on_message(filters.command(["start", f"start@{USERNAME}"]))
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton("CHANNEL 💥", url="https://t.me/mod_apk_premium_cs"),
                InlineKeyboardButton("SUPPORT 😉", url="https://t.me/seriesprovider1"),
            ],
            [
                InlineKeyboardButton("💫OWNER 👑", url="https://t.me/iAmLiKu1"),
                InlineKeyboardButton("FOLLOW ME 🤗", url="https://instagram.com/liku__cs?utm_medium=copy_link"),
            ],
            [
                InlineKeyboardButton("❔ HOW TO USE ❔", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply_photo(photo="https://telegra.ph/file/2af51be858db592dca309.jpg", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await message.delete()



@Client.on_message(filters.command(["help", f"help@{USERNAME}"]))
async def show_help(client, message):
    buttons = [
            [
                InlineKeyboardButton("CHANNEL 💥", url="https://t.me/mod_apk_premium_cs"),
                InlineKeyboardButton("SUPPORT 😉", url="https://t.me/seriesprovider1"),
            ],
            [
                InlineKeyboardButton("💫OWNER 👑", url="https://t.me/iAmLiKu1"),
                InlineKeyboardButton("FOLLOW ME🤗", url="https://instagram.com/liku__cs?utm_medium=copy_link"),
            ],
            [
                InlineKeyboardButton("CLOSE 🔐", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_photo(photo="https://telegra.ph/file/2af51be858db592dca309.jpg", caption=HELP_TEXT, reply_markup=reply_markup)
    await message.delete()
@Client.on_message(filters.command(["restart", f"restart@{USERNAME}"]) & filters.user(Config.ADMINS) & (filters.chat(CHAT) | filters.private))
async def restart(client, message):
    await message.reply_text("🔄 **Restarting... @iAmLiKu1**")
    await message.delete()
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        process.send_signal(signal.SIGTERM) 
    os.execl(sys.executable, sys.executable, *sys.argv)
    
