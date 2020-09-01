import requests
import webbrowser
import tempfile
import platform
from docx2python import docx2python


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


def get_random_course_fragment():
	document = docx2python("../course_fragments/Ресурсы для проведения обзора литературы.docx")
	text = ""
	for line in document.text.splitlines()[:-4]:
		if line != '':
			text = text + '\n' + line
	return text[1:]


print(get_random_course_fragment())
