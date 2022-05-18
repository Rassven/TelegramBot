﻿ru_c_base = ['рубл', 'доллар', 'евро', 'биткоин', 'эфириум']
ru_c_ends = [['ь', 'я', 'ей'], ['', 'а', 'ов'], ['', '', ''], ['', 'а', 'ов'], ['', 'а', 'а']]
inter_c_base = ['RUB', 'USD', 'EUR', 'BTC', 'ETH']
ru_c_dict = {} #{'русское': 'международное (обозначение)'}
for i in range(len(ru_c_base)):
    ru_c_dict[ru_c_base[i]+ru_c_ends[i][1]] = inter_c_base[i]

ru_greeting_mess = ["Здравствуйте! Вас приветствует Телеграм-бот. Он пока не умеет запоминать тех, с кем общался, "
                    "так что будет стандартное приветствие в начале каждого сеанса общения.",
                    "Привет еще раз. Виделись уже.", "Ничего не понял, но рад общению."]

ru_err_mess = {'input': ["Запрос ни о чем, проверьте ввод.", "Указаны более двух валют.", "Не указана исходная валюта.",
                         "Не указана конечная валюта.", "Не найдено количество исходной."],
               'conversion': ["Перевод валюты из самой в себя не имеет смысла.", "Нужна обратная конвертация?"]}

ru_help_mess = "   О боте:\n" \
               "   Бот сделан для перевода количества исходной валюты в количество конечной (по данным CryptoCompare.com).\n" \
               "   Доступные команды:\n" \
               "      /start - приветствие + данный текст," \
               "      /help - это повтор данного текста,\n" \
               "      /available - выводит список известных боту валют,\n" \
               "      /mem - повтор последнего запроса.\n" \
               "   Запрос вида <исходная валюта (наименование)> <её количество> <конечная валюта(наименование)> (не скупитесь на пробелы),\n" \
               " ответом будет число конечной валюты за заданное количество исходной.\n" \
               "   Ввод одного названия валюты - замена конечной, ввод только числа - меняет количество исходной.\n" \
               "   Вввод текста без ключевых слов и числовых значений считается ошибкой."