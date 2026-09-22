"""Генератор паролей. Шаг 2: добавляем цифры и символы.

Отличие от шага 1 — один набор символов:
    chars = string.ascii_letters + string.digits + string.punctuation

Запуск:  python 02_password_symbols.py
"""

import random
import string

print("=== Генератор паролей ===")

length = int(input("Длина пароля: "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))
print(f"Твой пароль: {password}")