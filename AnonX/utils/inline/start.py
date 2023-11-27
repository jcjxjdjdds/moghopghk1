from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 الاوامر",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🗒 الاوامر", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺", url=f"https://t.me/T4_Mohamed"
            ),
            InlineKeyboardButton(
                text="👤 مطور البوت", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text=" ⌞ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝ ", url=f"https://t.me/T4_Mohamed"
            )
        ],
     ]
    return buttons
