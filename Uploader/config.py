# MIT License

# Copyright (c) 2022 Hash Minner

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    WEBHOOK = os.environ.get("BOT_TOKEN", False)
    # Get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6152226851:AAGRUrOephKbiBbNrJussdt-oFTDMWTZ_Sk")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 11652964))
    API_HASH = os.environ.get("API_HASH", "6b05881ab5b93f417d366bda9089f130")
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot

    # File /video download location
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "tandrajana916@gmail.com")
    # If deploying on vps edit the above value as example := Mega_email = "Your-Mega_email-inside-inverted-commas."

    # This is not necessary! Enter your mega password only if you have a mega.nz account with pro/business features.
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "8108125227")
    # If deploying on vps edit the above value as example := Mega_password = "Your-Mega_password-inside-inverted-commas."
    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 4194304000

    # Chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # Proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "103.148.39.42:84")

    # Set timeout for subprcess
    PROCESS_MAX_TIMEOUT = 3700

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001846073583))
    OWNER_ID = int(os.environ.get("OWNER_ID", "5299021006"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "LegionURLBot")
    ADL_BOT_RQ = {}
    AUTH_USERS = list({int(x)
                      for x in os.environ.get("AUTH_USERS", "0").split()})
    AUTH_USERS.append(OWNER_ID)
