import random

from function_code import load_question, counting

if __name__ == '__main__':

    filename = 'questions.json'
    questions = load_question(filename)

    random.shuffle(questions)  # Перемешивание вопросов

    input('Игра начинается! Нажмите ввод!')

    for issue in questions:

        print(issue.build_question())  # Вывод вопроса
        user_input = input('Ваш ответ: ')

        issue.user_response = user_input  # Проверка ответа
        print(issue.build_positive_feedback())

    print(counting(questions))  # Вывод данных функции подсчета
