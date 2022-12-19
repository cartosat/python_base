from telegram.ext import Updater,MessageHandler,Filters

updater=Updater(token="920444593:AAGzXFDSXlLRntSeb95xJZAGTrRcW3xaAkk")

dispatcher=updater.dispatcher

def echo(bot, update):
    update.message.reply_text(update.message.text)


dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()

#import telegram

#bot=telegram.bot("920444593:AAGzXFDSXlLRntSeb95xJZAGTrRcW3xaAkk")

#for chats in bot.getUpdates():
#   print(chats.message.text)

