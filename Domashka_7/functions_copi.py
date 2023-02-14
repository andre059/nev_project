import json


#def load_students(filename):
    #with open(filename, 'r', encoding="UTF-8") as f:
        #data = json.load(f)

    #return data


#def load_professions(filename):
    #with open(filename, 'r', encoding="UTF-8") as f:
        #data = json.load(f)

    #return data

student_number = int(input('Введите номер студента'))

#professions = ()
#student = ()

def get_student_by_pk(s):

    """" Что знает студент по данной специальности """

    with open('student.json', 'r', encoding="UTF-8") as file:
        data = json.load(file)
        for student in data:
            if student['pk'] == s:
                professions = ", ".join(student["skills"])

                print(f'Студент - {student["full_name"]}\nЗнает - {professions}')
                return f'Студент - {student["full_name"]}\nЗнает - {professions}'


        else:
            print('Студента под таким номером нет')
            return 'Студента под таким номером нет'


get_student_by_pk(student_number)

#def load_professions(data_7):
    #with open('student.json', 'r', encoding="UTF-8") as file:
        #data = json.load(file)
        #for student in data:
            #if student['pk'] == s:

                #print(student["skills"])
                #return student["skills"]

        #else:
            #print()
            #return

user_name = input(f'Выберите специальность для оценки студента')


def get_profession_by_title(title):

    """" Выбор язаков данной специальности """

    with open('professions.json', 'r', encoding="UTF-8") as file:
        data = json.load(file)
        for get_professions in data:
            if get_professions['title'] == user_name:
                professions_join = ", ".join(get_professions["skills"])

                return professions_join


get_profession_by_title(user_name)


def check_fitness(prof, student_prof):

    """" Подсчет данных студента """
    set_prof = set(prof)
    set_student_prof = set(student_prof)

    has_professions = set_prof.intersection(set_student_prof)
    unexplored_professions = set_student_prof.difference(set_prof)

    professional_aptitude = round(len(has_professions) / len(unexplored_professions) * 100)

    y = list(has_professions)
    z = list(unexplored_professions)

    print(f'Имеет профессии {y}\n'
          f'Не знает {z}\n'
          f'Пригодность {professional_aptitude}%')

    #return f'Имеет профессии {", ".join(has_professions)} ' \
           #f'Не знает {", ".join(unexplored_professions)}'  \
           #f'Пригодность {professional_aptitude}%'


check_fitness(professions_join, professions)
