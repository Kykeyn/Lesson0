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
        return self.number_of_floors == other

    def __lt__(self, other):
        return self.number_of_floors < other

    def __gt__(self, other):
        return self.number_of_floors > other

    def __le__(self, other):
        return self.number_of_floors <= other

    def __ge__(self, other):
        return self.number_of_floors >= other

    def __ne__(self, other):
        return self.number_of_floors != other

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __add__(self, other):
        self.number_of_floors = self.number_of_floors + other
        return self

    def __radd__(self, other):
        self.number_of_floors = self.number_of_floors + other
        return self

    def __iadd__(self, other):
        self.number_of_floors += other
        return self

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
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)