import telebot
from tbot_config import ru_c_dict, ru_greeting_mess, ru_help_mess
from tbot_token import TOKEN
from tbot_app import InputException, Converter
bot = telebot.TeleBot(TOKEN)

greet_flag = False



@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    global greet_flag
    if greet_flag:
        text = ru_greeting_mess[1]
    else:
        text = ru_greeting_mess[0] + '\n' + ru_help_mess
        greet_flag = true
    bot.reply_to(message, text)


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = ru_help_mess
    bot.reply_to(message, text)


@bot.message_handler(commands=['available'])
def available(message: telebot.types.Message):
    text = ''  #'Доступные валюты:'
    for key in ru_c_dict::
        text = '\n'.join(key[0].upper() + key[1:] + ru_c_dict[key][1])
    bot.reply_to(message, text)


@bot.message_handler(commands=['mem'])
def mem(message: telebot.types.Message):
    pars = ''
    text = Converter.convert(pars)
    bot.send_message(message.chat.id, text)
    


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    temp = message.text + ' '
    pars = temp.lower()
    text = Converter.convert(pars)
    bot.send_message(message.chat.id, text)


bot.polling(non_stop=True)
