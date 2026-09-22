"""Генератор паролей. Шаг 1: пароль из букв.

Запуск:  python 01_password_letters.py
"""

import random
import string

print("=== Генератор паролей ===")

length = int(input("Длина пароля: "))
password = "".join(random.choice(string.ascii_letters) for _ in range(length))
print(f"Твой пароль: {password}")