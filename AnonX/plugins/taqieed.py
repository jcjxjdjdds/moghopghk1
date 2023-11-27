from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from time import time
from AnonX import app
import requests



@app.on_message(filters.command("تقييد", "") & filters.group & filters.reply)
async def restric(_: Client, message: Message):
    user_id = message.from_user.id 
    chat_id = message.chat.id 
    replied = message.reply_to_message.from_user.id
    member = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={chat_id}&user_id={user_id}").json()
    if member["result"]["status"] not in ["administrator", "creator"]:
        return await message.reply("- يجب ان تكون مشرف على الاقل لإستخدام هذا الامر")
    await app.restrict_chat_member(chat_id, replied, until_date=int(time())+30, permissions=ChatPermissions(can_send_messages=False, can_send_media_messages=False, can_send_other_messages=False))
    await message.reply_to_message.reply("- تم تقييدك لمدة 30 ثانيه.")

