from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from bot_command import *


updater = Updater('YOUR TOKEN HERE')

updater.dispatcher.add_handler(CommandHandler("start", hi))
updater.dispatcher.add_handler(CommandHandler("start_game", start_game))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), x_choise))


updater.start_polling()
updater.idle()

