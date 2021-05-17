# Telegram Radio Player UserBot

A Telegram UserBot to Play Radio in Channel or Group Voice Chats.

This is also the source code of the userbot which is being used for playing
Radio in [AsmSafone](https://t.me/AsmSafone) Channel.


## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AsmSafone/RadioPlayer)

- Generate pyrogram session string by [String Session Generator Bot](http://t.me/genStr_robot) 
or running [genStr.py](genStr.py) by yourself on heroku run console.
- Then Enable the worker after deploy the project on Heroku Resources Tab.


## Heroku Vars:

1. `API_ID` : Get From my.telegram.org
2. `API_HASH` : Get from my.telegram.org
3. `SESSION` : Generate from the owner [Doreamonfans](http://t.me/doreamonfans3.
5. `CHAT_NAME` : Username of Channel/Group where the bot plays Radio.
7. `ADMIN` : ID of user who can who can control the userbot.


## Requirements

- Python 3.6 or higher.
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account.
- [FFmpeg Python](https://www.ffmpeg.org/)
- Telegram [String Session](http://t.me/genStr_robot) of the account.

## Credits

- @doreamonfans1 [Dev]
- @doreamonfans2 [For tgcalls]
