# Just change the info below and rename this file to config.py

from pyrogram import filters

API_ID = 1383845
API_HASH = "0e3d2c299cc3c5cc26c283cecd2eb97c"
TOKEN = "1474570701:AAH-fVS4OM5yHpePfEpnXD145xzSFW4NUxc"
SUDO_USERS = [
    1131653685,
]
LOG_GROUP = None # Just keep it like this if you are not going to use one

# No need to touch this
SUDO_FILTER = filters.user(SUDO_USERS)
