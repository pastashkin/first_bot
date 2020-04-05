import telebot
import os

bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message, "Привет! Я пока умею отвечать приветом на привет и говорить что делать.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == "Привет!":
	    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
	elif message.text == "/help":
	    bot.send_message(message.from_user.id, "Напиши привет")
	else:
	    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")	

bot.polling(none_stop=True, interval=1)
