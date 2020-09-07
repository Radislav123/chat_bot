from docx2python import docx2python
from pathlib import Path
from constants import *
import platform
import telebot
import random
import flask
import glob
import re

project_root_directory = str(Path().absolute().parent)
bot = telebot.TeleBot(API_TOKEN)
app = flask.Flask(__name__)
commands = []


def get_platform():
	return platform.node()


def get_course_links_keyboard_markup():
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
			text = COURSE_LINK_DESCRIPTION,
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


def get_filepaths_by_path(path, extension = ''):
	regular_path = path + '*'
	if extension != '':
		regular_path += "." + extension
	return glob.glob(regular_path)


def get_random_filepath_by_path(path, extension = ''):
	filepaths = get_filepaths_by_path(path, extension)
	return filepaths[random.randrange(len(filepaths))]


def get_random_course_fragment_from_pages():
	fragment_path = get_random_filepath_by_path(
		project_root_directory + "\\course_fragments\\pages\\",
		COURSE_FRAGMENTS_EXTENSION
	)
	document = docx2python(fragment_path)
	text = ""
	for line in document.text.splitlines()[:-4]:
		text = text + '\n' + line
	return text[1:]


def get_random_course_fragment_from_books():
	book_path = get_random_filepath_by_path(project_root_directory + "\\course_fragments\\books\\") + "\\"
	fragment_path = get_random_filepath_by_path(book_path, COURSE_FRAGMENTS_EXTENSION)
	document = docx2python(fragment_path)
	text = ""
	for line in document.text.splitlines()[:-2]:
		text = text + '\n' + line
	return text[1:]


def split_text_by_chunks(text):
	chunks = []
	first = True
	for line in text.splitlines(False):
		words = len(line.split())
		if first or (words <= 6 and re.match("Группа", line)):
			first = False
		elif line != "":
			if re.match(r"--", line) or re.match(r"\t--", line) or re.match(r"\d\)", line):
				chunks[-1] += "\n\n" + line
			else:
				chunks.append(line)
	return chunks


def get_random_course_fragment():
	if random.randrange(2):
		text = get_random_course_fragment_from_pages()
	else:
		text = get_random_course_fragment_from_books()
	chunks = split_text_by_chunks(text)
	return chunks[random.randrange(len(chunks))]


def get_help_command_keyboard_markup():
	keyboard_markup = get_keyboard_markup(telebot.types.InlineKeyboardButton(
		text = COURSE_LINK_DESCRIPTION,
		url = COURSE_LINK
	))
	return keyboard_markup
