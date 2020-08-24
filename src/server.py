from commands import *
from service import *
import time


# Empty webserver index, return http 200
@app.route('/', methods = ['GET', 'HEAD'])
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


@bot.message_handler(commands = [HELP_COMMAND])
def command_list_command(message):
	return bot.send_message(message.chat.id, BOT_DESCRIPTION)


@bot.message_handler(commands = [COMMAND_LIST_COMMAND])
def command_list_command(message):
	return bot.send_message(message.chat.id, get_command_list_text())


@bot.message_handler(commands = [COURSE_LINKS_COMMAND])
def course_links_command(message):
	return bot.send_message(message.chat.id, COURSE_LINKS_COMMAND_DESCRIPTION, reply_markup = get_course_links())


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


# Handle all other messages
@bot.message_handler(content_types = ["text"])
def echo_message(message):
	return bot.reply_to(message, message.text)


if __name__ == '__main__':
	# Remove old webhook, it fails sometimes the set if there is a previous webhook
	bot.remove_webhook()
	time.sleep(0.1)

	set_bot_command_list()

	platform = get_platform()

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
	elif platform == LAPTOP_MACHINE_NAME:
		print("running on the local machine")
		bot.polling(none_stop = True)
	else:
		print("undefined machine\nnot running")
