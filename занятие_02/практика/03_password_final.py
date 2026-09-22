"""Генератор паролей. Эталон после merge веток на занятии 2.

Состав:
  - вся история занятия 1 (буквы → символы → выбор набора → файл);
  - пункт «Оценить свой пароль» (после merge raw и правильной веток
    осталась честная check_strength по баллам);
  - README на главной ветке.

«Готовый» вид меню: 1 Буквы / 2 Буквы и цифры / 3 Все символы /
4 Оценить свой пароль / 5 Выйти.

Запуск:  python 03_password_final.py
"""

import random
import string

ALPHABETS = {
    "1": string.ascii_letters,
    "2": string.ascii_letters + string.digits,
    "3": string.ascii_letters + string.digits + string.punctuation,
}


def generate_password(length, alphabet):
    """Собирает случайный пароль нужной длины из переданного алфавита."""
    return "".join(random.choice(alphabet) for _ in range(length))


def check_strength(password):
    """Возвращает «слабая», «средняя» или «сильная» для пароля."""
    length = len(password)
    has_digits = any(ch.isdigit() for ch in password)
    has_letters = any(ch.isalpha() for ch in password)
    has_symbols = any(not ch.isalnum() for ch in password)

    score = sum([has_digits, has_letters, has_symbols, length >= 8])

    if score <= 1:
        return "слабая"
    if score <= 3:
        return "средняя"
    return "сильная"


def save_password(password):
    """Дописывает пароль в файл passwords.txt."""
    with open("passwords.txt", "a", encoding="utf-8") as f:
        f.write(password + "\n")


def main():
    while True:
        print("\n=== Генератор паролей ===")
        print("1. Буквы")
        print("2. Буквы и цифры")
        print("3. Все символы")
        print("4. Оценить свой пароль")
        print("5. Выйти")

        choice = input("Выбери действие: ")

        if choice == "5":
            print("Пока!")
            break

        if choice == "4":
            password = input("Введи пароль: ")
            print(f"Сложность: {check_strength(password)}")
            continue

        if choice not in ALPHABETS:
            print("Не понял команду. Попробуй ещё раз.")
            continue

        length = int(input("Длина пароля: "))
        password = generate_password(length, ALPHABETS[choice])
        print(f"Твой пароль: {password}")

        if input("Сохранить в файл? (д/н): ").strip().lower() == "д":
            save_password(password)
            print("Пароль сохранён в passwords.txt.")


if __name__ == "__main__":
    main()