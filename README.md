# Telegram Radio Player UserBot

A Telegram UserBot to Play Radio in Channel or Group Voice Chats.

This is also the source code of the userbot which is being used for playing
Radio in [AsmSafone](https://t.me/AsmSafone) Channel.


## Deploy to Heroku (The Easy Way)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/AsmSafone/RadioPlayer)

- Generate pyrogram session string by [String Session Generator Bot](http://t.me/genStr_robot) 
or running [genStr.py](genStr.py) by yourself on heroku run console.
- Then Enable the worker after deploy the project on Heroku Resources Tab.


## Heroku Vars

1. `API_ID` : Get From my.telegram.org
2. `API_HASH` : Get from my.telegram.org
3. `SESSION` : Generate from [@genStr robot](http://t.me/genStr_robot).
5. `CHAT_NAME` : Username of Channel/Group where the bot plays Radio.
7. `ADMIN` : ID of user who can who can control the userbot.


## Requirements

- Python 3.6 or higher.
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account.
- [FFmpeg Python](https://www.ffmpeg.org/)
- Telegram [String Session](http://t.me/genStr_robot) of the account.
- Userbot Needs To Be Admin In The Channel or Group.

## Run On VPS (The Hard Way)

```sh
$ git clone https://github.com/AsmSafone/RadioPlayer
$ cd RadioPlayer
$ sudo apt-get install ffmpeg
$ pip3 install -U pip
$ pip3 install -U -r requirements.txt
```
Edit **config.py** with your own values.

```sh
$ python3 main.py
```


## Credits

- @AsmSafone [Dev]
- @MarshalX [For tgcalls]
