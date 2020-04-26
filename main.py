import telebot # импорт api бота
import api2ch # апи двача
# импорт виртуального окружения для получения токена
import os
from dotenv import load_dotenv
load_dotenv()
telegram_bot_token = os.getenv("telegram_bot_token")
print(telegram_bot_token)
#####################
bot = telebot.TeleBot(telegram_bot_token) # включение бота
#-------------------------------------------------------

# Парсинг ссылки
def link_parse(message):
    link = message.text
    link = link.split('/')
    if link[2] == "2ch.hk":
        desk = link[3]
        thread_num = link[5].split(".")[0]
        bot.send_message(message.chat.id, "Готово, даю первую картинку в треде")
        get_pic(message, desk, thread_num)
    else:
        bot.send_message(message.chat.id, "Это не двач")

#--------------------------

def get_pic(message, desk, thread_num):
    api = api2ch.DvachApi(desk)
    thread = api.get_thread(thread_num)
    pic_in_thread = []
    for post in thread:
        for file in post.files:
            pic_in_thread.append(api2ch.CHAN_URL + file.path)
    bot.send_message(message.chat.id, pic_in_thread[0])
    


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'добавить':
        bot.send_message(message.chat.id, "Добавьте ссылку на двач")
        bot.register_next_step_handler(message, link_parse)


bot.polling(none_stop=True, interval=0)