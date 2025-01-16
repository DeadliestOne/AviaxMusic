from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram.enums import ParseMode
from AviaxMusic import app
import config

TEXT = f"""
**ᴘʀɪᴠᴀᴄʏ ᴘᴏʟɪᴄʏ ғᴏʀ {app.mention} !! 

ɪғ ʏᴏᴜʀ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴏʀ ᴄᴏɴᴄᴇʀɴs ғᴇᴇʟ ғʀᴇᴇ ᴛᴏ ʀᴇᴀᴄʜ ᴏᴜᴛ ᴛᴏ ᴏᴜʀ [sᴜᴘᴘᴏʀᴛ ᴛᴇᴀᴍ](t.me/BeAkatsuki)  ᴏʀ ᴍᴇ @evyto !!**"""

@app.on_message(filters.command("privacy"))
async def privacy(client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "𝑝𝑟𝑖𝑣𝑎𝑐𝑦 𝑝𝑜𝑙𝑖𝑐𝑦", url="https://telegra.ph/Privacy-Policy-for-01-10"
                )
            ]
        ]
    )
    await message.reply_text(
        TEXT, 
        reply_markup=keyboard, 
        parse_mode=ParseMode.MARKDOWN, 
        disable_web_page_preview=True
    )

