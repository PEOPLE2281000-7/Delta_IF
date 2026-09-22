"""Генератор паролей. Шаг 4: меню, выбор набора и сохранение в файл.

Эталон конца занятия 1. После запуска появляется файл passwords.txt
(личные данные — его исключаем из git через .gitignore).

Запуск:  python 04_password_save.py
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
        print("4. Выйти")

        choice = input("Выбери действие: ")

        if choice == "4":
            print("Пока!")
            break

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