import flask
import telebot
import time

API_TOKEN = "933175966:AAENp5e-3y2DzknBhNPQZ_HAzerkbjX-a1E"

# www.simplebot.ru
IP = "18.218.144.4"
WEBHOOK_HOST = IP
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = "0.0.0.0"  # In some VPS you may need to put here the IP addr

WEBHOOK_SSL_CERT = '../attachments/webhook_cert.pem'  # Path to the ssl certificate
WEBHOOK_SSL_PRIV = '../attachments/webhook_pkey.pem'  # Path to the ssl private key

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
print(WEBHOOK_URL_BASE)
WEBHOOK_URL_PATH = "/%s/" % API_TOKEN

bot = telebot.TeleBot(API_TOKEN)
app = flask.Flask(__name__)


# Empty webserver index, return nothing, just http 200
@app.route('/', methods = ['GET', 'HEAD'])
def index():
	return ''


# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods = ['POST'])
def webhook():
	if flask.request.headers.get('content-type') == 'application/json':
		json_string = flask.request.get_data().decode('utf-8')
		update = telebot.types.Update.de_json(json_string)
		bot.process_new_updates([update])
		return ''
	else:
		flask.abort(403)


# Handle all other messages
@bot.message_handler(content_types = ["text"])
def echo_message(message):
	bot.reply_to(message, message.text)


# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

time.sleep(0.1)

# Set webhook
bot.set_webhook(url = WEBHOOK_URL_BASE + WEBHOOK_URL_PATH, certificate = open(WEBHOOK_SSL_CERT, 'r'))

# Start flask server
app.run(host = WEBHOOK_LISTEN, port = WEBHOOK_PORT, debug = True, ssl_context = (WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV))
