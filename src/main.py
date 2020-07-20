# -*- coding: utf-8 -*-
import telebot
import time


bot = telebot.TeleBot("933175966:AAENp5e-3y2DzknBhNPQZ_HAzerkbjX-a1E")

bot.remove_webhook()

time.sleep(0.1)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
	bot.send_message(message.chat.id, message.text)


#@bot.message_handler(commands = ["get_test_keyboard"])
#def test_keyboard(message):
#	keyboard_markup = telebot.types.ReplyKeyboardMarkup()
#	keyboard_markup.add("test", "it is test too")
#	bot.send_message(message.chat.id, "text for user", reply_markup = keyboard_markup)
#	return keyboard_markup


if __name__ == '__main__':
	bot.polling(none_stop = True)
