from functions import load_students, load_professions, get_student_by_pk, get_profession_by_title

if __name__ == "programma":
    file_students = "student.json"
    file_professions = "professions.json"

    #print(load_students(file_students))
    #print(load_professions(file_professions))

    s = int(input('Введите номер студента'))
    print(f'Студент - {name}'
        f'Знает - {knows_professions}')

    user_neim = input(f'Выберите специальность для оценки студента '
                  f'{name}')

def check_fitness(student, student_join, get_professions_join, profession):
    has_professions = student_join.intersection(get_professions_join)
    unexplored_professions = get_professions_join.difference(student_join)
    professional_aptitude = (len(has_professions) / len(unexplored_professions))*100

    print(f'Имеет профессии {has_professions}'
          f'Не знает {unexplored_professions}'
          f'Пригодность {professional_aptitude}%')
