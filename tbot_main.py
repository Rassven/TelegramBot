import telebot
from tbot_config import ru_c_base, ru_c_ends, ru_greeting_mess, ru_help_mess
from tbot_token import TOKEN
from tbot_app import InputException, Converter
bot = telebot.TeleBot(TOKEN)

greet_flag = False
base = '' #русские базовые
amount = '' #текст
target = '' #русские базовые


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = ru_greeting_mess[0] + '\n' + ru_help_mess
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = ru_help_mess
    bot.reply_to(message, text)


@bot.message_handler(commands=['available'])
def available(message: telebot.types.Message):
    text = ''  #'Доступные валюты:'
    for i in range(len(ru_c_base)):
        text = '\n'.join((text, ru_c_base[i]+ru_c_ends[i][0]))
    bot.reply_to(message, text)


@bot.message_handler(commands=['mem'])
def mem(message: telebot.types.Message):
    pars = base + amount + target
    result = Converter.convert(pars)
    text = f'Цена {base} {amount} в {target} = {result}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    pars = message.text
    result = Converter.convert(pars)
    text = f'Цена {base} {amount} в {target} = {result}'
    bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)
