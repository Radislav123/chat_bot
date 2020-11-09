Запускать из [*src/*](https://github.com/Radislav123/chat_bot/tree/master/src) (через командную оболочку):

Windows:  

    ...src> python server.py

Unix:  

    ...src> python3 ./server.py

В [*attachments/*](https://github.com/Radislav123/chat_bot/tree/master/attachments) должны находиться файлы, которых нет в репозитории:
1) *telegram_bot_token.txt* с [*токеном*](https://core.telegram.org/bots#6-botfather) бота.
2) *webhook_cert.pem* и *webhook_pkey.pem* - [*самоподписный сертификат*](https://groosha.gitbook.io/telegram-bot-lessons/chapter4#sozdaem-sertifikat) и приватный ключ

try.py прямого отношения к проекту не имеет.

В случае проблем с самоподписным сертификатом - [*certificate_problems.txt*](https://github.com/Radislav123/chat_bot/blob/master/attachments/certificate_problems.txt)
