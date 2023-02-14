import json
import random
from random import choice
# import requests as requests
# from storage_for_json import JSON_SOURCE
from basic_word import BasicWord


def load_random_word(file):
    with open('text.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

        # word_data = random.choice(data)
        # basic_word = BasicWord(word_data['word'], word_data['subwords'])

        # return basic_word


# load_random_word('text.json')


        #word = []

        for item in data:
            original_word = item['word']
            acceptable_words = item['subwords']
            basic_word = BasicWord(original_word, acceptable_words)

            #print(basic_word)

            #word.append(original_word)

        #random.shuffle(word)

        #print(original_word)
        #print(acceptable_words)
    return original_word, acceptable_words


load_random_word('text.json')


# basicword = BasicWord(original_word, acceptable_words)
# basicword = BasicWord(word, word)
# basicword = BasicWord(original_word=['word'], acceptable_words=['subwords'])
# print(basicword)

# - получит список слов с внешнего ресурса,
# - выберет случайное слово,
# - создаст экземпляр класса `BasicWord`,
# - вернет этот экземпляр.
