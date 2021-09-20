import os

secret_key = os.getenv('secret_key')
secret_token = os.getenv('secret_token')
my_idname = os.getenv('my_idname')


from Adafruit_IO import Client
aio = Client('my_idname','secret_key')

from telegram.ext import Updater, MessageHandler, Filters      

def demo1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning on')
  aio.send('bedroom-lights',1)

def demo2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning off')
  aio.send('bedroom-lights',0)

def main(bot,update):
  a= bot.message.text.lower()
  if a =="ON":
    demo1(bot,update)
  elif a =="OFF":
    demo2(bot,update)

bot_token = 'secret_token'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
