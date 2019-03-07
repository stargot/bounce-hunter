import imaplib
import settings
from helper import random_hash

# Файл в котором будут сохраняться значения
f = open('check_{}.txt'.format(random_hash()), 'w+')

# Подключение
m = imaplib.IMAP4_SSL(settings.SMTP_HOST)
m.login(settings.SMTP_LOGIN, settings.SMTP_PASSWORD)
print("Подключение к почтовому ящику")
# Выбор нужной папки
m.list()
m.select('INBOX')
print("Переходим в папку Входящие")
# Поиск сообщений от нужного отправителя

typ, data = m.search(None, '(FROM settings.MAILER_DAEMON_EMAIL)')

# Количество писем для обработки
total = len(data[0].split())
print(f'Загружено {total} писем')

print("Запускаем цикл обработки")
for num in data[0].split():
    typ, data = m.fetch(num, '(RFC822)')
    # print('Message %s\n%s\n' % (num, data[0][1]))
    f.write(str(data[0][1]) + '\n')
    m.store(num, '+FLAGS', '\\Deleted')
    # print("Письмо обработано. Идем дальше.")
print("Цикл обработки завершен")
# Удаляем помеченные письма
m.expunge()
print("Удаляем помеченные письма")

m.close()
print("Закрываем текущий почтовый ящик")

m.logout()
print("Завершаем соединение с почтовым сервером")
print("Готово!")
