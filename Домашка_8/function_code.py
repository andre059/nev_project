import json
from question import Question

def load_question(filename):

    """
    Задаем данные классу Question
    :param filename:
    :return:
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    questions = []

    for item in data:
        question_text = item['q']
        correct_answer = item['a']
        complexity_question = int(item['d'])
        question = Question(question_text, complexity_question, correct_answer)

        questions.append(question)

    return questions


def counting(questions):

    """
    Подсчет баллов и сколько отвечено вопросов правильно
    :param questions:
    :return:
    """
    number_points = 0
    correct_answered_questions = 0

    for question in questions:
        if question.is_correct():
            number_points += question.points_question
            correct_answered_questions += 1

    return f'\nВот и все: \n' \
           f'Вы ответили на {correct_answered_questions} вопросов правильно \n'\
           f'Набрали {number_points} баллов'


