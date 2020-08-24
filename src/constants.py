
with open("../attachments/telegram_bot_token.txt", 'r') as file:
	API_TOKEN = file.read().replace('\n', '')

BOT_HTTP_INDEX_TEXT = "Hello, world!\nI\'m SimpleHelper bot and it's root page of my webhook flask-server."

AWS_INSTANCE_IP = "52.14.162.201"
WEBHOOK_HOST = AWS_INSTANCE_IP
WEBHOOK_PORT = 8443  # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = "0.0.0.0"  # In some VPS you may need to put here the IP addr
WEBHOOK_SSL_CERTIFICATE = "../attachments/webhook_cert.pem"  # Path to the ssl certificate
WEBHOOK_SSL_PRIVATE_KEY = "../attachments/webhook_pkey.pem"  # Path to the ssl private key
WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % API_TOKEN
WEBHOOK_URL_FULL = WEBHOOK_URL_BASE + WEBHOOK_URL_PATH

SERVER_MACHINE_NAME = "EC2AMAZ-H0K2IKR"
LAPTOP_MACHINE_NAME = "LAPTOP-8DTEU61A"

BOT_DESCRIPTION = "Тут должно быть описание бота (в том числе и к какому курсу он прикреплен)"

COURSE_LINK = "https://online.hse.ru/course/view.php?id=1845"
