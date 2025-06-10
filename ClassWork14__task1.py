from abc import ABC, abstractmethod
class Profession(ABC):
    @abstractmethod
    def work(self):
        pass

class Doctor(Profession):
    def work(self):
        return "Лечу пациентов."

class Teacher(Profession):
    def work(self):
        return "Преподаю уроки."

def perform_work(professions):
    for profession in professions:
        print(profession.work())

people = [Doctor(), Teacher(), Doctor()]
perform_work(people)