##Flight from ____ to ____
#class Flight:

    #def __init__(self, city_from, city_to):
        #self.city_from = city_from
        #self.city_to = city_to

    #def __str__(self):
        #return f"Flight from {self.city_from} to {self.city_to}"

# Не удаляйте текст ниже, он нужен для проверки

#print(Flight(input(), input()))


class Flight:

    def __init__(self, city_from, city_to):
        self.city_from = city_to
        self.city_to = city_to

    def __repr__(self):
        return f"Flight (city_from='{self.city_from}', city_to='{self.city_to}')"

# Не удаляйте текст ниже, он нужен для проверки

print(Flight(input(), input()))