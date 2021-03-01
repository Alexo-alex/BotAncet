import telebot
from telebot import types

bot = telebot.TeleBot('1547106535:AAHSCVDQy-alTpKTt-tkMNdWzSru1nwfk0w')

name = ''
sex = ''
age = 0


@bot.message_handler(content_types=['text'])
def start(message):
    #Меню бота
    if message.text == 'Меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Ваша інформація")
        item2 = types.InlineKeyboardButton("Налаштування")
        markup.add(item1, item2)
        bot.send_message(message.from_user.id, 'Меню', reply_markup=markup)
    elif message.text == 'Ваша інформація':
        bot.send_message(message.chat.id, f'{name}\n{sex}\n{age}р.')

    elif message.text == 'Налаштування':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Змінити вік")
        item2 = types.InlineKeyboardButton("Змінити стать")
        item3 = types.InlineKeyboardButton("Змінити ім'я")
        item4 = types.InlineKeyboardButton("Назад")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, 'Налаштування', reply_markup=markup)

    elif message.text == 'Змінити вік':
        bot.send_message(message.chat.id, 'Змініть свій вік!')
        bot.register_next_step_handler(message, age_sett)

    elif message.text == 'Змінити стать':
        bot.send_message(message.chat.id, 'Змініть свію стать!')
        bot.register_next_step_handler(message, sex_sett)

    elif message.text == "Змінити ім'я":
        bot.send_message(message.chat.id, "Змініть своє ім'я!")
        bot.register_next_step_handler(message, name_sett)

    elif message.text == "Назад":  # Кнопка повернення до меню
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Меню")
        markup.add(item1)
        bot.send_message(message.from_user.id, 'Меню', reply_markup=markup)
    #При умові що текст = /start здійснюється запуск функції анкетування
    elif message.text == '/start':
        bot.send_message(message.from_user.id, "Твоє ім'я?")
        bot.register_next_step_handler(message, get_name)


def get_name(message):  # Отримуємо ім'я
    global name
    if len(message.text) < 2 or len(message.text) > 20:
        bot.send_message(message.from_user.id, "Ім'я не може бути менше 2 або більше 20 символів!\n"
                                               "Спробуйте ще раз!")
        bot.register_next_step_handler(message, get_name)
    else:
        name = message.text
        bot.send_message(message.from_user.id, 'Ваша стать - Чоловік/Жінка?', )
        bot.register_next_step_handler(message, get_sex)


def get_sex(message):  # Отримуємо стать
    global sex
    if (message.text == 'Чоловік') or (message.text == 'Жінка'):  # Умова вказує, що стать може мати лише два варіанти вводу "Чоловік" або "Жінка"
        sex = message.text
        bot.send_message(message.from_user.id, 'Ваш вік?')
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(message.from_user.id, "Спробуйте ще раз - Чоловік/Жінка")
        bot.register_next_step_handler(message, get_sex)


def get_age(message):  # Отримуємо вік
    global age
    try:  # Перевіряємо, що вік введено коректно
        age = int(message.text)
    except Exception:
        bot.send_message(message.from_user.id, 'Цифрами, будь ласка!')
        bot.register_next_step_handler(message, get_age)
        return
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.InlineKeyboardButton("Меню")
    markup.add(item1)

    bot.send_message(message.from_user.id, 'Ваші данні отримано, змінити та переглянути їх можливо в меню!',
                     reply_markup=markup)

# Функції зміни даних
def age_sett(message):  # Змінити вік
    global age
    if message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Меню")
        markup.add(item1)
        bot.send_message(message.from_user.id, 'Меню', reply_markup=markup)
    else:
        try:  # Перевіряємо, що вік введено коректно
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, будь ласка!')
            bot.register_next_step_handler(message, age_sett)
            return
        bot.send_message(message.from_user.id, 'Ви успішно змінили свій вік!')


def sex_sett(message):  # Змінити стать
    global sex
    if message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Меню")
        markup.add(item1)
        bot.send_message(message.from_user.id, 'Меню', reply_markup=markup)
    elif (message.text == 'Чоловік') or (message.text == 'Жінка'):  # Умова вказує, що стать може мати лише два варіанти вводу "Чоловік" або "Жінка"
        sex = message.text
        bot.send_message(message.from_user.id, 'Ви успішно змінили свою стать!')
    else:  # Після некоректного вводу просимо повторити спробу
        bot.send_message(message.from_user.id, "Спробуйте ще раз - Чоловік/Жінка")
        bot.register_next_step_handler(message, sex_sett)


def name_sett(message):  # Змінити ім'я
    global name
    if message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.InlineKeyboardButton("Меню")
        markup.add(item1)
        bot.send_message(message.from_user.id, 'Меню', reply_markup=markup)
    elif len(message.text) < 2 or len(message.text) > 20:  # Перевіка імені на відповідність заданій умові
        bot.send_message(message.from_user.id, "Ім'я не може бути менше 2 або більше 20 символів!\n"
                                               "Спробуйте ще раз!")
        bot.register_next_step_handler(message, name_sett)
    else:
        name = message.text
        bot.send_message(message.from_user.id, "Ви успішно змінили своє ім'я!")


bot.polling(none_stop=True)
