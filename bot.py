import telebot
from telebot import types
import sqlite3

conn = sqlite3.connect("DBbot.db", check_same_thread=False) # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Questions ('Name' TEXT, 'Answer' TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS QuestionsForManager ('Name' TEXT, 'Detailed_Answer' TEXT)")

requesting = False

VSU_Bot = telebot.TeleBot('716129192:AAHlKIXNx7Y8JiQF_c5hevXMx1e7j6wTClo')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard = telebot.types.ReplyKeyboardMarkup()

keyboard1.row('Вопросы по шаблонам', 'Задай свои вопросы', 'Рассылка уведомлений', 'Завершить чат')
   

cursor.execute("SELECT * FROM Questions")
questions_table = cursor.fetchall()
questions = list(map(lambda x : x[0], questions_table))
desc = list(map(lambda x : x[1], questions_table))
answers = list(map(lambda x : x[2], questions_table))

q = dict(zip(questions, answers))


@VSU_Bot.message_handler(commands=['start'])
def start_message(message):
    start = """Привет! Я помогу тебе узнать ВГУ и найти полезную информацию.
Ты можешь воспользоваться актуальными вопросами и сразу получить на них ответ.
А можешь задать свой, но ответ тебе придёт не сразу.
Подписавшись на уведомления, ты сможешь получать ежедневные новости и анонсы о мероприятиях.
Надеюсь, тебе понравится!"""
    VSU_Bot.send_message(message.chat.id, start , reply_markup=keyboard1)
    
    
        
@VSU_Bot.message_handler(content_types=["text"])
def send_text(message):
    global requesting
    if(requesting):
        cursor.execute('INSERT INTO QuestionsForManager (Name) VALUES ('+message.text+')')
        conn.commit()
        VSU_Bot.send_message(message.chat.id, 'Готово!')
        
        requesting = False
    elif (message.text.lower() == 'вопросы по шаблонам'):
        spisok = "\n"+"\n"
        for i in range(len(questions)):            
            spisok += questions[i]+' - '+desc[i]+"\n"
        VSU_Bot.send_message(message.chat.id, 'Список вопросов: '+spisok)
        
    elif (message.text in questions):
        VSU_Bot.send_message(message.chat.id, q[message.text])
        
    elif (message.text.lower() == 'задай свои вопросы'):
        
        requesting = True
        VSU_Bot.send_message(message.chat.id, 'Что ты хочешь узнать о ВГУ?')
    elif (message.text.lower() == 'я тебя люблю'):
        VSU_Bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    else:
        print(str(q))
        VSU_Bot.send_message(message.chat.id, 'Извини, я тебя не понимаю...')



VSU_Bot.polling(none_stop=True, interval=0)