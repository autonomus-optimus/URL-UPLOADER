from flask import Flask
from pyrogram import Client
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'


if __name__ == "__main__":
    

    API_ID = 11652964
    API_HASH = "0123456789abcdef0123456789abcdef"
    BOT_TOKEN = "6152226851:AAGRUrOephKbiBbNrJussdt-oFTDMWTZ_Sk"

    app = Client(
        "my_bot",
        API_ID=API_ID, API_HASH=API_HASH,
        BOT_TOKEN=BOT_TOKEN
    )
    app.run()
