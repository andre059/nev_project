raw_list = ["сельдь-черноспинка", "морская камбала", "тунец", "ставрида", "морской окунь", "треска", "сайра",
"морская камбала", "ставрида", "треска", "треска", "треска", "тунец", "ставрида", "морская камбала",
"тунец", "морская камбала", "морская камбала", "морская камбала", "морская камбала", "тунец",
           ]

unique_raw_list = list(set(raw_list))
print(f"Всего {len(unique_raw_list)} видов рыб")

unique_raw_list.sort()

for unique_list in unique_raw_list:

    print(unique_list)

    #unique_list = list(set(raw_list))

    #unique_list.sort()