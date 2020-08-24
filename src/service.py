from constants import *
import platform
import telebot
import flask

bot = telebot.TeleBot(API_TOKEN)
app = flask.Flask(__name__)
commands = []


def get_platform():
	return platform.node()


def get_course_links():
	keys = [
		telebot.types.InlineKeyboardButton(
			text = "первая важная ссылка",
			url = "https://online.hse.ru/mod/forum/view.php?id=48811"
		),
		telebot.types.InlineKeyboardButton(
			text = "вторая важная ссылка",
			url = "https://online.hse.ru/mod/page/view.php?id=49106"
		),
		telebot.types.InlineKeyboardButton(
			text = "третья важная ссылка",
			url = "https://online.hse.ru/mod/page/view.php?id=123827"
		),
		telebot.types.InlineKeyboardButton(
			text = "ссылка на курс",
			url = COURSE_LINK
		)
	]
	return get_keyboard_markup(*keys)


def get_additional_materials_links():
	keys = [
		telebot.types.InlineKeyboardButton(
			text = "рекомендуемая литература",
			url = "https://online.hse.ru/mod/page/view.php?id=48941"
		)
	]
	return get_keyboard_markup(*keys)


def get_deadlines_text():
	deadlines = "тут должен быть список дэдлайнов\nможно оформить в виде кнопок с ссылками"
	return deadlines


def get_keyboard_markup(*keys):
	keyboard_markup = telebot.types.InlineKeyboardMarkup()
	keyboard_markup.add(*keys)
	return keyboard_markup


def get_command_list_text():
	text = ""
	for command, description in get_commands_with_descriptions():
		text += '/' + command + "   " + description + '\n'
	return text


def get_commands_with_descriptions():
	if len(commands) == 0:
		with open("commands.py", encoding='utf-8') as commands_file:
			for line in commands_file:
				if line == '\n':
					pair = [commands_file.readline().split(" = ")[1], commands_file.readline().split(" = ")[1]]
					pair[0] = pair[0][1:-2]
					pair[1] = pair[1][1:-2]
					commands.append(pair)
	return commands


def set_bot_command_list():
	bot_commands = []
	for pair in get_commands_with_descriptions():
		bot_commands.append(telebot.types.BotCommand(pair[0], pair[1]))
	return bot.set_my_commands(bot_commands)
