answer = 0
max_record = []
items_count = 0


user_nem = input("������� ���� ���")  # ���� ������ ������������


with open("words.txt", "r", encoding='utf-8') as file:
    import random

    """������������� ���� � ����� � ���������� �� �������������"""

    for line in file:
        line = line.rstrip("\n")
        items = "".join(random.sample(line, len(line)))

        print(f"�������� ����� {items}")

        user = input()

        if user.lower().strip(" ") == line:
            answer += 10

            print("�����! �� ��������� 10 �����.")

        else:
            print(f"�������! ������ ����� � {line}")


with open("history.txt", "a", encoding='utf-8') as file:
    file.write(f"{user_nem}:{answer}\n")

    """������ ������"""


with open("history.txt", "r", encoding='utf-8') as file:

    """������ � ����� (������� �������� ��� � ������������ ������)"""

    for item_data in file:
        name, scores = item_data.strip().split(":")
        max_record.append(scores)
        items_count += 1

    print(f"\n����� ��� �������:{items_count}")
    print(f"������������ ������:{max(max_record)}")
