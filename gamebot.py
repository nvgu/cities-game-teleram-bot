import config
import telebot
import cities_script
bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = ""
    user_message = str(message.text)
    for message_city in cities_script.city: 
        if user_message.lower() == message_city['name'].lower():
            i = user_message[-1] 
            for city in cities_script.city:
                if i.lower() == city['name'][0].lower():
                    text = city['name']
                    break
        else:
            text = "Я не знаю такой город"
        break
    bot.send_message(message.chat.id, text)
if __name__ == '__main__':
     bot.polling(none_stop=True)