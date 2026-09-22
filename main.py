"""Генератор паролей. Шаг 1: пароль из букв.

Запуск:  python 01_password_letters.py
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