class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    def go_to(self, floor):
        if floor < 0:
            print('"Такого этажа не существует"')
        for i in range(1, floor + 1):
            if floor <= self.number_of_floors and floor > 0:
                print(i)
            else:
                print('"Такого этажа не существует"')
                break


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
