class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return self.brand + "(" + self.model + ")"


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража

    def __init__(self, *args):
        self.car_list = list(args)

    def __str__(self):
        out = ""
        for i in self.car_list:
            out += str(i) + "; "
        return out

    def add(self, car):
        self.car_list.append(car)

    def delete(self, index):
        self.car_list.pop(index)


car1 = Car('Reno', 'Capture')
car2 = Car('BMW', 'X6')
car3 = Car('Ford', 'Kuga')
car4 = Car('Mitsubishi', 'Lancer')


garage1 = Garage(car1, car2, car3)
print(garage1)

garage1.add(car4)
print(garage1)

garage1.delete(1)
print(garage1)
