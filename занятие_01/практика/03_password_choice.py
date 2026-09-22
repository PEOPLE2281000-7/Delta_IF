"""Генератор паролей. Шаг 3: выбор набора символов.

Пользователь выбирает набор:
    1 — только буквы;
    2 — буквы и цифры;
    3 — буквы, цифры и символы.

Запуск:  python 03_password_choice.py
"""

import random
import string

ALPHABETS = {
    "1": string.ascii_letters,
    "2": string.ascii_letters + string.digits,
    "3": string.ascii_letters + string.digits + string.punctuation,
}

print("=== Генератор паролей ===")
print("1. Буквы")
print("2. Буквы и цифры")
print("3. Все символы")

mode = input("Выбери набор: ")
length = int(input("Длина пароля: "))

password = "".join(random.choice(ALPHABETS[mode]) for _ in range(length))
print(f"Твой пароль: {password}")