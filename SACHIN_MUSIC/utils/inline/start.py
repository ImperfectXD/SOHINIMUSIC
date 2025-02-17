from pyrogram.types import InlineKeyboardButton

import config
from SACHIN_MUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_3"],url=f"https://t.me/{app.username}?startgroup=true",)
        ],
        [
            InlineKeyboardButton(text="𝐒ᴜʙsᴄʀɪʙᴇ 𝐓ᴏ 𝐒ᴏʜɪɴɪ 💗",url=f"https://t.me/About_Sohini"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="MAIN_CP"),
        ],
        
    ]
    return buttons
