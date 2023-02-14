class Room:

    def __init__(self, number, is_free):
        self.number = number
        self.is_free = is_free


def get_free_rooms(rooms):
    free_rooms = []
    for i in rooms:
        if i.is_free == True:
            free_rooms.append(i)

    return free_rooms


rooms = [Room(14, True), Room(15, False), Room(16, True)]
rooms_free = get_free_rooms(rooms)

# Не удаляйте этот код, он нужен для проверки

#for r in rooms_free:
#print(rooms_free)
#print(r.number)
[print(r.number) for r in rooms_free]
