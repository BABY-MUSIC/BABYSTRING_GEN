from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/y9c134.jpg",
        caption=f"""❍ ʜᴇʏ  {msg.from_user.mention}  ✤,
❍ ɪ ᴀᴍ{me2},

❍ Aɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ sᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.

❍ ᴘʟᴇᴀꜱᴇ ᴄʜᴏᴏꜱᴇ ᴛʜᴇ ᴘʏᴛʜᴏɴ ʟɪʙʀᴀʀʏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ꜰᴏʀ.

❍ ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ᯓ𓆰𝅃꯭᳚ ⃪♔͢༎꯭𝝦꯭ ϒ ꯭τ ꯭ዙ ꯭𝛐፝֟֟֟͠ ꯭𝛈꯭ 𓆪꯭ 𝆺꯭𝅥⇢](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="˹ ɢᴇɴᴇʀᴀᴛᴇ sᴛʀɪɴɢ ˼", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/+OL6jdTL7JAJjYzVl"),
                    InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇs ˼", url="https://t.me/BABY09_WORLD")
                ],
                [
                    InlineKeyboardButton("˹ sᴏᴜʀᴄᴇ ˼", url="https://github.com/BABY-MUSIC/BABYSTRING_GEN"),
                    InlineKeyboardButton("˹ ᴍᴜsɪᴄ ʙᴏᴛ ˼", url="https://t.me/BABY_MUSIC09_BOT")
                ]                
            ]
        )
    )
