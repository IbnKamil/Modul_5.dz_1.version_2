# Модуль №5, Д/З №1
# ПРАКТИЧЕСКОЕ ЗАДАНИЕ
# 2023/10/25 00:00|Домашняя работа по уроку "Атрибуты и методы объекта."
# Цель: применить на практике знания о классах, объектах и их атрибутах.
#
# Задача "Developer - не только разработчик"


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1:
            print("Такого этажа не существует")
        elif new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            i = 1
            for i in range(1, new_floor + 1):
                print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)

h3 = House('Lagranda', 20)

h3.go_to(19)