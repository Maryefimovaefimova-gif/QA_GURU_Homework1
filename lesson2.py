from datetime import datetime


# 1.Нормализация email адресов
def normalize_addresses(value: str) -> str:
    return value.lower().strip()
# 2.Сокращенная версия тела письма
def add_short_body(email: dict) -> dict:
    short_body = email["body"][0:10] + "..."
    email["short_body"] = short_body
    return email
# 3.Очистка текста письма
def clean_body_text(body: str) -> str:
    return body.replace("\n", " ").replace("\t", " ").strip()

# 4.Формирование итогового текста письма
def build_sent_text(email: dict) -> str:
    sent_text = f"""Кому: {email['recipient']}, от {email['sender']}\nТема: {email['subject']}, дата {email['date']}\n{email['body']}"""
    return sent_text

# 5. Проверка пустоты темы и тела
def check_empty_fields(subject: str, body: str) -> tuple[bool, bool]:
    is_subject_empty = (subject.strip() == "")
    is_body_empty = (body.strip() == "")

    return is_subject_empty, is_body_empty
# 6.Маска email отправителя
def mask_sender_email(login: str, domain: str) -> str:
    return f"{login[0:2]}***@{domain}"

# 7. Проверка корректности email
def get_correct_email(email_list: list[str]) -> list[str]:

    lst = []
    for email in email_list:
        email = email.strip().lower()
        login, _, domain = email.partition("@")
        domain, _, _ = domain.partition(".")

        if login and domain:
            if "@" in email and email.endswith((".com", ".ru", ".net")):
                lst.append(email)
    return lst
# 8. Создание словаря письма
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    return {"recipient": recipient, "sender": sender, "subject": subject, "body": body}
# 9. Добавление даты отправки
def add_send_date(email: dict) -> dict:
    date = datetime.now().strftime("%Y-%m-%d")
    email["date"] = date
    return email
# 10. Получение логина и домена
def extract_login_domain(address: str) -> tuple[str, str]:
    return address.split("@")[0].strip(), address.split("@")[1].strip()


# --------- Part B ---------

def sender_email(recipient_list: list[str], subject: str, message: str, *, sender="default@study.com") -> list[dict]:
    #1 Проверить, что recipient_list не пустой.
    if not recipient_list:
        return []

    #2 Проверить корректность email отправителя и получателей через get_correct_email().
    recipient_list = get_correct_email(recipient_list)
    if not recipient_list:
        return []

    # 3 Проверить заполненность темы и тела письма
    is_subject_empty, is_body_empty = check_empty_fields(subject, message)

    if is_subject_empty is True or is_body_empty is True:
        return []

    # 4 Исключить отправку самому себе
    recipient_list = [recipient for recipient in recipient_list if recipient != sender]

    # 5 Нормализовать все текстовые данные
    subject = clean_body_text(subject)
    message = clean_body_text(message)

    for recipient in recipient_list:
        normalize_addresses(recipient)

    sender = normalize_addresses(sender)

    lst = []

    # 6 Создать письмо для каждого получателя
    for recipient in recipient_list:
        email = create_email(recipient=recipient, sender=sender, subject=subject, body=message)
    # 7 Добавить дату отправки
        add_send_date(email)
    # 8 Замаскировать email отправителя
        login, domain = extract_login_domain(sender)
        mask_sender = mask_sender_email(login=login, domain=domain)

        email["sender"] = mask_sender

    # 9 Создать короткую версию тела письма
        email = add_short_body(email)

    # 10 Сформировать итоговый текст письма функцией build_sent_text()
        email["sent_text"] = build_sent_text(email)

        lst.append(email)

    return lst
