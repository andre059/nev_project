class Player:

    def __init__(self, user_name='', users_word=None):
        self.user_name = user_name  # имя пользователя

        if users_word is None:
            self.users_word = []  # слова пользователя
        else:
            self.users_word = users_word

    def __repr__(self):
        return f'Player(user_name={self.user_name}, user_words_used={self.users_word})'

    def get_user_name(self):
        """
        Возвращает имя пользователя
        :return: Возвращает str
        """
        return self.user_name

    def getting_number_words(self):
        """
        Получение количества использованных слов
        :return: Возвращает int
        """

        return len(self.users_word)

    def adding_word_used(self, word):
        """
        Добавление слова в использованные слова
        """

        self.users_word.append(word)

    def checking_use_word(self, word):
        """
        Проверка использования данного слова до этого
        :param word: Слово для проверки
        :return: Возвращает bool
        """

        return word in self.users_word

# player = Player('Василий')
# player.adding_word_used('рюкзак')
# player.adding_word_used('вешалка')
# player.adding_word_used('котелок')

# print(player)
# print(player.getting_number_words())
# print(player.checking_use_word('вешалка'))
# print(player.checking_use_word('труба'))
# print(player.checking_use_word('лампа'))
# print(player.checking_use_word('рюкзак'))
