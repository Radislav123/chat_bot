# -*- coding: utf-8 -*-
import telebot


bot = telebot.TeleBot("933175966:AAENp5e-3y2DzknBhNPQZ_HAzerkbjX-a1E")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
	bot.polling(none_stop=True)