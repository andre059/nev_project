fish = [
{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for Pisces in fish:
    if Pisces["water"] == "sea":
        sea_water.append(Pisces["specie"])
        i = ", ".join(sea_water)
    else:
        fresh_water.append(Pisces["specie"])
        x = ", ".join(fresh_water)

print(f"Морские: {i}")
print(f"Пресноводные: {x}")
