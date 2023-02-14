from utils import load_students, load_professions, get_student_by_pk, get_profession_by_title, check_fitness, show_result

if __name__ == '__main__':

    '''' Переменные с данными студента и данными профессий '''

    file_students = 'student.json'
    file_professions = 'professions.json'

    '''' Вызов функций для загрузки данных студента и профессий '''

    data_students = load_students(file_students)
    data_professions = load_professions(file_professions)

    '''' Ввод и получение студента по pk '''

    pk = int(input('Введите номер студента: '))
    student = get_student_by_pk(pk, data_students)

    if student:
        print(f'Студент: {student["full_name"]}')
        str_skills = ', '.join(student["skills"])
        print(f'Знает: {str_skills}')
    else:
        print(f'У нас нет такого студента')
        quit()

    '''' Получение профессий по названию '''

    title = input('Выберете специальность для оценки студента: ')
    profession = get_profession_by_title(title, data_professions)

    if not profession:
        print(f'У нас нет такой специальностьи')
        quit()

    '''' находим необходимый результат с помощью метода множества '''

    data = check_fitness(student, profession)
    print(show_result(data, student['full_name']))
