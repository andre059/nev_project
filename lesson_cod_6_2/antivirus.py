virus_cod = "Я вирус"

with open("answers.py", encoding='utf-8') as file:
        content = file.read()

        if virus_cod in content:
            print("Вирус обнаружен")

        else:
            print("Все хорошо, вирусов нет")