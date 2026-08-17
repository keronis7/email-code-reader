```
# Email Code Reader

Простой Python-инструмент для автоматического получения кодов подтверждения с почты через IMAP.

## Возможности

- Подключение к любому почтовому сервису через IMAP
- Поиск кода в теме и теле письма
- Настройка длины кода (по умолчанию 6 цифр)
- Настройка периода поиска (по умолчанию 30 минут)

## Установка

1. Склонируйте репозиторий:

git clone https://github.com/keronis7/email-code-reader.git
cd email-code-reader

2. Создайте виртуальное окружение:

python -m venv venv
venv\Scripts\activate

3. Установите зависимости:

pip install -r requirements.txt

4. Создайте файл .env:

EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_password
EMAIL_IMAP_SERVER=imap.yourserver.com
TARGET_EMAIL=email_where_code_sent@example.com

## Использование

from email_code_reader import EmailCodeReader

reader = EmailCodeReader(
    email_address="your_email@example.com",
    password="your_password",
    imap_server="imap.yourserver.com"
)

code = reader.get_code(
    to_email="target@example.com",
    minutes=30,
    code_length=6
)

if code:
    print(f"Код: {code}")
else:
    print("Код не найден")

## Лицензия

MIT
```
