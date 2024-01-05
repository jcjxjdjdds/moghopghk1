import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين سي ار","المطورين","مطورين","مطورين dark"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/6ccfb45597628a287bbc8.jpg",
        caption=f"""⌞𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺⌝**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين دارك ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙳𝙰𝚁𝙺َّّ ", url=f"https://t.me/T4_Mohamed"), 
                 ],[
                    InlineKeyboardButton(
                        "𝑻𝑾𝑰𝑵𝑺𓆪 َِ𝆹𝅥𝅮™𝙢𝙖𝙧𝙨𝙝𝙢𝙚𝙡𝙡𝙤 ⃝🇬🇧➼", url=f"https://t.me/AL_G_A_D_A_R_A2"),
                ],[
                    InlineKeyboardButton(
                        "مـًٌٍّ̨̥̬̩ـمـ༈ۖ҉ـآرٍشـًٌٍّ̨̥̬̩ـمـًٌٍّ̨̥̬̩ـيلُـِـِِـِِِؤ❾ فـ༈ۖ҉ـء", url=f"https://t.me/Marshmello_x_x"),
                    InlineKeyboardButton(
                        "سورس القناه", url=f"https://t.me/S_MA4"),
                ],[
                
                    InlineKeyboardButton(
                        "⌞𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺⌝", url=f"https://t.me/P1PPIP"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["مطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("T4_Mohamed")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["دارك"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("T4_Mohamed")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["تونز"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("AL_G_A_D_A_R_A2")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["مارش"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("Marshmello_x_x")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━⊶★━⩺\n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ee5511d9d2d10b09cb9e8.jpg",
        caption=f"""⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝*\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس dark\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙳𝙰𝚁𝙺", url=f"https://t.me/T4_Mohamed"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝⚡", url=f"https://t.me/T4_Mohamed"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/ee5511d9d2d10b09cb9e8.jpg",
        caption=f"""**⩹⊷━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس dark\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝙳𝙰𝚁𝙺", url=f"https://t.me/T4_Mohamed"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  𝚂𝙾𝚄𝚁𝙲𝙴 𝙳𝙰𝚁𝙺 ⌝⚡", url=f"https://t.me/T4_Mohamed"),
                ],

            ]

        ),

    )



    
