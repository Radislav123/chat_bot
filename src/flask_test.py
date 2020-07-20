import flask

# www.simplebot.ru
IP = "18.218.144.4"
app = flask.Flask(__name__)


# Empty webserver index, return nothing, just http 200
@app.route('/')
def index():
	return 'Hello, world!'


app.run(host = "0.0.0.0", port = 80)