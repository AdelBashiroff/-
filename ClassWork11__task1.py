class Animal:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print('Недопустимое значение')

    def speak(self):
        print('Звук')

    def display_info(self):
        print(f'Имя: {self.name}, Возраст: {self.age}')

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print('Гав')

    def display_info(self):
        super().display_info()
        print(f'Порода: {self.breed}')

dog = Dog('Имя', 6, 'Бульдог')
dog.speak()
dog.display_info()