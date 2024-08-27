class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, floor):
        if floor <= 0:
            print('"Такого этажа не существует"')
        for i in range(1, floor + 1):
            if floor <= self.number_of_floors:
                print(i)
            else:
                print('"Такого этажа не существует"')
                break


h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 8)
h1.go_to(5)
h2.go_to(10)
