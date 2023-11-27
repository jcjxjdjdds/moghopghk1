from pyrogram import Client, filters
from pyrogram.types import ChatPermissions #ChatPrivileges
import asyncio, requests 
from AnonX import app
#by > @PROGRAMMER_TOM / @BENN_DEV

welcome_enabled = True

@app.on_chat_member_updated(group=277)
async def welcome(client: Client, chat_member_updated):
    if not welcome_enabled:
        return
    print(chat_member_updated.new_chat_member.status)
    if chat_member_updated.new_chat_member.status == "banned":
        kicked_by = chat_member_updated.new_chat_member.restricted_by
        user = chat_member_updated.new_chat_member.user
        
        if kicked_by is not None and kicked_by.is_self:
            message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة بواسطة البوت"
        else:
            if kicked_by is not None:
                message = f"• المستخدم [{user.first_name}](tg://user?id={user.id}) \n• تم طرده من الدردشة بواسطة [{kicked_by.first_name}](tg://user?id={kicked_by.id})\n• ولقد طردته بسبب هذا"
                try:
                    await client.ban_chat_member(chat_member_updated.chat.id, kicked_by.id)
                except Exception as e:
                    message += f"\n\nعذرًا، لم استطع حظر الإداري بسبب: {str(e)}"
            else:
                message = f"• المستخدم {user.username} ({user.first_name}) تم طرده من الدردشة"
            
            
        
        await client.send_message(chat_member_updated.chat.id, message)


@app.on_message(filters.command("رفع مشرف", "") & filters.group)
async def promote_g_admin(client: Client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = await app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = await app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            await message.reply_text("لا يمكن العثور على المستخدم")
            return

    tom_id = message.from_user.id
    chat_id = message.chat.id
    toom = requests.get(f"https://api.telegram.org/bot{app.bot_token}/getChatMember?chat_id={chat_id}&user_id={tom_id}").json()
    if (toom["result"]["status"] == "creator" or toom["result"]["status"] == "administrator"):
        await client.promote_chat_member(chat_id, user_id, can_invite_users=True, can_pin_messages=True, can_delete_messages=True)
        await message.reply(f"تم رفع {user_id} ادمن بنجاح")
    else:
        await message.reply("يجب ان تكون مشرف لإستخدام الامر")
	 
