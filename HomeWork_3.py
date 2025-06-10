class Vehicle:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage

    # Геттеры и сеттеры
    def get_make(self):
        return self.__make

    def set_make(self, value):
        if isinstance(value, str) and value:
            self.__make = value

    def get_model(self):
        return self.__model

    def set_model(self, value):
        if isinstance(value, str) and value:
            self.__model = value

    def get_year(self):
        return self.__year

    def set_year(self, value):
        if isinstance(value, int) and value > 1800:
            self.__year = value

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__mileage = value

    def display_info(self):
        print(f"{self.__year} {self.__make} {self.__model}, пробег: {self.__mileage} км")

    def drive(self, miles):
        if isinstance(miles, (int, float)) and miles > 0:
            self.__mileage += miles


class Car(Vehicle):
    def __init__(self, make, model, year, mileage, number_of_doors):
        super().__init__(make, model, year, mileage)
        self.__number_of_doors = number_of_doors

    def get_number_of_doors(self):
        return self.__number_of_doors

    def set_number_of_doors(self, value):
        if isinstance(value, int) and 2 <= value <= 5:
            self.__number_of_doors = value

    def display_info(self):
        super().display_info()
        print(f"Количество дверей: {self.__number_of_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, mileage, has_sidecar):
        super().__init__(make, model, year, mileage)
        self.__has_sidecar = has_sidecar

    def get_has_sidecar(self):
        return self.__has_sidecar

    def set_has_sidecar(self, value):
        if isinstance(value, bool):
            self.__has_sidecar = value

    def display_info(self):
        super().display_info()
        print("С боковым прицепом" if self.__has_sidecar else "Без бокового прицепа")


class Truck(Vehicle):
    def __init__(self, make, model, year, mileage, payload_capacity, number_of_axles):
        super().__init__(make, model, year, mileage)
        self.__payload_capacity = payload_capacity
        self.__number_of_axles = number_of_axles

    def get_payload_capacity(self):
        return self.__payload_capacity

    def set_payload_capacity(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self.__payload_capacity = value

    def get_number_of_axles(self):
        return self.__number_of_axles

    def set_number_of_axles(self, value):
        if isinstance(value, int) and value > 0:
            self.__number_of_axles = value

    def display_info(self):
        super().display_info()
        print(f"Грузоподъемность: {self.__payload_capacity} кг")
        print(f"Количество осей: {self.__number_of_axles}")
