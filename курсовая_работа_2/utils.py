import random
import requests as requests

from basic_word import BasicWord
from storage_for_json import JSON_SOURCE


def load_random_word(json_source):
    """
    Принимаются данные со стороннего ресурса, рандомно выбираются данные
    (слово выводимое для пользователя и проверочные слова)
    :param json_source: //jsonkeeper.com/b/9UTY
    :return: Вывод данных для класса слова
    """

    result = requests.get(json_source, verify=False)
    result_data = result.json()

    word_data = random.choice(result_data)

    basic_word = BasicWord(word_data['word'], word_data['subwords'])

    return basic_word


print(load_random_word(JSON_SOURCE))
