"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
import datetime


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    now = datetime.date.today()
    yesterday = datetime.date.today() - datetime.timedelta(days = 1)
    mounth_ago = datetime.date.today().replace(day=1) - datetime.timedelta(days=1)
    print (now)
    print (yesterday)
    print (mounth_ago)
    
    
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    datetime_object = datetime.datetime.strptime(string, '%d/%m/%y %H:%M:%S.%f')
    return datetime_object

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
