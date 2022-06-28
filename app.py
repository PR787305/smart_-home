import os
key = os.getenv('key')
token1=os.getenv('token1')
token2=os.getenv('token2')

from Adafruit_IO import Client
aio = Client('PR7',f'{key}')





from telegram.ext import Updater, MessageHandler, Filters



def demo1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning on bedroom lights')
  aio.send('bedroom lights',1)
  
def demo2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning off bedroom lights')
  aio.send('bedroom lights',0)

def demo3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning on fans')
  aio.send('fans',1)

def demo4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning off fans')
  aio.send('fans',0)

def demo5(bot,update):
  chat_id  = bot.message.chat_id
  bot.message.reply_text('turning on television')
  aio.send('television',1)

def demo6(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('turning off television')
  aio.send('television',0)

def main(bot,update):
  a= bot.message.text.lower()
  if a =="turn on bedroom lights":
    demo1(bot,update)
  elif a =="turn off  bedroom lights":
    demo2(bot,update)
  elif a =="turn on fans":
    demo3(bot,update)
  elif a =="turn off fans":
    demo4(bot,update)
  elif a =="turn on television":
    demo5(bot,update)
  elif a=="turn off television": 
    demo6(bot,update)  


bot_token = f'{token1}:{token2}'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()

















