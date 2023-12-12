import requests
import json
import os
import time
import telebot

api_token = "5929009539:AAG18NDhJ8JzMnh-Kx64Ne0qAq3EG2OI91w"
bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'جاريً إحضار مواقيت الصلاة ... ')
    response = requests.get('https://eros.dstor.space/api/apiR.php?city=cairo')
    json_data = json.loads(response.text)
    times = json_data['times']
    info = json_data['info'].splitlines()[:7]
    azan = json_data['azan']
    sent_message = bot.send_message(chat_id, f'{times}\n{os.linesep.join(info)}\n{azan}')
    message_id = sent_message.message_id

    while True:
        try:
	        response = requests.get('https://eros.dstor.space/api/apiR.php?city=cairo')
	        json_data = json.loads(response.text)
	        new_times = json_data['times']
	        new_info = json_data['info'].splitlines()[:2] + json_data['info'].splitlines()[3:7] 
	        new_azan = json_data['azan']
	        if times != new_times or info != new_info or azan != new_azan:
	            times, info, azan = new_times, new_info, new_azan
	            bot.edit_message_text(f'{times}\n{os.linesep.join(info)}\n{azan}', chat_id, message_id)
	        time.sleep(0.00001)
        except telebot.apihelper.ApiTelegramException:
         time.sleep(1)
	              
bot.polling()
