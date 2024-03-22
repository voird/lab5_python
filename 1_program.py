import re

def validate_phone_number(phone_number):
    pattern = r'^(\+?7|8)?[\s-]?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{2}[\s-]?\d{2}$'
    return bool(re.match(pattern, phone_number))

def get_phone_number(phone_number):

    if validate_phone_number(phone_number):
        return phone_number
    else:
        raise ValueError("Некорректный телефонный номер")

phone = input()

try:
    validated_phone = get_phone_number(phone)
    print("Введенный номер:", validated_phone)
except ValueError as e:
    print(e)
