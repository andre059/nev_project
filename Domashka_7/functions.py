import json

#s = int(input())

def load_students(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = json.load(f)

        #print(data)
    return data


def load_professions(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = json.load(f)

        #print(data)
    return data


def get_student_by_pk(pk, data):
    with open('student.json', 'r', encoding="UTF-8") as file:
        data = json.load(file)
        for student in data:
            if student['pk'] == s:
                student_join = ", ".join(student["skills"])

                print(f'Студент - {student["full_name"]} \nЗнает - {student_join}')
                return f'Студент - {student["full_name"]}\nЗнает - {student_join}'

        else:

            print('Студента под таким номером нет')
            return 'Студента под таким номером нет'




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

#user_neim = input()

def get_profession_by_title(title):
    with open('professions.json', 'r', encoding="UTF-8") as file:
        data = json.load(file)
        for get_professions in data:
            if get_professions['title'] == user_neim:
                get_professions_join = ", ".join(get_professions["skills"])

                print(get_professions_join)
        return get_professions_join


#get_profession_by_title(4)


#def check_fitness(student, student_join, get_professions_join, profession):
    #has_professions = student_join.intersection(get_professions_join)
    #unexplored_professions = get_professions_join.difference(student_join)
    #professional_aptitude = (len(has_professions) / len(unexplored_professions))*100

    #print(f'Имеет профессии {has_professions}'
          #f'Не знает {unexplored_professions}'
          #f'Пригодность {professional_aptitude}%')

