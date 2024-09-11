class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args)
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.houses_history = []

    def __del__(self):
        return print(f'{self.name} снесён, но он останется в истории')

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors < other

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        elif isinstance(other, House):
            return self.number_of_floors > other

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors <= other
        elif isinstance(other, House):
            return self.number_of_floors <= other

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other
        elif isinstance(other, House):
            return self.number_of_floors >= other

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other
        elif isinstance(other, House):
            return self.number_of_floors != other

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other
            return self
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            return 'Ошибка'

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            return "Ошибка"

    def __iadd__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other
            return self
        elif isinstance(other, int):
            self.number_of_floors += other
            return self
        else:
            return "Ошибка"

    def go_to(self, floor):
        if floor <= 0:
            print('"Такого этажа не существует"')
        for i in range(1, floor + 1):
            if floor <= self.number_of_floors:
                print(i)
            else:
                print('"Такого этажа не существует"')
                break


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
