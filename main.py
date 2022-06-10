import telebot
import sqlite3
from telebot import types

bot = telebot.TeleBot('5501931977:AAF_fIoOhSgGaEwrin38Cys_yi6xs8Vql0M')

connect = sqlite3.connect('Questions.db', check_same_thread=False)
cursor = connect.cursor()


def add_info(user_id: int, user_name: str, user_surname: str, username: str):
    cursor.execute('INSERT INTO Users_questions (user_id, user_name, user_surname, username) '
                   'VALUES (?, ?, ?, ?)',
                   (user_id, user_name, user_surname, username))
    connect.commit()


def get_question(message):
    people_id = message.from_user.id
    cursor.execute(f"SELECT user_id FROM Users_questions WHERE user_id ={people_id}")
    data = cursor.fetchone()
    if data is None:
        us_id = message.from_user.id
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        username = message.from_user.username
        add_info(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

        bot.send_message(message.chat.id,
                     'Ми отримали ваш запит. Найближчим часом з вами сконтактує наш представник, щоб'
                     'вирішити ваше питання. Якщо хочете дізнатися відповідь на інше запитання, напишіть'
                     ' команду /start')
    else:
        bot.send_message(message.chat.id, "Ви вже відправляли запит. Чекайте відповіді або можете ще раз переглянути "
                         "типові питання написавши /start")

@bot.message_handler(commands=['start'])
def start(message):
    case_student = types.KeyboardButton('Студент')
    case_partner = types.KeyboardButton('Роботодавець / Партнер')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(case_student, case_partner)

    bot.send_message(message.chat.id, 'Цей бот має на меті відповісти на ваші запитання. Для початку введіть хто ви:'
                                      ' Студент чи Роботодавець / Партнер?', reply_markup=markup)


@bot.message_handler(regexp='Студент')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('Як взяти участь в IT School/Sales School/будь-якому проєкті STUD-POINT?')
    button2 = types.KeyboardButton('Як купити відеокурси STUD-POINT і скільки вони коштують?')
    button3 = types.KeyboardButton('Ви отримали моє резюме, хочу працювати у вас?')
    button4 = types.KeyboardButton(
        'Я економіст/копірайтер/дизайнер/будь-хто, які вакансії ви можете мені запропонувати?')
    button5 = types.KeyboardButton('Мого питання немає серед переліку')

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)

    bot.send_message(message.chat.id, 'Оберіть ваше питання:', reply_markup=markup)

    @bot.message_handler()
    def get_text(message):
        if message.text == 'Як взяти участь в IT School/Sales School/будь-якому проєкті STUD-POINT?':
            bot.send_message(message.chat.id, 'підпис тут: https://www.instagram.com/studpoint/ і підпис тут: '
                                              'https://web.telegram.org/k/ Там актуальні новини від STUD-POINTу, '
                                              'цікаві івенти, проєкти та багато цікавинок 😊. Доєднуйся, бо на тебе вже '
                                              'очікують 😉')
        elif message.text == 'Як купити відеокурси STUD-POINT і скільки вони коштують?':
            bot.send_message(message.chat.id,
                             'крок 1: відкрий сайт STUD-POINTу; крок 2: якщо знайшов кнопку «курси» зверху,'
                             ' то клацни на неї; при успішному проходженні цих кроків, тобі відкриється '
                             'світ актуальних відеокурсів з детальним описом, цінами та найголовніше, '
                             'вигідними пропозиціями. Або не мороч собі голову і перейди за цим '
                             'покликанням: https://stud-point.com/video-courses/ ')
        elif message.text == 'Ви отримали моє резюме, хочу працювати у вас?':
            bot.send_message(message.chat.id,
                             'Для відповіді на це питання, зв’яжись зі STUD-POINTом через нашого іншого '
                             'бота: https://web.telegram.org/k/. Оператори зконтактують з тобою найближчим '
                             'часом')
        elif message.text == 'Я економіст/копірайтер/дизайнер/будь-хто, які вакансії ви можете мені запропонувати?':
            bot.send_message(message.chat.id,
                             'Ми тут лишимо покликаннячко тобі https://stud-point.com/blog/vakansiyi/, '
                             'тут ти можеш підібрати найкращу вакансію під своє резюме) Слідкуй за '
                             'оновленнями та нехай удача завжди буде з тобою 😉')
        else: get_question(message)


@bot.message_handler(regexp='Роботодавець / Партнер')
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('Як і на яких умовах розмістити у вас вакансію/анонс/інформацію?')
    button2 = types.KeyboardButton('Які слоти на публікацію у вас є і чи можна опублікувати комерційне просто зараз?')
    button3 = types.KeyboardButton('Як взяти участь в IT School/Sales School/будь-якому проєкті STUD-POINT?')
    button4 = types.KeyboardButton('Як купити відеокурси STUD-POINT і скільки вони коштують?')
    button5 = types.KeyboardButton('Хочемо взяти участь у проєкті, щоб закрити вакансії та посилити бренд '
                                   'роботодавця, які івенти заплановані на найближчий час?')
    button6 = types.KeyboardButton('Мого питання немає серед переліку')

    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    markup.add(button6)

    bot.send_message(message.chat.id, 'Оберіть ваше питання:', reply_markup=markup)

    @bot.message_handler()
    def get_text(message):
        if message.text == 'Як і на яких умовах розмістити у вас вакансію/анонс/інформацію?':
            bot.send_message(message.chat.id, 'Комплексні послуги для роботодавців включають в себе 4 пакети '
                                              'послуг: “Basic”, “Optimal”, “Premium”, “Platinum”. Для детальнішої '
                                              'інформації ознайомтесь, будь ласка, за цим покликанням: '
                                              'https://www.canva.com/design/DAD7Sr3yGE8/TOO6wZGuClG1v9PIGs1sPQ/'
                                              'view?utm_content=DAD7Sr3yGE8&utm_campaign=designshare&utm_medium='
                                              'link&utm_source=sharebutton#1')
        elif message.text == 'Які слоти на публікацію у вас є і чи можна опублікувати комерційне просто зараз?':
            bot.send_message(message.chat.id,
                             'Через декілька хвилин Вам напише менеджер щодо нашого контент плану та ми оберемо '
                             'зручний для вас час.')
        elif message.text == 'Як взяти участь в IT School/Sales School/будь-якому проєкті STUD-POINT?':
            bot.send_message(message.chat.id,
                             'Актуальну інформацію розміщено на таких платформах як інстаграм https://www.instagram.'
                             'com/studpoint/, фейсбук https://www.facebook.com/studpoint.ua та телеграм '
                             'https://web.telegram.org/k/')
        elif message.text == 'Як купити відеокурси STUD-POINT і скільки вони коштують?':
            bot.send_message(message.chat.id,
                             'При переході за покликанням https://stud-point.com/video-courses/ , відкриється '
                             'інформація про актуальні курси, інформацію про них та ціни з вигідними пропозиціями')
        elif message.text == 'Хочемо взяти участь у проєкті, щоб закрити вакансії та посилити бренд ' \
                             'роботодавця, які івенти заплановані на найближчий час?':
            bot.send_message(message.chat.id, 'STUD-POINT надає можливість для розвитку бренду роботодавця та надає '
                                              'такі послуги як рекламна кампанія для Вашої цільової авдиторії та '
                                              'реалізація індивідуальних кар’єрних подій на замовлення. Для детальнішої '
                                              'інформації ознайомтесь, будь ласка, за цим покликанням: '
                                              'https://www.canva.com/design/DAD6o7QqjTs/nSYcK-UKozTWBJ5QGmga7A/view#4 ')
        else: get_question(message)


@bot.message_handler(commands=['delete'])
def delete_data(message):
    cursor.execute("DELETE FROM Users_questions")
    connect.commit()


bot.infinity_polling()
