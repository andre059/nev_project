from player import Player
from storage_for_json import JSON_SOURCE
from utils import load_random_word

if __name__ == '__main__':

    def main():
        """
        Пользователь вводит свое имя (убираются лишние знаки и меняется первая буква на заглавную)
        """

        name = input('Ввведите ваше имя\n').strip().title()
        player = Player(user_name=name)
        basic_word = load_random_word(JSON_SOURCE)

        """
        Программа выводит условия игры
        """

        print(f'Привет, {name}')  # Выводиться имя пользователя
        print(f'Составь {basic_word.counting_number_subwords()} '  # Сколько составить слов 
              f'слов из слова - {basic_word.get_original_word()}'  # Слово из которого нужно составлять слова
            f'\nСлова должны быть не короче 3 букв'
            f'\nЧтобы закончить игру, угадайте все слова или напишите "stop"'
            f'\nПоехали, ваше первое слово?')

        while player.getting_number_words() < basic_word.counting_number_subwords():
            """
            Основной цикл программы, 
            программа проверяет слова пользовотеля на правильность
            """

            user_input = input().strip().lower()

            if len(user_input) < 3:  # проверка длины слова
                print('слишком короткое слово')

            elif user_input in ('стоп', 'stop'):  # кодовое слово для завершения программы
                break

            elif player.checking_use_word(user_input):  # было ли введено уже такое слово
                print('Такое слово уже использовано')

            elif not basic_word.word_verification(user_input):  # содержиться слово в предлагаемом слове (bool)
                print('неверно')

            else:  # Все проверки пройдены
                print('верно')
                player.adding_word_used(user_input)

        print(f'Игра завершена, вы угадали {player.getting_number_words()} слов!')


    main()
