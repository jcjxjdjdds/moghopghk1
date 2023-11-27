import requests as s
from requests import Response
from typing import Union
from pyrogram import Client, filters
from pyrogram.types import Message
from AnonX import app


#s = Session()
@app.on_message(filters.regex(r"^(مواقيت صلاة|مواقيت صلاه|صلوات)"))
async def sendAdhan(_: Client, message: Message) -> None:
    address: str = message.text.rsplit(maxsplit=1)[-1]
    if address == "مواقيت الصلاة": return await message.reply("- اكتب اسم المنطقه بجانب الأمر،")
    adhan: Union[str, bool] = getAdhan(address)
    if not adhan: return await message.reply("- حدث خطأ أثناء جلب مواقيت الصلاة.", reply_to_message_id=message.message_id)
    await message.reply(adhan, reply_to_message_id=message.message_id)    


def getAdhan(address: str) -> Union[str, bool]:
    method: int = 1
    params = {
        "address" : address,
        "method" : method, 
        "school" : 0
    }
    res: Response = s.get("http://api.aladhan.com/timingsByAddress", params=params)
    data: dict = res.json()
    if data["code"] != 200: return print(data)
    data: dict = data["data"]
    timings: dict = data["timings"]
    date: dict = data["date"]["hijri"]
    weekday: str = date["weekday"]["ar"] + " - " + date["weekday"]["en"]
    month: str = date["month"]["ar"] + " - " + date["month"]["en"]
    date: str = date["date"]
    caption: str = f"- مـواقـيت الـصلـاة: \n    - الـفـجـر: {timings['Fajr']}\n    - الـشـروق: {timings['Sunrise']}\n    - الـظـهـر: {timings['Dhuhr']}\n    - الـعـصـر: {timings['Asr']}\n    - الـمـغـرب: {timings['Maghrib']}\n    - الـعـشـاء: {timings['Isha']}\n    - الـإمـسـاكـ: {timings['Imsak']}\n    - الـثـلـث الـأول مـن الـلـيـل: {timings['Firstthird']}\n    - مـنـتـصـف الـلـيـل: {timings['Midnight']}\n    - الـثـلـث الـأخـيـر مـن الـلـيـل: {timings['Lastthird']}"
    caption += f"\n\n- بـتـاريـخ: {date} (هـ)\n- يـوم: {weekday}\n- بـشـهـر: {month}"
    return caption

# 𝗪𝗥𝗜𝗧𝗧𝗘𝗡 𝗕𝗬 : @BENN_DEV
# 𝗦𝗢𝗨𝗥𝗖𝗘 : @BENfiles
