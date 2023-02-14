row_index = 0
items_count = 0
items_som = 0

with open('shopping_list.txt', encoding='utf-8') as file:
    for item_data in file:
        row_index += 1
        if item_data.count(":") < 2:
            print(f"В строке {row_index} есть ошибка")
            continue

        item, quantity, price = item_data.strip().split(":")
        items_count += 1
        items_som += int(price) * int(quantity)

print(f"в списке {items_count} позиций. Сумма {items_som} р.")