virus_cod = 'print("Я вирус")'

with open("answers.py", "a", encoding='utf-8') as file:
    file.write(f"\n{virus_cod}\n")

   #print(file.read())

#print(virus_cod)
