class House:
    # Метод __init__ для инициализации объекта с именем и количеством этажей
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # Метод go_to для перемещения на новый этаж
    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")


# Исходные данные
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызов метода go_to
h1.go_to(5)  # Ожидаемый результат: вывод от 1 до 5
h2.go_to(10)  # Ожидаемый результат: "Такого этажа не существует"
