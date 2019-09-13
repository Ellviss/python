#Задание
#Установите модуль ephem
import ephem
import datetime as dt   
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


date = dt.datetime.today().strftime("%m/%d/%Y")
#Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском, например /planet Mars
#bot 
PROXY = {'proxy_url': 'socks5://t3.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text='Вызван /start'
    print (update)
    print(text)
    update.message.reply_text(text)


def planet(bot,update):
    update.message.reply_text ('Try print /planet Name_of_Planet')
    user_text = (update.message.text.split())
    print(user_text)
    planets=[name for _0, _1, name in ephem._libastro.builtin_planets()]
    planet = capitalize(user_text[-1])
    command= user_text[0]
    if command='/planet' and planet in planets :
        u = ephem.getattr(ephem, planet)()
        u.compute(date)
        cons=(ephem.constellation(u))
        update.message.reply_text(planet+' in '+cons)            
    else:
        update.message.reply_text('Its not a planet - '+planet)


def main():
    mybot = Updater("тут апи кей",request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, planet))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()                       
#В функции-обработчике команды из update.message.text получите название планеты (подсказка: используйте .split())
#При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.
#planet= input('Введите планету? ')
#planets=[name for _0, _1, name in ephem._libastro.builtin_planets()]
#print (planets)
#if planet in planets:
#    u = ephem.Mars() ? How set variable to this method
#    u.compute(date)
#    print(ephem.constellation(u))
