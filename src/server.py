from constants import *
import telebot
import flask
import time


bot = telebot.TeleBot(API_TOKEN)
app = flask.Flask(__name__)


# Empty webserver index, return http 200
@app.route('/', methods=['GET', 'HEAD'])
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
		flask.abort(403)


@bot.message_handler(commands = ["get_test_keyboard"])
def test_keyboard(message):
	keyboard_markup = telebot.types.ReplyKeyboardMarkup()
	keyboard_markup.add("test", "it is test too")
	bot.send_message(message.chat.id, "text for user", reply_markup = keyboard_markup)
	return keyboard_markup


# Handle "/start" and "/help"
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.reply_to(message, "Hi there, I am EchoBot.\nI am here to echo your kind words back to you.")


# Handle all other messages
@bot.message_handler(content_types = ["text"])
def echo_message(message):
	bot.reply_to(message, message.text)


if __name__ == '__main__':
	# Remove old webhook, it fails sometimes the set if there is a previous webhook
	bot.remove_webhook()
	time.sleep(0.1)

	webhook = False

	if webhook:
		# Set webhook
		bot.set_webhook(url = WEBHOOK_URL_FULL, certificate = open(WEBHOOK_SSL_CERTIFICATE, 'r'))

		# Start flask server
		app.run(
			ssl_context = (WEBHOOK_SSL_CERTIFICATE, WEBHOOK_SSL_PRIVATE_KEY),
			host = WEBHOOK_LISTEN,
			port = WEBHOOK_PORT
		)
	else:
		bot.polling(none_stop = True)
