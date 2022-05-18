import requests
import json
from tbot_config import ru_c_base, inter_c_base, ru_err_mess, ru_c_dict
base = ''  #русские базовые
amount = ''  #текст
target = ''  #русские базовые

class InputException(Exception):
   def __str__(self):
       pass


class Converter:
    @staticmethod
    def convert(pars):
        #tst_str = 'перевести 129 биткоинов в доллары или евро или рубли'; pars = tst_str

        words = pars.split(' ')
        fpar = []; num = -1
        for wcou in words:
            if wcou.isnumeric():
                num = float(wcou)
                break
        for checkval in ru_c_base:
            for wcou in words:
                if wcou.find(checkval) > -1:
                    fpar.append(checkval)
                    break

        #Обработка поиска
        try:
            if len(fpar) == 0 and num == -1:
                raise InputException('Ошибка.' + ru_err_mess.get('input')[0])
            if len(fpar) > 2:
                raise InputException('Ошибка.' + ru_err_mess.get('input')[1])
        except InputException as e:
            pass

        #Обработка данных
        if num > -1:
            amount = str(num)
        try:
            if len(fpar) == 1:
                if base == fpar[0]:
                    raise InputException('Ошибка.' + ru_err_mess.get('conversion')[0])
                else:
                    target = fpar[0]
            else:
                base = fpar[0]
                target = fpar[1]
        except InputException as e:
            pass

        base_ticker = inter_c_base[ru_c_base.index(base)]
        target_ticker = inter_c_base[ru_c_base.index(target)]

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={target_ticker}&tsyms={base_ticker}')
        result = float(amount) * float(json.loads(r.content)[ru_c_dict[base]])
        return result
