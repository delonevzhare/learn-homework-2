"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
import locale
def print_days():
    dt_now = datetime.now()
    dt_yesterday = dt_now - timedelta(days=1)
    dt_30d = dt_now - timedelta(days=30)

    print("Сегодня: ", dt_now.strftime("%d/%m/%Y"))
    print("Вчера: ", dt_yesterday.strftime("%d/%m/%Y"))
    print("30 дней назад: ", dt_30d.strftime("%d/%m/%Y"))

print_days()

def str_2_datetime(date_string):
    date_format = "%d/%m/%Y %H:%M:%S"
    return datetime.strptime(date_string, date_format)

print(str_2_datetime("01/01/20 12:10:03.234567"))