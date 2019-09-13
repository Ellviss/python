"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""
import urllib.request


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    url = 'https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0'
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8')
    print (text)
    len_text= len(text)
    print (len_text)
    len_words= len(text.split(' '))
    print(len_words)
    new_text = text.replace('.','!')
    print (new_text)
    f = open( 'referat2.txt', 'w' )
    f.write(new_text)
    f.close()

if __name__ == "__main__":
    main()
