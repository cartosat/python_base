from telegram.ext import Updater,MessageHandler,Filters,CommandHandler
import requests

updater=Updater(token="920444593:AAGzXFDSXlLRntSeb95xJZAGTrRcW3xaAkk")

dispatcher=updater.dispatcher

def jokes(bot, update):
    req=requests.get("https://raw.githubusercontent.com/taivop/joke-dataset/master/stupidstuff.json")
    rand=random.randint(0,3770)

    joke=req.json()[rand]["category"]+"\n"+req.json()[rand]["body"]

    update.message.reply_text(joke)


dispatcher.add_handler(CommandHandler("jokes", jokes))

updater.start_polling()
updater.idle()