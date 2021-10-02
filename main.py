from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import InputMediaPhoto

# import modules
import helloworld

# token for @yourTGbot
updater = Updater('bot_key_here')

# calling a function from a module with a callback
# the logic is ("command's name", callback = module name.function name)
updater.dispatcher.add_handler(CommandHandler('helloworld', callback = helloworld.helloworld))
# add the next ones

updater.start_polling()
updater.idle()
