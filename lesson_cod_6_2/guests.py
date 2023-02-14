guests_count = 0

with open('guests.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        print(line)
        guests_count += 1

print(f"количество гостей = {guests_count}")