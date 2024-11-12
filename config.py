import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7605940903:AAHMDAVxLKvFxaG5gMM6hI7dDa9hKrz9FuU")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24935727"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3fd33336629324ecd664e9b6894f0909")

#Database 
DB_URI = os.environ.get("DB_URI", "")
