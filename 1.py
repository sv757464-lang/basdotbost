import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))
zoa = 0

log = int(os.getenv('sslog'))
chat = int(os.getenv('sschat'))
id0 = int(os.getenv('ssid0'))
id1 = int(os.getenv('ssid1'))
id2 = int(os.getenv('ssid2'))

# id3 =
# id4 =
# id5 =
# id6 =
# id7 =
# id8 =
# id9 =
# id10 =
# id11 =
blackList = []
whiteList = [id0, id1, id2]
Nsubjects = 100
subjects = [0]*Nsubjects
@bot.message_handler(commands=['help'])
def help(message):
    if message.chat.id in whiteList:
        bot.send_message(message.chat.id, 'Привет! Чтобы отправить ДЗ, тебе нужно следовать инструкциям.')
        bot.send_message(message.chat.id, 'Инструкция:\n1. Нажми кнопку в меню "/send" или напиши, как команду.\n2. Выбери предмет, по которому заполняешь форму ДЗ\n3. Введи само домашнее задание.')
        bot.send_message(message.chat.id, 'Примечание: медиа/документы и (или) иные файлы прикрепляются только в комментариях поста ДЗ в ТГканале.')
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id in whiteList:
        bot.send_message(message.chat.id, 'Бот для отправления ДЗ в ТГканал (подробнее - /help):')
@bot.message_handler(commands=['send'])
def send(message):
    if message.chat.id in whiteList:
        bot.send_message(message.chat.id, 'Форма для отправления ДЗ:')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        kn1 = types.KeyboardButton('1  Алгебра')
        kn2 = types.KeyboardButton('2  Биология')
        kn3 = types.KeyboardButton('3  Вероятность и статистика')
        kn4 = types.KeyboardButton('4  География')
        kn5 = types.KeyboardButton('5  Геометрия')
        kn6 = types.KeyboardButton('6  Английский язык')
        kn7 = types.KeyboardButton('7  Немецкий язык')
        kn8 = types.KeyboardButton('8  Информатика')
        kn9 = types.KeyboardButton('9  История')
        kn10 = types.KeyboardButton('10 Литература')
        kn11 = types.KeyboardButton('11 Обществознание')
        kn12 = types.KeyboardButton('12 ОБЗР')
        kn13 = types.KeyboardButton('13 Русский язык')
        kn14 = types.KeyboardButton('14 Труд (технология)')
        kn15 = types.KeyboardButton('15 Физика')
        kn16 = types.KeyboardButton('16 Физическая культура')
        kn17 = types.KeyboardButton('17 Химия')
        markup.add(kn1, kn2, kn3, kn4, kn5, kn6, kn7, kn8, kn9, kn10, kn11, kn12, kn13, kn14, kn15, kn16, kn17)
        msg = bot.send_message(message.chat.id, 'Выберите предмет \U0001F447', reply_markup=markup)
        bot.register_next_step_handler(msg, item)
def item(message):
    global x
    a = types.ReplyKeyboardRemove()
    x = message.text[3:]
    for i in range(Nsubjects):
        if subjects[i] == 0:
            subjects[i] = str(message.chat.id) + ':' + str(x)
            break
    msg = bot.send_message(message.chat.id, 'Напишите ДЗ (\U0000261Dмедиафайлы прикрепляются отдельно, комментарием к посту\U0000261D)', reply_markup=a)
    bot.register_next_step_handler(msg, item2)

def item2(message):
    global x2
    if message.content_type == 'text':
        x2 = message.text
        zoa = 0
        for i in range(Nsubjects):
            A1 = str(subjects[i])
            A = A1.split(':', 2)
            if A[0] == str(message.chat.id):

                bot.send_message(chat, '#' + str(A[1]) + '\n' + x2)
                bot.send_message(log,
                                 '@' + str(message.from_user.username) + '\n' + str(message.chat.id) + '\n' + '#' + str(
                                     A[1]) + '\n' + str(message.text))
                subjects[i] = 0
                bot.send_message(message.chat.id, 'ДЗ отправлено успешно \U0001F60E')
                break

bot.polling(none_stop=True)