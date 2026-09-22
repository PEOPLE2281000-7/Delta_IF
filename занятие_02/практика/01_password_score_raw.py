"""Генератор паролей. Ветка feature-score-raw: оценка «наспех».

Отличия от конца занятия 1 — две вещи:
  1) check_strength() оценивает пароль только по длине (кривая логика);
  2) в меню добавился пункт «Оценить свой пароль» (№4), «Выйти» стал №5.

Потом эта ветка сливается в main БЕЗ конфликта (fast-forward),
а правильная feature-score заменит эту функцию на честную (см. 02, 03).

Запуск:  python 01_password_score_raw.py
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
    # наспех: оценим только по длине — так тоже бывает
    if len(password) >= 8:
        return "сильная"
    return "слабая"


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