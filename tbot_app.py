import requests
import json
from tbot_config import ru_c_dict, ru_err_mess, ru_greeting_mess
from tbot_main import bot
err_message = ''


class UserException(Exception):
   def __init__(self, r_str):
       global err_message
       err_message = 'Ошибка!' + r_str


class Converter:
    @staticmethod
    def convert(pars):
        #tst_str = 'эфириум перевести в 129 биткоинов и доллары или евро или рубли'; pars = tst_str
        
        global err_message, base, target, amount
        if pars == '':  #команда mem
            pars = base + ' ' + target + ' ' + amount
        words = pars.split()
        fpar = []; num = -1
        for wcou in words:
            if wcou.isnumeric():
                num = float(wcou)
                break
        for wcou in words:
            for check_val in ru_c_dict:
                if wcou.find(check_val) > -1:
                    fpar.append(check_val)
                    break

        #Обработка поиска
        if len(words) > 3 and len(fpar) == 0:
            bot.reply_to(message, ru_greeting_mess[2])
        try:
            if len(fpar) == 0 and num == -1:
                raise UserException(ru_err_mess.get('input')[0])
            if len(fpar) > 2:
                raise UserException(ru_err_mess.get('input')[1])
        except UserException:
            bot.reply_to(message, err_message)
        try:
            if amount == '' and num < 0:
                raise UserException(ru_err_mess.get('Input')[4])
        except UserException:
            bot.reply_to(message, err_message)

        #Обработка данных
        if num > -1:
            amount = str(num)
        try:
            if len(fpar) == 1:
                if base == fpar[0]:
                    raise UserException(ru_err_mess.get('conversion')[0])
                else:
                    target = fpar[0]
            else:
                base = fpar[0]
                target = fpar[1]
        except UserException:
            bot.reply_to(message, err_message)
        
        #сборка
        base_ticker = ru_c_dict[base][0]
        target_ticker = ru_c_dict[target][0]
        
        #Запрос: fsym=USD&tsyms=RUB, ответ: {"RUB": 63.93}
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={target_ticker}')
        result = float(amount) * json.loads(r.content)[target_ticker]
        ending = 2
        result_text = f'Стоимость {amount} {base + ru_c_dict[base][ending]} составляет {result} {target + ru_c_dict[target][ending]}'
        return result_text
