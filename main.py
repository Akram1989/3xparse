import requests
from bs4 import BeautifulSoup
import time
import symbols
import telebot
from telebot import types

TOKEN = '1074823668:AAGxy_dkcrwXz9ckLrL_Yz10tez2h_bD67c'

bot = telebot.TeleBot(TOKEN)
r = bot.get_me()
print("@" + r.username)

@bot.message_handler(commands=["start"])
def wellcome(message):
    bot.send_message(message.chat.id, "Ассалом алейкум, введите пароль")
    bot.register_next_step_handler(message, password)

def password(message):
    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(True, True)
    keyboard.row('Начать цикл')
    keyboard.row('Остановить')
    if message.text == 'oy5752757':
            bot.register_next_step_handler(message, password)
            bot.send_message(message.chat.id, "Доступ открыт", reply_markup=keyboard)
            bot.register_next_step_handler(message, starting)
    else:
            bot.send_message(message.chat.id, "Пароль не верный, повторите попытку")
            bot.register_next_step_handler(message, password)

def starting(message):
    chat_id = message.chat.id
    if message.text == 'Начать цикл':
        parse(message)
    elif message.text == 'Остановить':
        bot.register_next_step_handler(message, wellcome)


def parse(message):
      while True:
        for item in symbols.domain_name:
              BASE_URL = f'https://m.cctld.uz/whois/?domain={item}&zone=uz&sub=%D0%9F%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D1%82%D1%8C'
              try:
                  page = requests.get(BASE_URL)
                  soup = BeautifulSoup(page.content, "html.parser")
                  chto = []
                  msg = soup.find('div', 'leftext')
                  chto.append(msg)
                  result = [c for c in chto[0]]
                  resa = (result[3].string, result[7].string, result[19].string)
                  resb = result[0].string
                  if result[7].string.find('Статус: Активный')==-1:
                    bot.send_message(message.chat.id, result[3])
                    bot.send_message(message.chat.id, result[7])
                    bot.send_message(message.chat.id, result[19])
              except IndexError:
                    bot.send_message(message.chat.id, result[0].string)
                    print(resb)
        break


bot.polling(none_stop=True)

