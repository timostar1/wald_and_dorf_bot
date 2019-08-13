from telegram.ext import Updater, CommandHandler, MessageHandler
from telegram.ext.filters import Filters


def hello(bot, update):
    print(bot)
    update.message.reply_text(
        'Hello, my friend')

def answerer(bot, update):
    update.message.reply_text('use commands, please!')


updater = Updater('907968649:AAHAwxvO6WDPoyXimEwzFdH1zEkWeIOCA78')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(MessageHandler(Filters.all, answerer))

updater.start_polling()
updater.idle()