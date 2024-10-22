import config
import time
import logging
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from flask import Flask

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logging.getLogger("pymongo").setLevel(logging.ERROR)

# Initialize Flask app
flask_app = Flask(__name__)

# Initialize the Client
app = Client(
    "Anonymous",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="StringGenBot"),
)

@flask_app.route('/')
def home():
    return "String-Baby Session Gen is running..."

if __name__ == "__main__":
    print("𝚂𝚝𝚛𝚒𝚗𝚐-𝚋𝚊𝚋𝚢 𝚂𝚎𝚜𝚜𝚒𝚘𝚗 𝙶𝚎𝚗 𝚜𝚝𝚊𝚛𝚝𝚒𝚗𝚐...")
    try:
        app.start()
    except ApiIdInvalid:
        raise Exception("Your API_ID is not valid.")
    except ApiIdPublishedFlood:
        raise Exception("Your API_ID/API_HASH is flood banned.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

    uname = app.get_me().username
    print(f"@{uname} NOW STRING-BABY SESSION GEN IS READY TO GEN SESSION")

    # Start Flask app on port 8000
    flask_app.run(host='0.0.0.0', port=8000)

    idle()

    app.stop()
    print("🇸 🇪 🇸 🇸 🇮 🇴 🇳  🇬 🇪 🇳 🇷 🇦 🇹 🇮 🇳 🇬  🇸 🇹 🇴 🇵 🇵 🇪 🇩...")
