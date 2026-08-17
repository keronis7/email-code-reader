\# Email Code Reader



Простой Python-инструмент для автоматического получения кодов подтверждения с почты через IMAP.



\## Возможности



\- Подключение к любому почтовому сервису через IMAP

\- Поиск кода в теме и теле письма

\- Настройка длины кода (по умолчанию 6 цифр)

\- Настройка периода поиска (по умолчанию 30 минут)



\## Установка



1\. Склонируйте репозиторий:

```bash

git clone https://github.com/yourusername/email-code-reader.git

cd email-code-reader



2\. Создайте виртуальное окружение:

python -m venv venv

venv\\Scripts\\activate



3\. Установите зависимости:

pip install -r requirements.txt



4\. Создайте файл .env:

EMAIL\_USER=your\_email@example.com

EMAIL\_PASSWORD=your\_password

EMAIL\_IMAP\_SERVER=imap.yourserver.com

TARGET\_EMAIL=email\_where\_code\_sent@example.com



\## Использование



from email\_code\_reader import EmailCodeReader



reader = EmailCodeReader(

&#x20;   email\_address="your\_email@example.com",

&#x20;   password="your\_password",

&#x20;   imap\_server="imap.yourserver.com"

)



code = reader.get\_code(

&#x20;   to\_email="target@example.com",

&#x20;   minutes=30,

&#x20;   code\_length=6

)



if code:

&#x20;   print(f"Код: {code}")

else:

&#x20;   print("Код не найден")



\## Лицензия



MIT



