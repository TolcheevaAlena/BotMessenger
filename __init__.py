import telebot

VSU_bot = telebot.TeleBot('716129192:AAHlKIXNx7Y8JiQF_c5hevXMx1e7j6wTClo')
@VSU_bot.message_handler(commands=['start'])
def start_message(message):
    VSU_bot.send_message(message.chat.id, 'Привет, вот что я умею /start')

VSU_bot.polling()
