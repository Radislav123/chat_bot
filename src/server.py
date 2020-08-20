from commands import *
from service import *
import time


# Empty webserver index, return http 200
@app.route('/', methods = ['GET', 'HEAD'])
def index():
	return "Hello, world!\nI\'m SimpleHelper bot and it's root page of my webhook flask-server."


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
def help_command(message):
	return bot.reply_to(message, "Hi there, I am EchoBot.\nI am here to echo your kind words back to you.")


@bot.message_handler(commands = [COMMAND_LIST_COMMAND])
def command_list_command(message):
	return bot.send_message(message.chat.id, "it is command list")


@bot.message_handler(commands = [MAIN_MENU_COMMAND])
def main_menu_command(message):
	return bot.send_message(message.chat.id, "temp")


@bot.message_handler(commands = [TEST_KEYBOARD_COMMAND])
def test_keyboard_command(message):
	keyboard_markup = get_keyboard_markup(["test", "it is test too"])
	bot.send_message(message.chat.id, "text for user", reply_markup = keyboard_markup)
	return keyboard_markup


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
