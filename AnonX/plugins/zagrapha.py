from re import findall
from html import unescape
from requests import post
from pyrogram import Client, filters
from pyrogram.types import Message
from AnonX import app

@app.on_message(filters.command("زخرفة", ""))
async def zhakhrafa(_, message: Message):
    data = message.text.split(maxsplit=1)
    if len(data) < 2: return await message.reply("- ازخرف اي؟؟", reply_to_message_id=message.message_id)
    wait = await message.reply("- جارٍ الزخرفه!", reply_to_message_id=message.message_id)
    decorated = decorator(data[1])
    text = "\n".join([f"`{text}`" for text in decorated])
    caption = f"- انتهت زخرفة {data[1]}\nاضغط على ماتريده ليتم نسخه.\n\n{text}"
    await wait.edit_text(text=caption)
    

def decorator(text: str) -> list[str]:
    cookies: dict = {
        "PHPSESSID": "4qp6upnbba034600cjohth03r6",
    }
    headers: dict = {
        'authority': 'coolnames.online',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://coolnames.online',
        'referer': 'https://coolnames.online/English-decoration',
        'sec-ch-ua': '"Chromium";v="105", "Not)A;Brand";v="8"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 12; M2004J19C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }
    data: dict = {
        'name': text,
        'get': 'english',
    }
    response: str = post('https://coolnames.online/cool.php', cookies=cookies, headers=headers, data=data).text
    decorated_tag: list = findall(r'<textarea.*?>(.*?)<\/textarea>', response)
    decorated: list = [unescape(text) for text in decorated_tag if text.strip()]
    return decorated

