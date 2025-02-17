from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SACHIN_MUSIC import app
from config import BOT_USERNAME
from SACHIN_MUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - 𓆩 𝐒 𝐇 𝐔 𝐁 𝐇 𝐎 𓆪
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - sᴇᴄʀᴇᴛ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @Hey_cuties
├┤~ @about_sohini
├┤~ @shubhos_timeline
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @shubhos_timeline
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𓆩 𝐒 𝐇 𝐔 𝐁 𝐇 𝐎 𓆪", url=f"https://t.me/shubhos_timeline")
        ],
        [
          InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/shubhos_timeline"),
          InlineKeyboardButton("ʀᴇᴘᴏ", url="https://t.me/shubhos_timeline"),
          ],
               [
                InlineKeyboardButton("ɪɴᴄʀɪᴄɪʙʟᴇ ɴᴇᴛᴡᴏʀᴋ", url=f"https://t.me/shubhos_timeline"),
],
[
InlineKeyboardButton("ᴏғғɪᴄɪᴀʟ ʙᴏᴛ", url=f"https://t.me/shubhos_timeline"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/0wtv2m.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
