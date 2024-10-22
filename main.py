import config
import logging
import threading
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

def run_flask():
    flask_app.run(host='0.0.0.0', port=8000)

if __name__ == "__main__":
    print("𝚂𝚝𝚛𝚊𝚗𝚐-𝚋𝚊𝚋𝚢 𝚂𝚎𝚜𝚜𝚒𝚘𝚗 𝙶𝚎𝚗 𝚜𝚝𝚊𝚝𝚝𝚒𝚗𝚐...")
    try:
        app.start()  # Start the bot first
        
        uname = app.get_me().username
        print(f"@{uname} NOW STRING-BABY SESSION GEN IS READY TO GEN SESSION")
        
        # Start the Flask app in a separate thread
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.start()
        
        idle()  # Keep the bot running

    except ApiIdInvalid:
        raise Exception("Your API_ID is not valid.")
    except ApiIdPublishedFlood:
        raise Exception("Your API_ID/API_HASH is flood banned.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise
    finally:
        app.stop()
        print("🇸 🇪 🇸 🇸 🇮 🇴 🇳  🇬 🇪 🇳 🇷 🇦 🇹 🇮 🇳 🇬  🇸 🇹 🇴 🇵 🇵 🇪 🇩...")
