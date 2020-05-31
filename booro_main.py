import telebot # импорт api бота
from telebot.types import Message
from telebot import types
from telebot.types import InputMediaPhoto
import requests
import json
import time
# импорт виртуального окружения для получения токена
import os
from dotenv import load_dotenv
load_dotenv()
telegram_bot_token = os.getenv("telegram_bot_token")
CHANNEL_NAME = '@ecchi_konachan'
print(telegram_bot_token)
#####################
bot = telebot.TeleBot(telegram_bot_token) # включение бота

#-------------------------------------------------------

urls = [
    "https://konachan.com/post.json?limit=10"
    ]

def scan():
    while True:
        f = open('id.txt', 'r+')
        id = f.read()
        get = requests.get(urls[0])
        get = get.json()
        text = []
        for i in range(0, 10):
            if( int(get[i]["id"]) > int(id) ):
                print(get[i]["id"])
                try:
                    bot.send_photo(CHANNEL_NAME, get[i]["jpeg_url"])
                except:
                    pass
                
        f.seek(0)
        f.write(str( int(get[0]["id"]) ))
        f.close()
                

        
        time.sleep(6)



def start():
    f = open('id.txt', 'r+')
    string = f.read()
    print(string)
    f.seek(0)
    f.write("1234612ds5")
    f.close()
    f = open('id.txt', 'r+')
    string = f.readline()
    print(string)
    f.close()
        

def send_post():
    get = requests.get(urls[0])
    get = get.json()
    text = []
    for i in range(0, 10):
        print(get[i]["jpeg_url"])
        bot.send_photo(CHANNEL_NAME, get[i]["jpeg_url"])


scan()
bot.polling(none_stop=True, interval=0)