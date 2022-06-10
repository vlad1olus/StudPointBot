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
#
# # @bot.message_handler(commands=['start'])
# # def start (message):
# #     connect = sqlite3.connect('Questions.db', check_same_thread=False)
# #     cursor = connect.cursor()
# #
# #     def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
# #         cursor.execute('INSERT INTO Users_questions (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
# #                        (user_id, user_name, user_surname, username))
# #         connect.commit()
# #
# #     us_id = message.from_user.id
# #     us_name = message.from_user.first_name
# #     us_sname = message.from_user.last_name
# #     username = message.from_user.username
# #
# #     db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)
# #
# # @bot.message_handler(commands=['delete'])
# # def delete(message):
# #
# #     connect = sqlite3.connect('users.db')
# #     cursor = connect.cursor()
# #
# #     people_id = message.chat.id
# #     cursor.execute(f"DELETE FROM login_id WHERE id = {people_id}")
# #     connect.commit()
#
# # Just a Message
# # @bot.message_handler(commands=['start'])
# # def start(message):
# #     bot.send_message(message.chat.id, 'Hello')
#
#
# # With name
# # @bot.message_handler(commands=['start'])
# # def start(message):
# #    mess = f'Hello, {message.from_user.first_name}'
# #    bot.send_message(message.chat.id, mess)
#
# # answer on any message
# # @bot.message_handler()
# # def get_user_text(message):
# #    if message.text == 'Hi':
# #        bot.send_message(message.chat.id, 'Hi')
# #    elif message.text == 'No':
# #        bot.send_message(message.chat.id, 'No')
# #    else: bot.send_message(message.chat.id, 'QHJGRQ')
#
# # photo
# # bot.message_handler()
# # def get_photo(message):
# #    if message.text == 'Photo':
# #        photo = open('Path', 'rb')
# #        bot.send_message('message.chat.id', photo)
#
# # files reading
# # @bot.message_handler(content_types=['Photo'])
# # def get_user_photo(message):
# #     bot.send_message('message.chat.id', 'Textsmth')
#
# # message with buttons
# # @bot.message_handler(commands=['smth'])
# # def smth(message):
# #     markup = types.InlineKeyboardMarkup
# #     item = types.InlineKeyboardButton("Name of the button", url="https://skillsetter.io")
# #     markup.add(item)
# #     bot.send_message(message.chat.id, 'Hello', reply_markup=item)
#
#
# # buttons with message

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



# @bot.message_handler()
# def get_question(message):
#     if message != '/start' \
#             and message != '/delete' \
#             and message != 'Студент' \
#             and message != 'Як взяти участь в IT School/Sales School/будь-якому проєкті STUD-POINT?' \
#             and message != 'Як купити відеокурси STUD-POINT і скільки вони коштують?' \
#             and message != 'Ви отримали моє резюме, хочу працювати у вас?' \
#             and message != 'Я економіст/копірайтер/дизайнер/будь-хто, які вакансії ви можете мені запропонувати?' \
#             and message != 'Оберіть ваше питання:' \
#             and message != 'Мого питання немає серед переліку' \
#             and message != 'Як і на яких умовах розмістити у вас вакансію/анонс/інформацію?' \
#             and message != 'Які слоти на публікацію у вас є і чи можна опублікувати комерційне просто зараз?' \
#             and message != 'Як взяти участь в IT School/Sales School/будь-якому проєкті STUD-POINT?' \
#             and message != 'Як купити відеокурси STUD-POINT і скільки вони коштують?' \
#             and message != 'Хочемо взяти участь у проєкті, щоб закрити вакансії та посилити бренд ' \
#                              'роботодавця, які івенти заплановані на найближчий час?' \
#             and message != 'Роботодавець / Партнер':
#
#         us_id = message.from_user.id
#         us_name = message.from_user.first_name
#         us_sname = message.from_user.last_name
#         username = message.from_user.username
#         us_text = message.text
#         add_info(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username, text=us_text)
#
#         bot.send_message(message.chat.id, 'Дякую! Чекайте на відповідь від наших представників. Якщо хочете повернутися'
#                                           'до переліку питань, напишіть /start')
#     else:
#         pass


@bot.message_handler(commands=['delete'])
def delete_data(message):
    cursor.execute("DELETE FROM Users_questions")
    connect.commit()


# @bot.message_handler(commands=['q'])
# @bot.message_handler()
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#
#     first_button = types.KeyboardButton('Як і на яких умовах розмістити у вас вакансію/анонс/інформацію?')
#     second_button = types.KeyboardButton('Які слоти на публікацію у вас є і чи можна опублікувати комерційне просто '
#                                          'зараз?')
#     third_button = types.KeyboardButton('Як взяти участь в IT School/Sales School/будь-якому проєкті STUD-POINT?')
#     fourth_button = types.KeyboardButton('Як купити відеокурси STUD-POINT і скільки вони коштують?')
#     fifth_button = types.KeyboardButton('Ви отримали моє резюме, хочу працювати у вас?')
#     sixth_button = types.KeyboardButton('Я економіст/копірайтер/дизайнер/будь-хто, які вакансії ви можете мені '
#                                         'запропонувати?')
#     seventh_button = types.KeyboardButton('Хочемо взяти участь у проєкті, щоб закрити вакансії та посилити бренд '
#                                           'роботодавця, які івенти заплановані на найближчий час?')
#     eight_button = types.KeyboardButton('Мого питання немає серед переліку')
#
#     #    markup.add(first_button, second_button)
#     markup.add(first_button)
#     markup.add(second_button)
#     markup.add(third_button)
#     markup.add(fourth_button)
#     markup.add(fifth_button)
#     markup.add(sixth_button)
#     markup.add(seventh_button)
#     markup.add(eight_button)
#
#     bot.send_message(message.chat.id, 'Яке ваше питання?', reply_markup=markup)
#
#     @bot.message_handler(content_types=['text'])
#     def get_text(message):
#         if message.text == 'Як і на яких умовах розмістити у вас вакансію/анонс/інформацію?':
#             bot.send_message(message.chat.id, "Комплексні послуги для роботодавців включають в себе 4 пакети послуг: "
#                                               "“Basic”, “Optimal”, “Premium”, “Platinum”. Для детальнішої інформації "
#                                               "ознайомтесь, будь ласка, за цим покликанням: "
#                                               "https://www.canva.com/design/DAD7Sr3yGE8/TOO6wZGuClG1v9PIGs1sPQ/"
#                                               "view?utm_content=DAD7Sr3yGE8&utm_campaign=designshare&utm_medium=link&"
#                                               "utm_source=sharebutton#1")
#         if message.text == 'Які слоти на публікацію у вас є і чи можна опублікувати комерційне просто зараз?':
#             bot.send_message(message.chat.id, 'Через декілька хвилин Вам напише менеджер щодо нашого контент плану та '
#                                               'ми оберемо зручний для вас час.')
#         if message.text == 'Як взяти участь в IT School/Sales School/будь-якому проєкті STUD-POINT?':
#             bot.send_message(message.chat.id, 'Студент: підпис тут: https://www.instagram.com/studpoint/ і підпис тут: '
#                                               'https://web.telegram.org/k/ Там актуальні новини від STUD-POINTу, '
#                                               'цікаві івенти, проєкти та багато цікавинок 😊. Доєднуйся, бо на тебе '
#                                               'вже очікують \n 😉 Роботодавець: Актуальну інформацію розміщено на таких '
#                                               'платформах як інстаграм https://www.instagram.com/studpoint/, фейсбук '
#                                               'https://www.facebook.com/studpoint.ua та телеграм https://web.telegram.'
#                                               'org/k/')
#         if message.text == 'Як купити відеокурси STUD-POINT і скільки вони коштують?':
#             bot.send_message(message.chat.id, 'Студент: крок 1: відкрий сайт STUD-POINTу; крок 2: якщо знайшов кнопку '
#                                               '«курси» зверху, то клацни на неї; при успішному проходженні цих кроків, '
#                                               'тобі відкриється світ актуальних відеокурсів з детальним описом, цінами '
#                                               'та найголовніше, вигідними пропозиціями. Або не мороч собі голову і '
#                                               'перейди за цим покликанням: https://stud-point.com/video-courses/ \n '
#                                               'Роботодавець: При переході за покликанням https://stud-point.com/video-'
#                                               'courses/ , відкриється інформація про актуальні курси, інформацію про '
#                                               'них та ціни з вигідними пропозиціями')
#         if message.text == 'Ви отримали моє резюме, хочу працювати у вас?':
#             bot.send_message(message.chat.id, 'Студент: Ми тут лишимо покликаннячко тобі https://stud-point.com/blog/'
#                                               'vakansiyi/, тут ти можеш підібрати найкращу вакансію під своє резюме) '
#                                               'Слідкуй за оновленнями та нехай удача завжди буде з тобою 😉'
#                                               '\n Роботодавець: STUD-POINT зібрав найкращі вакансії в одному місці, '
#                                               'потрібно лише обрати з різноманіття. Покликання ось: '
#                                               'https://stud-point.com/blog/vakansiyi/')
#         if message.text == 'Я економіст/копірайтер/дизайнер/будь-хто, які вакансії ви можете мені запропонувати?':
#             bot.send_message(message.chat.id, 'Не повіриш. Вакансії економіста, дизайнера або будь-кого')
#         if message.text == 'Хочемо взяти участь у проєкті, щоб закрити вакансії та посилити бренд роботодавця,' \
#                            'які івенти заплановані на найближчий час?':
#             bot.send_message(message.chat.id, 'Роботодавець: STUD-POINT надає можливість для розвитку бренду р'
#                                               'оботодавця та надає такі послуги як рекламна кампанія для Вашої цільової '
#                                               'авдиторії та реалізація індивідуальних кар’єрних подій на замовлення. '
#                                               'Для детальнішої інформації ознайомтесь, будь ласка, за цим покликанням: '
#                                               'https://www.canva.com/design/DAD6o7QqjTs/nSYcK-UKozTWBJ5QGmga7A/view#4 ')
#         if message.text == 'Мого питання немає серед переліку':
#
#             connect = sqlite3.connect('questions.db')
#             cursor = connect.cursor()
#
#             cursor.execute("""CREATE TABLE IF NOT EXISTS all_questions(айді INTEGER, номер_телефону TEXT,
#             логін_телеграм TEXT, питання TEXT,)""")
#
#             connect.commit()
#
#             # check
#             people_id = message.chat.id
#             cursor.execute(f"SELECT id FROM all_questions WHERE id = {people_id}")
#             data = cursor.fetchone()
#             if data is None:
#                 # add values in fields
#                 question = [message.chat.id, message.chat.phone_number, message.chat.username, message.chat.text]
#                 cursor.execute("INSERT INTO all_questions VALUES (?);", question)
#                 connect.commit()
#             else:
#                 bot.send_message(message.chat.id, "Такий користувач вже існує")


# huge example
# bot.message_handler(commands=['help'])
#
#
# def help(message):
#   markup = types.InlineKeyboardMarkup()
#   item_yes = types.InlineKeyboardButton('Yes','Yes')
#   item_no = types.InlineKeyboardButton('No', 'No')
#
#   markup.add(item_yes, item_no)
#   bot.send_message(message.chat.id, 'Do you wanna know smth about you?', reply_markup=markup)
#
#
# @bot.callback_query_handler(lambda call: True)
# def answer(call):
#    if call.data == 'yes':
#        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
#        first_button = types.KeyboardButton('ID')
#        second_button = types.KeyboardButton('Name')
#
#       markup_reply.add(first_button, second_button)
#    bot.send_message(call.message.chat.id, 'Press te button', reply_markup=markup_reply)
#    elif call.data == 'no':
#        pass  # sm action
#
#
# @bot.message_handler(content_types=['text'])
# def get_text(message):
#    if message.text == 'ID':
#        bot.send_message(message.chat.id, f'{message.from_user.id}')
#    if message.text == 'Name':
#        bot.send_message(message.chat.id, f'{message.from_user.firstName} {message.from_user.lastName}')


bot.infinity_polling()
