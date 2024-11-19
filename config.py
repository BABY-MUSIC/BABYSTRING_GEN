from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","16457832"))
API_HASH = getenv("API_HASH","3030874d0befdb5d05597deacc3e83ab")
BOT_TOKEN = getenv("BOT_TOKEN", "7015056498:AAFaPW1VAfUH_xpEowOp5yacHOgu4y1mjoI")
OWNER_ID = int(getenv("OWNER_ID","7400383704"))

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://vivek:1234567890@cluster0.c48d8ih.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MUST_JOIN = getenv("MUST_JOIN","BABY09_WORLD")
