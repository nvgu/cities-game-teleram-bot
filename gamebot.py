import config
import telebot
import cities_script
bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    user_message = message.text
    i = user_message[-1] 
    for city in cities_script.city:
        bot.send_message(message.chat.id, city['name'])
        if i == city['name'][0]:
            bot.send_message(message.chat.id, city['name'])
if __name__ == '__main__':
     bot.polling(none_stop=True)