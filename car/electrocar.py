
# from car import carclass  # вначале имя пакета - импорт - имя модуля
from car.carclass import CarClass
# А можно из имя пакета.имя модуля - импорт - имя класса (CarClass)


# class ElectroCar(carclass.CarClass):  # имя модулю.имя класса
class ElectroCar(CarClass):
    def __init__(self, brand, model, year, run):
        super().__init__(brand, model, year, run)
        self.battery = 100

    def description_battery(self):
        print(f"Этот автомобиль имеет мощность {self.battery} %")
