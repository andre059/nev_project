class BasicWord:
    """
    Класс базовое слово, для игры:
    угадай какие слова входят в указанное слово слово
    """

    def __init__(self, original_word='', acceptable_words=None):
        self.original_word = original_word  # исходное слово

        if acceptable_words is None:
            self.acceptable_words = []  # набор допустимых подслов
        else:
            self.acceptable_words = acceptable_words

    def __repr__(self):

        return f'BasicWord(original_word={self.original_word}, acceptable_words={self.acceptable_words})'

    def get_original_word(self):
        """
        Возвращает исходное слово
        :return: Вернет в str
        """

        return self.original_word

    def counting_number_subwords(self):
        """
        Подсчет количества подслов
        :return: Вернет int
        """

        return len(self.acceptable_words)

    def word_verification(self, original_word):
        """
        Возвращает True если введенное слово есть в списке допустимых подслов
        :return: Вернет bool
        """

        return original_word in self.acceptable_words


#original_word = BasicWord(original_word='питон', acceptable_words=['тип', 'тон', 'пин'])

#print(original_word)
#print(original_word.counting_number_subwords())
#print(original_word.word_verification('пин'))
#print(original_word.word_verification('тил'))





