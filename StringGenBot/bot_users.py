from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID
from StringGenBot.db.users import add_served_user, get_served_users
sudo_user_id = 7400383704

@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(client: Client, msg: Message):  # 'client' argument add kiya
    await add_served_user(msg.from_user.id)
    await client.send_message(chat_id=sudo_user_id, text=f"DONE: {msg.from_user.id}")  # client instance ka use kiya

@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(client: Client, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs", quote=True)
