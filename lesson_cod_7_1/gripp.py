employees = [

 {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
 {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
 {"fio": "Аверин Мартын Егорович", "vaccinated": True},
 {"fio": "Князева Августа Егоровна", "vaccinated": False},
 {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
 {"fio": "Куприна Марина Викторовна", "vaccinated": False},
 {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},
]


vaccinated = []
not_vaccinated = []

for word in employees:
    if word["vaccinated"] == True:
        vaccinated.append(word["fio"])
    else:
        not_vaccinated.append(word["fio"])

vaccin = '\n'.join(vaccinated)
not_vaccin = '\n'.join(not_vaccinated)

print(f"Вакцинированные:\n{vaccin}")
print(f"Остальные:\n{not_vaccin}")

