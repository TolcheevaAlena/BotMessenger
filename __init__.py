import telebot

VSU_bot = telebot.TeleBot('716129192:AAHlKIXNx7Y8JiQF_c5hevXMx1e7j6wTClo')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Подписаться на рассылку', 'Выбрать вопрос из шаблона', 'Получить развернутый ответ на вопрос')
   
@VSU_bot.message_handler(commands=['start'])
def start_message(message):
    VSU_bot.send_message(message.chat.id, 'Привет, вот мои функции:', reply_markup=keyboard1)
    
@VSU_bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '/start':
        VSU_bot.send_message(message.chat.id, 'Привет, вот что я могу:')
    elif message.text == '/end':
        VSU_bot.send_message(message.chat.id, 'Рад был помочь.')
        
@VSU_bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'подписаться на рассылку':
        bot.send_message(message.chat.id, 'Подписка оформлена')
    elif message.text.lower() == 'Выбрать вопрос из шаблона':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

@VSU_bot.message_handler(commands=['start'])
def start_message(message):
    VSU_bot.send_message(message.chat.id, 'Привет, вот мои функции:', reply_markup=keyboard1)

@VSU_bot.message_handler(commands=['Сколько лет ВГУ?'])
def ageVSU(message):
    VSU_bot.send_message(message.chat.id, '100', reply_markup=keyboard1)
    
@VSU_bot.message_handler(commands=['Сколько корпусов ВГУ?'])
def ageVSU(message):
    VSU_bot.send_message(message.chat.id, '9', reply_markup=keyboard1)
    

VSU_bot.polling()