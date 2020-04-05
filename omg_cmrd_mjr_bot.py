import telebot
import os

bot = telebot.TeleBot(os.environ.get('TELEGRAM_BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я пока умею отвечать приветом на привет и говорить что делать.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	if message.text == "Привет!":
	    bot.reply_to(message, "Привет, чем я могу тебе помочь?")
	elif message.text == "/help":
	    bot.reply_to(message, "Напиши привет")
	else:
	    bot.reply_to(message, "Я тебя не понимаю. Напиши /help.")	

bot.polling(none_stop=True, interval=0)
