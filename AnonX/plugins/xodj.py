import os
try:
  from pyrogram import Client, filters
except:
  os.system("pip install pyrogram")
  from pyrogram import Client, filters
import sqlite3

db = sqlite3.connect('rotbah.db',check_same_thread=False)
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS msgtext (chat_id TEXT, user_id TEXT)")

def add_chat_message_0text(chat_id,user_id):
  try:
    cr.execute(f"insert into msgtext (chat_id,user_id) values ('{chat_id}', '{user_id}')")
    db.commit()
    return True
  except Exception as e:
    return e

def show_chat_message_0text(chat_id,user_id):
  try:
    cr.execute(f"select * from msgtext where chat_id = '{chat_id}' and user_id = '{user_id}'")
    return cr.fetchall()
  except Exception as e:
    return e

bot_token = "***"
api_hash ="***"
api_id = ***

client = Client(name='client', bot_token=bot_token,
             api_id=api_id, api_hash=api_hash)

@client.on_message(filters.regex("^رسائلي$") & filters.group)
async def delrdood(app,message):
   await message.reply(f"-› عدد رسائلك : {len(show_chat_message_0text(message.chat.id,message.from_user.id))}")

@client.on_message(filters.text & filters.group, group=1)
async def gettt_rd(app, message):
   add_chat_message_0text(message.chat.id,message.from_user.id)

client.run()