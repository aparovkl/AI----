import telebot
import tensorflow as tf
import os
from bot_logic import *  # Импортируем функции из bot_logic
from model import *

# Замени 'TOKEN' на токен твоего бота
bot = telebot.TeleBot("7671973249:AAGTt8DyvMLL9Pw2XUmmKoswFzHUuRys8yo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji или /coin  ")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_name = file_info.file_path.split('/')[-1]
    downloaded_file = bot.download_file(file_info.file_path)
    
    # Сохраняем файл в папку с проектом
    save_path = os.path.join(os.getcwd(), file_name)
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    # Вызываем функцию обработки
    result = get_class(model_path='Python Projects\KDLND Projects\AI BOT\keras_model.h5', labels_path='Python Projects\KDLND Projects\AI BOT\labels.txt', image_path=save_path)
    bot.reply_to(message, f"Результат: {result}")
# Запускаем бота
bot.polling()