from broadcast import *
from commands import *
from service import *
import time


# For periodic course fragments broadcasting
# {chat_id: timer}
chats_ids = {}


# Empty webserver index, return http 200
@app.route('/', methods = ["GET", "HEAD"])
def index():
	return BOT_HTTP_INDEX_TEXT


# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods = ["POST"])
def webhook():
	if flask.request.headers.get("content-type") == 'application/json':
		json_string = flask.request.get_data().decode('utf-8')
		update = telebot.types.Update.de_json(json_string)
		bot.process_new_updates([update])
		return ''
	else:
		return flask.abort(403)


@bot.callback_query_handler(func = lambda call: True)
def set_timer_callback_handler(callback):
	if re.match(r"set timer \d+", callback.data):
		timer = int(re.findall(r"\d+", callback.data)[0])
		chats_ids[str(callback.message.chat.id)] = timer
	return bot.edit_message_text("Время выбрано.", callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands = [START_COMMAND])
def start_command(message):
	keyboard_markup = get_help_command_keyboard_markup()
	bot.send_message(message.chat.id, BOT_DESCRIPTION, reply_markup = keyboard_markup)

	return set_timer_command(message)


@bot.message_handler(commands = [SET_TIMER_COMMAND])
def set_timer_command(message):
	call_back_data = "set timer %d"
	keys = []

	for timer in TIMERS:
		keys.append(telebot.types.InlineKeyboardButton(text = str(timer), callback_data = call_back_data % timer))

	keyboard_markup = get_keyboard_markup(*keys)
	return bot.send_message(
		message.chat.id,
		"Выберите, как часто я должен отправлять тебе случайный фрагмент материалов курса.\n\nРаз в ___ час[а|ов].",
		reply_markup = keyboard_markup
	)


@bot.message_handler(commands = [GET_TIMER_COMMAND])
def get_timer_command(message):
	return bot.send_message(message.chat.id, "Твой таймер установлен на %d час[а|ов]." % chats_ids[str(message.chat.id)])


@bot.message_handler(commands = [HELP_COMMAND])
def help_command(message):
	return bot.send_message(message.chat.id, BOT_DESCRIPTION, reply_markup = get_help_command_keyboard_markup())


@bot.message_handler(commands = [COMMAND_LIST_COMMAND])
def command_list_command(message):
	return bot.send_message(message.chat.id, get_command_list_text())


@bot.message_handler(commands = [COURSE_LINKS_COMMAND])
def course_links_command(message):
	return bot.send_message(
		message.chat.id,
		COURSE_LINKS_COMMAND_DESCRIPTION,
		reply_markup = get_course_links_keyboard_markup()
	)


@bot.message_handler(commands = [ADDITIONAL_MATERIALS_LINKS_COMMAND])
def additional_materials_links_command(message):
	return bot.send_message(
		message.chat.id,
		ADDITIONAL_MATERIALS_LINKS_COMMAND_DESCRIPTION,
		reply_markup = get_additional_materials_links()
	)


@bot.message_handler(commands = [DEADLINES_COMMAND])
def deadlines_command(message):
	return bot.send_message(message.chat.id, get_deadlines_text())


@bot.message_handler(commands = [INTERVIEW_COMMAND])
def interview_command(message):
	text = "1) тут можно воткнуть кнопку-ссылку на гугл-опрос\n2) можно что-то налепить внутри бота"
	return bot.send_message(message.chat.id, text)


# Handle all other text messages
@bot.message_handler(content_types = ["text"])
def echo_message(message):
	text = "Я тебя не понимаю, поэтому лучше почитай\n\n\n" + get_random_course_fragment()
	return bot.send_message(message.chat.id, text)


if __name__ == '__main__':
	# Remove old webhook, it fails sometimes the set if there is a previous webhook
	bot.remove_webhook()
	time.sleep(0.1)

	set_bot_command_list()
	chats_ids = load_chats_ids_from_file()

	# add_jobs(chats_ids) must be called firstly
	# tl.start() secondly
	add_jobs(chats_ids)
	tl.start()

	platform = get_platform()

	try:
		if platform == SERVER_MACHINE_NAME:
			print("running on the dedicated server")
			# Set webhook
			bot.set_webhook(url = WEBHOOK_URL_FULL, certificate = open(WEBHOOK_SSL_CERTIFICATE, 'r'))

			# Start flask server
			app.run(
				ssl_context = (WEBHOOK_SSL_CERTIFICATE, WEBHOOK_SSL_PRIVATE_KEY),
				host = WEBHOOK_LISTEN,
				port = WEBHOOK_PORT
			)
		elif platform == LAPTOP_MACHINE_NAME or platform == DESKTOP_MACHINE_NAME:
			print("running on the local machine")
			bot.polling(none_stop = True)
		else:
			print("undefined machine\nnot running")
	finally:
		tl.stop()
		save_chats_ids_to_file(chats_ids)
