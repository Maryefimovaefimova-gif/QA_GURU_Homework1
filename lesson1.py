from datetime import date
import re


# Нормализация email адресов
def normalize_addresses(value: str) -> str:
    """
    Нормализует email адрес: удаляет пробелы и приводит к нижнему регистру.
    """
    if not value:
        return ""
    # Удаляем пробелы и приводим к нижнему регистру
    return value.strip().lower()


# Сокращенная версия тела письма
def add_short_body(email: dict) -> dict:
    """
    Добавляет сокращенную версию тела письма (первые 50 символов).
    """
    if not email or 'body' not in email:
        return email

    body = email.get('body', '')
    # Берем первые 50 символов, если тело длиннее, добавляем многоточие
    short_body = body[:50] + ('...' if len(body) > 50 else '')
    email['short_body'] = short_body
    return email


# Очистка текста письма
def clean_body_text(body: str) -> str:
    """
    Заменяет табы и переводы строк на пробелы.
    """
    if not body:
        return ""

    # Заменяем табы и переводы строк на пробелы
    cleaned = body.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    # Удаляем множественные пробелы
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()


# Формирование итогового текста письма
def build_sent_text(email: dict) -> str:
    """
    Формирует текст письма в формате:

    Кому: {to}, от {from}
    Тема: {subject}, дата {date}
    {clean_body}
    """
    sender = email.get('sender', 'неизвестно')
    recipient = email.get('recipient', 'неизвестно')
    subject = email.get('subject', 'Без темы')
    body = email.get('body', '')
    date_sent = email.get('date', date.today().strftime('%Y-%m-%d'))

    # Очищаем тело письма
    clean_body = clean_body_text(body)

    # Формируем текст письма
    result = f"Кому: {recipient}, от {sender}\n"
    result += f"Тема: {subject}, дата {date_sent}\n"
    result += clean_body

    return result


# Проверка пустоты темы и тела
def check_empty_fields(subject: str, body: str) -> tuple[bool, bool]:
    """
    Возвращает кортеж (is_subject_empty, is_body_empty).
    True, если поле пустое.
    """
    is_subject_empty = not bool(subject and subject.strip())
    is_body_empty = not bool(body and body.strip())
    return (is_subject_empty, is_body_empty)


# Маска email отправителя
def mask_sender_email(login: str, domain: str) -> str:
    """
    Возвращает маску email: первые 2 символа логина + "***@" + домен.
    """
    if not login:
        return f"***@{domain}" if domain else ""

    # Если логин короче 2 символов, маскируем полностью
    if len(login) <= 2:
        masked_login = login[0] + '*' if len(login) == 2 else '*'
    else:
        masked_login = login[:2] + "***"

    return f"{masked_login}@{domain}"


# Получение корректных email
def get_correct_email(email_list: list[str]) -> list[str]:
    """
    Возвращает список корректных email.
    """
    if not email_list:
        return []

    # Простой паттерн для проверки email
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    correct_emails = []

    for email in email_list:
        if email and isinstance(email, str):
            normalized = normalize_addresses(email)
            if email_pattern.match(normalized):
                correct_emails.append(normalized)

    return correct_emails


# Создание словаря письма
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    """
    Создает словарь email с базовыми полями:
    'sender', 'recipient', 'subject', 'body'
    """
    # Нормализуем email адреса
    sender_normalized = normalize_addresses(sender)
    recipient_normalized = normalize_addresses(recipient)

    return {
        'sender': sender_normalized,
        'recipient': recipient_normalized,
        'subject': subject or 'Без темы',
        'body': body or ''
    }


# Добавление даты отправки
def add_send_date(email: dict) -> dict:
    """
    Возвращает email с добавленным ключом email["date"] — текущая дата в формате YYYY-MM-DD.
    """
    if not email:
        return email

    current_date = date.today().strftime('%Y-%m-%d')
    email['date'] = current_date
    return email


# Получение логина и домена
def extract_login_domain(address: str) -> tuple[str, str]:
    """
    Возвращает логин и домен отправителя.
    Пример: "user@mail.ru" -> ("user", "mail.ru")
    """
    if not address or '@' not in address:
        return ("", "")

    parts = address.split('@', 1)
    return (parts[0], parts[1])
# Создаем письмо
email = create_email(
    sender="user@mail.ru",
    recipient="friend@gmail.com",
    subject="Привет!",
    body="Это тестовое письмо.\nС новой строки.\tС табуляцией."
)

# Добавляем дату
email = add_send_date(email)

# Добавляем сокращенную версию
email = add_short_body(email)

# Получаем логин и домен
login, domain = extract_login_domain(email['sender'])
print(f"Логин: {login}, Домен: {domain}")

# Маскируем email
masked = mask_sender_email(login, domain)
print(f"Маскированный email: {masked}")

# Формируем текст письма
text = build_sent_text(email)
print(text)

# Проверяем поля
is_subject_empty, is_body_empty = check_empty_fields(email['subject'], email['body'])
print(f"Тема пуста: {is_subject_empty}, Тело пусто: {is_body_empty}")

# Проверка корректных email
emails = ["user@mail.ru", "invalid-email", "test@gmail.com", "another@test"]
correct = get_correct_email(emails)
print(f"Корректные email: {correct}")
