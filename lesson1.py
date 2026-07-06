import re
import pathlib
from datetime import datetime

#1Создайте словарь
def test_create_email_dict():
 email = {
  "subject": "Тестовое письмо",
  "from": "sun@mail.ru",
  "to": "rep@mail.ru",
  "body": "Это тело письма.",
  "date": datetime.now().strftime("%Y-%m-%d") #2Добавьте дату отправки
 }

#3Нормализуйте e-mail адреса
 email["from"] = email["from"].strip().lower()
 email["to"] = email["to"].strip().lower()

#4 Извлеките логин и домен отправителя
 login = email["from"].split("@")[0]
 domain = email["from"].split("@")[1]

#5Создайте сокращённую версию текста
 send_date = email["date"]
 email["short_body"] = email["body"][:10] + "..."

#6Списки доменов
 personal_domains = list(set(['gmail.com', 'list.ru', 'yahoo.com', 'outlook.com','hotmail.com', 'icloud.com', 'yandex.ru', 'mail.ru','list.ru', 'bk.ru', 'inbox.ru']))
 corporate_domains = list(set(['company.ru', 'corporation.com', 'university.edu','organization.org', 'company.ru', 'business.net']))
 personal_set = set(personal_domains)
 corporate_set = set(corporate_domains)
 #7Проверьте что в списке личных и корпоративных доменов нет пересечений
 cross = list(set(personal_domains) & set(corporate_domains))
 is_cross_empty = not cross

 #8Проверьте «корпоративность» отправителя
 is_corporate = personal_domains in corporate_domains

 #9Соберите «чистый» текст сообщения
 clean_body = email["body"].replace("\t", " ").replace("\n", " ")
 email["clean_body"] = clean_body

 #10Сформируйте текст отправленного письма
 sent_text = f"""
 Кому: {email["to"]}
 От: {email["from"]}
 Тема: {email["subject"]}
 Дата: {email["date"]}
 {email["clean_body"]}
 """
 email["sent_text"] = sent_text

 #11Рассчитайте количество страниц печати
 pages = round((len(email["sent_text"]) + 499) // 500)
 email["pages"] = str(pages)

 #12Проверьте пустоту темы и тела письма
 is_subject_empty = not email["subject"]
 is_body_empty = not email["body"]
 #13Создайте «маску» e-mail отправителя
 masked_from = login[:2] + '***@' + domain
 email["masked_from"] = masked_from
 #14Удалите из списка личных доменов
 personal_domains_copy = list(set(personal_domains))
 personal_domains_copy.remove("list.ru")
 personal_domains_copy.remove("bk.ru")

#Для быстрой проверки

#print("Задание 1:", email)
#print("Задание 2:", email["date"])
#print("Задание 3:", email["from"], email["to"])
#print("Задание 4:", login, domain)
#print("Задание 5:", email["short_body"])
#print("Задание 6:", personal_domains,"\n", corporate_domains)
#print("Задание 7:", is_cross_empty)
#print("Задание 8:", is_corporate)
#print("Задание 9:", email["clean_body"])
#print("Задание 10:", email["sent_text"])
#print("Задание 11:", email["pages"])
#print("Задание 12:", is_subject_empty, is_body_empty)
#print("Задание 13:", email["masked_from"])
#print("Задание 14:", personal_domains_copy)
