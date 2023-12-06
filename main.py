from env import *
import telebot 

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['info'])
def introdaction(message):
    bot.send_message(message.chat.id, "Hello this is JUST_BOT_ZEE, nice to see you here")
    
bot.polling()