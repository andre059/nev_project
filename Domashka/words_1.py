answer = 0
max_record = []
items_count = 0


user_nem = input("Введите ваше имя")  # Ввод данных пользователя


with open("words.txt", "r", encoding='utf-8') as file:
    import random

    """перемешивание букв в слове и угадывание их пользователем"""

    for line in file:
        line = line.rstrip("\n")
        items = "".join(random.sample(line, len(line)))

        print(f"Угадайте слово {items}")

        user = input()

        if user.lower().strip(" ") == line:
            answer += 10

            print("Верно! Вы получаете 10 очков.")

        else:
            print(f"Неверно! Верный ответ – {line}")


with open("history.txt", "a", encoding='utf-8') as file:
    file.write(f"{user_nem}:{answer}\n")

    """Запись данных"""


with open("history.txt", "r", encoding='utf-8') as file:

    """подщет и вывод (сколько сыгранно игр и максимальный рекорд)"""

    for item_data in file:
        name, scores = item_data.strip().split(":")
        max_record.append(scores)
        items_count += 1

    print(f"\nВсего игр сыграно:{items_count}")
    print(f"Максимальный рекорд:{max(max_record)}")
