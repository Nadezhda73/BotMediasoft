import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    send_mess = f"Привет, {message.from_user.first_name}\nКакой жанр тебя интересует?"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Боевик")
    item2 = types.KeyboardButton("Детектив")
    item3 = types.KeyboardButton("Документальный")
    item4 = types.KeyboardButton("Драма")
    item5 = types.KeyboardButton("Комедия")
    item6 = types.KeyboardButton("Мелодрама")
    item7 = types.KeyboardButton("Триллер")
    item8 = types.KeyboardButton("Ужасы")

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

    bot.send_message(message.chat.id, send_mess, reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "С помощью данного бота ты сможешь выбрать интересующий тебя жанр и перейти на сайт для выбора фильма 😉\nСписок команд:\n/help\n/start")


@bot.message_handler(content_types=['text'])
def genre(message):
    if message.chat.type == 'private':
        if message.text.lower() == 'боевик':
            murkup = types.InlineKeyboardMarkup()
            murkup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.kinopoisk.ru/lists/navigator/action/?quick_filters=high_rated%2Cfilms&tab=all"))
            bot.send_message(message.chat.id, "👇🏻 Лучшие боевики 👇🏻", parse_mode='html', reply_markup=murkup)
        elif message.text.lower() == 'детектив':
            murkup = types.InlineKeyboardMarkup()
            murkup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.kinopoisk.ru/lists/navigator/mystery/?quick_filters=high_rated%2Cfilms&tab=all"))
            bot.send_message(message.chat.id, "👇🏻 Лучшие детективы 👇🏻", parse_mode='html', reply_markup=murkup)
        elif message.text.lower() == 'документальный':
            murkup = types.InlineKeyboardMarkup()
            murkup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.kinopoisk.ru/lists/navigator/documentary/?quick_filters=films%2Chigh_rated&tab=all"))
            bot.send_message(message.chat.id, "👇🏻 Лучшие документальные фильмы 👇🏻", parse_mode='html', reply_markup=murkup)
        elif message.text.lower() == 'драма':
            murkup = types.InlineKeyboardMarkup()
            murkup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.kinopoisk.ru/lists/navigator/drama/?quick_filters=high_rated%2Cfilms&tab=all"))
            bot.send_message(message.chat.id, "👇🏻 Лучшие драмы 👇🏻", parse_mode='html', reply_markup=murkup)
        elif message.text.lower() == 'комедия':
            murkup = types.InlineKeyboardMarkup()
            murkup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.kinopoisk.ru/lists/navigator/comedy/?quick_filters=high_rated%2Cfilms&tab=all"))
            bot.send_message(message.chat.id, "👇🏻 Лучшие комедии 👇🏻", parse_mode='html', reply_markup=murkup)
        elif message.text.lower() == 'мелодрама':
            murkup = types.InlineKeyboardMarkup()
            murkup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.kinopoisk.ru/lists/navigator/romance/?quick_filters=high_rated%2Cfilms&tab=all"))
            bot.send_message(message.chat.id, "👇🏻 Лучшие мелодрамы 👇🏻", parse_mode='html', reply_markup=murkup)
        elif message.text.lower() == 'триллер':
            murkup = types.InlineKeyboardMarkup()
            murkup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.kinopoisk.ru/lists/navigator/thriller/?quick_filters=high_rated%2Cfilms&tab=all"))
            bot.send_message(message.chat.id, "👇🏻 Лучшие триллеры 👇🏻", parse_mode='html', reply_markup=murkup)
        elif message.text.lower() == 'ужасы':
            murkup = types.InlineKeyboardMarkup()
            murkup.add(types.InlineKeyboardButton("Посетить сайт", url="https://www.kinopoisk.ru/lists/navigator/horror/?quick_filters=high_rated%2Cfilms&tab=all"))
            bot.send_message(message.chat.id, "👇🏻 Лучшие ужасы 👇🏻", parse_mode='html', reply_markup=murkup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю такой жанр 😰 Выбери из предложенных!')


bot.polling(none_stop=True)