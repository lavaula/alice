import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22436694
API_HASH = "60936a5a597d2bc6205c92ced26e03d6"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8091262597:AAGReFCCq8RsEJ9gb6XUq-JPMiwoeMZEr_E"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://rupampro93:rupampro93@cluster0.dzka8gt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002500359934

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7613586638

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/NexiusUpdates"
SUPPORT_GROUP = "https://t.me/BeAkatsuki"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQGTFSMAkfBfwvqPHtpZ6YVnUlq_xPoIMXsg-Gyn-t-5w8AiI-n26xXuEikC1M7MLsqjtF6TDcuY3TK8kerlrsQF41wkYEfioNODk6m95jT1DR81o1yAxetQdQp0IrTsPePk6YHVyUKoRIpDqq1ky9bQAQ7juVArm48AyBonkoq2134B5DivtJFS-zP2HMIwl1YtfQC70h8qvDEgoDFVkcu-v8271RHpyGuEtsI2SP-zZSdy-RldFG4K4l4qUT36GQQMf02QCx0sP2ppn1b_4ywWQQIQmX7rQIj0juR2AFq7mTgAK9U5EM0hrq9fbg5fxfsuM6TeESFIcMzqNvmf9WeQuqQDnAAAAAGYRrxGAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/c3042da8d3ceed8419336-6f77f95906c2c3d079.jpg"

PING_IMG_URL = "https://graph.org/file/d215bb5e7cd426de29ff0-ac244c5f8b8cf1ea1d.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/763a841a2ad5cbb1e2fc5.jpg"
STATS_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
