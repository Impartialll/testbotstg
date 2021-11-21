# name of bot 'miketester_bot'

import telebot
import config

bot = telebot.TeleBot(config.config['token'])

@bot.message_handler(commands = ['start'])
def get_text(message):
    bot.send_message(message.id, 'Hello, my name is Mike!\nAnd what do you want?')

@bot.message_handler(text = ['calc'])
def get_text(message):
    if commands.text == ''
        bot.send_message(message.chat.id, message.text*100)
bot.polling(none_stop = True, interval = 0)