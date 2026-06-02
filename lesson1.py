##1. **Создайте словарь `email`**, который содержит поля:
##   `"subject"` (тема письма), `"from"` (адрес отправителя), `"to"` (адрес получателя), `"body"` (текст письма).
emails = [
    {
        "subject": "  Quarterly Report  ",
        "from": "  Alice.Cooper@Company.ru ",
        "to": "   bob_smith@Gmail.com   ",
        "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
    },
    {
        "subject": " Weekend plans ",
        "from": "  katya_yan@yandex.ru ",
        "to": "  friend@mail.ru ",
        "body": "\tHey!\nLet's go hiking this weekend.\nBring snacks!\n"
    },
    {
        "subject": "Reminder: Meeting",
        "from": "  ceo@corporation.com ",
        "to": " team_lead@outlook.com ",
        "body": "   "
    },
{
    "subject": "   ",
    "from": "   alex@business.net ",
    "to": "   hr@company.ru ",
    "body": "Hi HR,\nPlease find attached my updated CV.\nThanks!"
},
{
    "subject": "Project collaboration",
    "from": " partner@organization.org ",
    "to": "  lead_dev@icloud.com ",
    "body": "Hello,\nWe are interested in a partnership.\tPlease reply soon.\nRegards,\nTeam"
}
]
##2. **Добавьте дату отправки**: создайте переменную `send_date` как текущую дату в формате `YYYY-MM-DD` и запишите её в
##   `email["date"]`.
##   https://www.w3schools.com/python/python_datetime.asp
send_date = datetime.datetime.now().strftime("%Y-%m-%d")
email["date"] = send_date
##3. **Нормализуйте e-mail адреса** отправителя и получателя: приведите к нижнему регистру и уберите пробелы по краям.
##   Запишите обратно в `email["from"]` и `email["to"]`.
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

##4. **Извлеките логин и домен отправителя** в две переменные `login` и `domain`.
login, domain = email["from"].split('@')

##5. **Создайте сокращённую версию текста**: возьмите первые 10 символов `email["body"]` и добавьте многоточие `"..."`.
##   Сохраните в новый ключ словаря: `email["short_body"]`.
body_for_short = email["body"].strip() if email["body"].strip() else ""
if len(body_for_short) >= 10:
    short_body = body_for_short[:10] + "..."
else:
    short_body = body_for_short + "..." if body_for_short else "..."
email["short_body"] = short_body

##6. **Списки доменов**: создайте список личных доменов
##   `['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']`
##   и список корпоративных доменов
##   `['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']`.
##   с учетом того что там должны быть только уникальные значение
personal_domains = list(set(['gmail.com','list.ru','yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru']))
corporate_domains = list(set(['company.ru','corporation.com','university.edu','organization.org','company.ru','business.net']))
##7. **Проверьте что в списке личных и корпоративных доменов нет пересечений**: ни один домен не должен входить в оба
   списка одновременно.
intersection = set(personal_domains) & set(corporate_domains)
if intersection:
    print(f"Внимание! Найдены пересекающиеся домены: {intersection}")
else:
    print("Пересечений доменов нет.")

##8. **Проверьте «корпоративность» отправителя**: создайте булеву переменную `is_corporate`, равную результату проверки
   вхождения домена отправителя в список корпоративных доменов.
is_corporate = domain in corporate_domains

##9. **Соберите «чистый» текст сообщения** без табов и переводов строк: замените `"\t"` и `"\n"` на пробел.
##   Сохраните в `email["clean_body"]`.
clean_body = email["body"].replace('\t', ' ').replace('\n', ' ')

##10. **Сформируйте текст отправленного письма** многострочной f-строкой и сохраните в `email["sent_text"]`:

##`Кому: {получатель}, от {отправитель}
##Тема: {тема письма}, дата {дата}
##{чистый текст сообщения}`
email["sent_text"] = f"""Кому: {email['to']}, от {email['from']}
Тема: {email['subject'].strip()}, дата {email['date']}
{email['clean_body']}"""

##11. **Рассчитайте количество страниц печати** для `email["sent_text"]`, если на 1 страницу помещается 500 символов.
##    Сохраните результат в переменную `pages`. Значение должно быть округленно в большую сторону
sent_text_length = len(email["sent_text"])
pages = math.ceil(sent_text_length / 500)

##12. **Проверьте пустоту темы и тела письма**: создайте переменные  `is_subject_empty, is_body_empty ` в котором будет
##    хранится что тема письма содержит данные. Пустая строка, это не только строка без символов, но и строка, состоящая только из пробелов.
is_subject_empty = len(email["subject"].strip()) == 0
is_body_empty = len(email["body"].strip()) == 0

##13. **Создайте «маску» e-mail отправителя**: первые 2 символа логина + `"***@"` + домен.
##    Запишите в `email["masked_from"]`.
masked_login = login[:2] + "***"
email["masked_from"] = f"{masked_login}@{domain}"

##14. **Удалите из списка личных доменов** значения `"list.ru"` и `"bk.ru"`.
personal_domains = [d for d in personal_domains if d not in ['list.ru', 'bk.ru']]


print("=== РЕЗУЛЬТАТЫ ОБРАБОТКИ ===")
print(f"Нормализованный from: {email['from']}")
print(f"Нормализованный to: {email['to']}")
print(f"Логин: {login}, Домен: {domain}")
print(f"Сокращённое тело: {email['short_body']}")
print(f"Личные домены (после удаления): {personal_domains}")
print(f"Корпоративные домены: {corporate_domains}")
print(f"Отправитель корпоративный? {is_corporate}")
print(f"Чистое тело: {email['clean_body']}")
print(f"Текст письма:\n{email['sent_text']}")
print(f"Длина текста письма: {sent_text_length} символов")
print(f"Количество страниц: {pages}")
print(f"Тема пуста? {is_subject_empty}")
print(f"Тело пусто? {is_body_empty}")
print(f"Маска email: {email['masked_from']}")
print("\nИтоговый словарь email:")
for k, v in email.items():
    print(f"  {k}: {repr(v)}")