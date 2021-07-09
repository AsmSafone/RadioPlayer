# Telegram Radio Player V3
![GitHub Repo stars](https://img.shields.io/github/stars/AsmSafone/RadioPlayer?color=blue&style=flat)
![GitHub forks](https://img.shields.io/github/forks/AsmSafone/RadioPlayer?color=green&style=flat)
![GitHub issues](https://img.shields.io/github/issues/AsmSafone/RadioPlayer)
![GitHub closed issues](https://img.shields.io/github/issues-closed/AsmSafone/RadioPlayer)
![GitHub pull requests](https://img.shields.io/github/issues-pr/AsmSafone/RadioPlayer)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/AsmSafone/RadioPlayer)
![GitHub contributors](https://img.shields.io/github/contributors/AsmSafone/RadioPlayer?style=flat)
![GitHub repo size](https://img.shields.io/github/repo-size/AsmSafone/RadioPlayer?color=red)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AsmSafone/RadioPlayer)
![GitHub](https://img.shields.io/github/license/AsmSafone/RadioPlayer)
[![Bot Support](https://img.shields.io/badge/Radio%20Player%20V2-support%20group-blue)](https://t.me/safothebot)


An Telegram Bot to Play Radio/Music/YouTube Live in Channel or Group Voice Chats.

This is also the source code of the bot which is being used for playing
Radio in [AsmSafone](https://t.me/AsmSafone) Channel & Music in [SafoTheBot](https://t.me/safothebot) Group.

## Special Features

- Playlist, queue, 24x7 radio stream
- Supports Live streaming from youtube
- Starts Radio after if no songs in playlist
- Automatic playback even if heroku restarts
- Show current playing position of the audio
- Control with buttons and commands
- Download songs from youtube as audio
- Automatically downloads audio for the first two tracks in the playlist to ensure smooth playing

## Deploy to Heroku (The Easy Way)

<p><a href="https://heroku.com/deploy?template=https://github.com/itspriyo/RadioPlayer/tree/V3.0"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>
NOTE: Make Sure You Have Started A Voice Chat In Your Channel/Group Before Deploying!

## Heroku Vars:
1. `API_ID` : Get From my.telegram.org
2. `API_HASH` : Get From my.telegram.org
3. `BOT_TOKEN` : Get it From @Botfather
4. `SESSION_STRING` : Generate From [@genStr robot](http://t.me/genStr_robot).
5. `CHAT` : ID of Channel/Group where the bot plays Music/Radio.
6. `LOG_GROUP` : Group to send Playlist, if CHAT is a Group.
7. `ADMINS` : ID of users who can use admin commands.
8. `STREAM_URL` : Stream URL of radio station or a youtube live video to stream when the bot starts or with /radio command.
9. `MAXIMUM_DURATION` : Maximum duration of song to play.(Optional)
10. `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature.
11. `ADMIN_ONLY` : Pass Y If you want to make /play commands only for admins of CHAT. By default /play is available for all.

- Enable the worker after deploy the project to Heroku.
- Bot will starts radio automatically in given `CHAT` with given `STREAM_URL` after deploy. 
- 24x7 Music even if heroku restarts, radio stream restarts automatically.  
- To play a song use /play as a reply to audio file or a youtube link or use /play [song name].
- To download audio you can use [@SafoneMusicBot](http://t.me/SafoneMusicBot) or `/song` command to the bot.
- Use `/help` to know about other commands & their usage.

## Requirements

- Python 3.6 or higher.
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account.
- [FFmpeg Python](https://www.ffmpeg.org/)
- Telegram [String Session](http://t.me/genStr_robot) of the account.
- Userbot Needs To Be Admin In The Channel or Group.
- Must Start A Voice Chat In Channel/Group Before Running The Bot.

## Run On VPS (The Hard Way)

```sh
$ git clone -b V3.0 https://github.com/AsmSafone/RadioPlayer
$ cd RadioPlayer
$ sudo apt-get install python3-pip ffmpeg
$ pip3 install -U pip
$ pip3 install -r requirements.txt
# <create variables appropriately>
$ python3 main.py
```


## License
```sh
MIT License

Copyright (c) 2021 SAF ONE

Permission is hereBy granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
## Credits

- [Me](https://github.com/AsmSafone) [Dev]
- [Dash](https://github.com/dashezup) [Dev]
- [Subin](https://github.com/subinps) [Dev]
