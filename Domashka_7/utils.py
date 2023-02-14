import json

"""" Згрузка данных студентов """

def load_students(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = json.load(f)

    return data


"""" Згрузка данных профессий """

def load_professions(filename):
    with open(filename, 'r', encoding="UTF-8") as f:
        data = json.load(f)

    return data


"""" Получение студента по pk """

def get_student_by_pk(pk, data):
    for item in data:
        if pk == item['pk']:
            return item


"""" Получение профессий по названию """

def get_profession_by_title(title, data):
    for item in data:
        if title == item['title']:
            return item


"""" С равнение данных студента с запрашиваемой специальностью """

def check_fitness(student, profession):

    set_student = set(student['skills'])
    set_profession = set(profession['skills'])

    has_skills = set_student.intersection(set_profession)
    lask_skills = set_profession.difference(set_student)

    fit_percent = round(len(has_skills)/len(set_profession) * 100)

    dict_result = {
            'has': has_skills,
            'lacks': lask_skills,
            'fit_percent': fit_percent,
    }

    return dict_result


"""" Вывод результатов """

def show_result(data, name):
    str_has = ', '.join(data['has'])
    str_lacks = ', '.join(data['lacks'])
    str_output = f'Пригодность: {data["fit_percent"]}%\n' \
                 f'{name} Знает: {str_has}\n' \
                 f'{name} Не знает: {str_lacks}'

    return str_output


