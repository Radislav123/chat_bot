from constants import *
import platform
import telebot
import flask

bot = telebot.TeleBot(API_TOKEN)
app = flask.Flask(__name__)


def get_platform():
	return platform.node()


def get_keyboard_markup(keys):
	return telebot.types.ReplyKeyboardMarkup().add(*keys)


def read_commands_with_descriptions():
	commands = []
	with open("commands.py", encoding='utf-8') as commands_file:
		for line in commands_file:
			if line == '\n':
				pair = [commands_file.readline().split(" = ")[1], commands_file.readline().split(" = ")[1]]
				pair[0] = pair[0][1:-2]
				pair[1] = pair[1][1:-2]
				print(pair)
				commands.append(
					telebot.types.BotCommand(
						pair[0], pair[1]
					)
				)
	return commands


def set_bot_command_list():
	return bot.set_my_commands(read_commands_with_descriptions())
