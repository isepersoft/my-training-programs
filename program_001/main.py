import telebot
from telebot import types
import tkinter as tk
from tkinter import *
import requests
import json

bot = telebot.TeleBot('6799546961:AAFkYkT6R4M8RqxQTDsILbRCqRV1LQw1TWU')

# Функция для получения погоды
def get_weather(city):
    url = ('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&APPID=4e04ad39dd9272d1ae0b831946a29bc4')
    weather_data = requests.get(url).json()
    weather_data_structure = json.dumps(weather_data, indent=2)

    temperature = round(weather_data['main']['temp'])
    temperature_feels = round(weather_data['main']['feels_like'])
    wind_speed = round(weather_data['wind']['speed'])

    return f'Ваш город: {city}.\nСейчас в городе {temperature} °C\nОщущается как {temperature_feels} °C\nСкорость ветра {wind_speed} м/с'

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtncity1 = types.KeyboardButton('Томск')
    itembtncity2 = types.KeyboardButton('Северск')
    markup.add(itembtncity1, itembtncity2)

    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>\nЧтобы узнать погоду - выберите город:'
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)

# Обработчик кнопок с городами
@bot.message_handler(func=lambda message: True)
def handle_city_buttons(message):
    if message.text in ['Томск', 'Северск']:
        weather_info = get_weather(message.text)
        bot.send_message(message.chat.id, weather_info, parse_mode='html')

# ... остальные обработчики

@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html') 
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')   

bot.polling(none_stop=True)
