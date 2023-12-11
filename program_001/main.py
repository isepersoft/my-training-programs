import telebot

bot = telebot.TeleBot('6799546961:AAFkYkT6R4M8RqxQTDsILbRCqRV1LQw1TWU')

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['help'])    
def help(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>\nРаздел Help находится в стадии разработки'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands=['about'])    
def about(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>\nРаздел About находится в стадии разработки'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    
@bot.message_handler()
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html') 
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')   
    

bot.polling(none_stop=True)