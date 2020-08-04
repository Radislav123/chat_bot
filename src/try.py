import requests
import webbrowser
import tempfile
import platform


def try_urls():
	urls = [
		"https://online.hse.ru/",
		"https://online.hse.ru/course/",
		"https://online.hse.ru/course/view.php",
		"https://online.hse.ru/course/view.php?id=1845"
	]

	for url in urls:
		response = requests.get(url)
		with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as file:
			url = 'file://' + file.name
			file.write(str(response.headers))
		webbrowser.open(url)


def get_ip():
	return requests.get('https://api.ipify.org').text


def get_platform():
	return platform.node()


print(get_platform())
