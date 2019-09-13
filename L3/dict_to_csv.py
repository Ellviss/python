"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    users=[ {'name': 'Petr', 'age': 35, 'job': 'Manager'},
            {'name': 'Alex', 'age': 30, 'job': 'Sysadmin'},
            {'name': 'Nina', 'age': 23, 'job': 'Secretary'}]
    
    with open('people.csv', 'w', encoding='utf8', newline='') as output_file:  #open file with w- wright and utf8 encode
        fc = csv.DictWriter(output_file,fieldnames=users[0].keys(),)
        fc.writeheader()    # запись ключей
        fc.writerows(users) # запись значений

if __name__ == "__main__":
    main()
