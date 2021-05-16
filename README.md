# Telegram Radio Player UserBot

A Telegram UserBot to Play Radio in Voice Chats.

This is also the source code of the userbot which is being used for playing
Radio in [AsmSafone](https://t.me/AsmSafone) Channel.


## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AsmSafone/RadioPlayer)

- Generate Pyrogram session string by running [genStr.py](genStr.py) by yourself.
- Enable the worker after deploy the project to Heroku.


## Heroku Vars:

1. `API_ID` : Get From my.telegram.org
2. `API_HASH` : Get from my.telegram.org
3. `SESSION` : Generate by running [genStr.py](genStr.py) by yourself.
5. `CHAT_NAME` : Username of Channel/Group where the bot plays Radio.
7. `ADMIN` : ID of user who can who can control the userbot.


## Requirements

- Python 3.6 or higher
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account
- [FFmpeg](https://www.ffmpeg.org/)

## Credits

- @AsmSafone [Dev]
- @MarshalX [For tgcalls]
