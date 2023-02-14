class Question:

    def __init__(self, question_text, complexity_question, correct_answer):
        self.question_text = question_text
        self.complexity_question = complexity_question
        self.correct_answer = correct_answer

        self.question = False
        self.user_response = None
        self.points_question = self.complexity_question * 10


    def get_points(self):

        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """

        return self.points_question


    def is_correct(self):

        """Возвращает True, если ответ пользователя совпадает
        с верным ответом, иначе False.
        """

        return self.correct_answer == self.user_response


    def build_question(self):

        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f'\nВопрос: {self.question_text} \nСложность {self.complexity_question}/5'

    def build_positive_feedback(self):

        """Возвращает :
        Ответ верный, получено __ баллов
        """

        if self.is_correct():
            return f'Ответ верный, получено {self.points_question} баллов'
        else:
            return f'Ответ неверный, верный ответ {self.correct_answer}'
