### Разное, но нужное
Для запуска в [*attachments/*](https://github.com/Radislav123/chat_bot/tree/master/attachments) должны находиться файлы, которых нет в репозитории:
1) *telegram_bot_token.txt* с [*токеном*](https://core.telegram.org/bots#6-botfather) бота (нужен для любого запуска)
2) *webhook_cert.pem* и *webhook_pkey.pem* - [*самоподписный сертификат*](https://groosha.gitbook.io/telegram-bot-lessons/chapter4#sozdaem-sertifikat) и приватный ключ
(нужны для запуска на сервере)

try.py прямого отношения к проекту не имеет.

В случае проблем с самоподписным сертификатом - [*certificate_problems.txt*](https://github.com/Radislav123/chat_bot/blob/master/attachments/certificate_problems.txt)

### Запуск

#### Для запуска на сервере:
1) [*AWS_INSTANCE_IP*](https://github.com/Radislav123/chat_bot/blob/master/src/constants.py#L7) - белый IP сервера
2) [*SERVER_MACHINE_NAME*](https://github.com/Radislav123/chat_bot/blob/master/src/constants.py#L18) - [*имя машины*](http://podmoga.org/?p=193#:~:text=%D0%92%20%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D0%B2%D1%88%D0%B5%D0%BC%D1%81%D1%8F%20%D0%BE%D0%BA%D0%BD%D0%B5%20%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D0%B8%D0%BA%D0%B0%20%D0%BD%D0%B0%D1%85%D0%BE%D0%B4%D0%B8%D0%BC,%3A%C2%BB%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%20%D1%83%D0%B2%D0%B8%D0%B4%D0%B5%D1%82%D1%8C%20%D0%B8%D0%BC%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%B0.),
на которой запускается бот

#### Для запуска локально:
1) [*LAPTOP_MACHINE_NAME*](https://github.com/Radislav123/chat_bot/blob/master/src/constants.py#L19)
или [*DESKTOP_MACHINE_NAME*](https://github.com/Radislav123/chat_bot/blob/master/src/constants.py#L20) - [*имя машины*](http://podmoga.org/?p=193#:~:text=%D0%92%20%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D0%B2%D1%88%D0%B5%D0%BC%D1%81%D1%8F%20%D0%BE%D0%BA%D0%BD%D0%B5%20%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D0%B8%D0%BA%D0%B0%20%D0%BD%D0%B0%D1%85%D0%BE%D0%B4%D0%B8%D0%BC,%3A%C2%BB%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%20%D1%83%D0%B2%D0%B8%D0%B4%D0%B5%D1%82%D1%8C%20%D0%B8%D0%BC%D1%8F%20%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80%D0%B0.),
на которой запускается бот

#### Запускать из [*src/*](https://github.com/Radislav123/chat_bot/tree/master/src) (через командную оболочку):

Windows:  

    ...src> python server.py

Unix:  

    ...src> python3 ./server.py
