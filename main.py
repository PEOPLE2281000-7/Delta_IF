"""Генератор паролей. Шаг 1: пароль из букв.

Запуск:  python 01_password_letters.py
"""

import random
import string

print("=== Генератор паролей ===")

length = int(input("Длина пароля: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))
print(f"Твой пароль: {password}")