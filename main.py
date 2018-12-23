import os

from flask import Flask, request

import config
import telebot

bot = telebot.TeleBot(config.token)
server = Flask(__name__)

print(os.environ.get('URL'))
print(str(os.environ.get('URL')))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'HIII')
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route('/' + config.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://officetimetable.herokuapp.com/' + config.token)
    return "!", 200


server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
