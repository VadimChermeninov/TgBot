import time
from background import keep_alive
import telebot
from datetime import datetime
import requests
from bs4 import BeautifulSoup as bs
import re
import os


link='https://pogoda.mail.ru/prognoz/chita/'
r=requests.get(link)
soup=bs(r.text, 'html.parser')
temp=soup.find('div', class_='information__content__temperature').getText()
temp_feel=soup.find('div', class_='information__content__additional__item').getText()
temp_feel=temp_feel.strip()
temp=temp.strip()
temperature=int(re.sub('[^0-9]','',temp))
temperature_feel=int(re.sub('[^0-9]','',temp_feel))
data=datetime.now().day



bot=telebot.TeleBot('7501965519:AAEkLXUWRGF9GPpQ1r2pA04727GUSAyj2k0')

@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "Привет, милая":
        time.sleep(2)
        bot.send_message(message.from_user.id, f'Здравствуй, дорогой) Представляешь сегодня уже {datetime.now().day} число')
        time.sleep(3)
        if temperature > 30:
            bot.send_message(message.from_user.id, f'Сегодня жарко милый, аж {temp} градусов на улице')
            time.sleep(2)
            if temperature_feel==temperature:
                bot.send_message(message.from_user.id, f'Примерно так и ощущаются, эти {temperature_feel} градусов(')
            time.sleep(2)
            if temperature_feel>temperature:
                bot.send_message(message.from_user.id, f'А ощущается вообще как все {temperature_feel} градусов(')
            else:
                bot.send_message(message.from_user.id, f'Но ощущается как будто градусов {temperature_feel}')
        else:
            bot.send_message(message.from_user.id, f'Сегодня хорошо, всего {temp} градусов на улице')
            time.sleep(2)
            if temperature_feel==temperature:
                bot.send_message(message.from_user.id, "Примерно так и ощущается, кстати)")
            else:
                bot.send_message(message.from_user.id, f'Но ощущается кстати, как {temperature_feel}')
            time.sleep(2)
        bot.send_message(message.from_user.id, "Ну а теперь, милый, введи вес молотого кофе")
        bot.register_next_step_handler(message, get_coffee)
    else:
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Это что, мне вместо "Привет, милая?)"')
        time.sleep(2)
        bot.send_message(message.from_user.id, 'Вводи вес кофе, нехороший)')
        bot.register_next_step_handler(message, get_coffee)
time.sleep(2)
def get_coffee(message):
    global coffee
    coffee=int(message.text)
    drink = round(coffee * 16.67)
    time.sleep(2)
    bot.send_message(message.from_user.id, f'Вес твоего кофе составит {drink} грамм и я уверена, оно будет горьким, как полынь, милый)')
    time.sleep(2)
    bot.send_message(message.from_user.id, ')))')
keep_alive()
bot.polling(none_stop=True, interval=0)