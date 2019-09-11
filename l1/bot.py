#bot 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
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
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    if user_text == 'blablabla':
        update.message.reply_text('Я не говорю блаблабла')
    else:
        update.message.reply_text(user_text)    
def info_user(bot,update):
    text='Hello: '+update['message']['chat']['username']+'! Welcome to telegramm '
    update.message.reply_text(text)
def main():
    mybot = Updater("тут апи кей",request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("info", info_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()
main()