# Программа описывает персонажей серии романов о Гарри Поттере
class House:
    # Имя факультета
    def __init__(self, name):
        self.name = name
        self.points = 0

    # Изменение количества очков
    def change_points(self):
        new_point = int(input())
        self.points += new_point

    # Вывод данных по факультету
    def show_house(self):
        description = (self.name + " points: " + str(self.points).title())
        print(description)


# Класс учеников, которые когда-либо обучались в Хогвартсе
class Hogwarts:
    def __init__(self, name, house):
        self.name = name
        self.house = house


# Следующие классы наследуют функции класса Hogwarts
class Student(Hogwarts):
    # Имя ученка, факультет, на котором он обучается, его курс
    def __init__(self, name, house, course):
        super().__init__(name, house)
        self.course = course

    # Вывод данных ученика
    def show_character(self):
        return "Name: " + self.name + " House: " + self.house + " Course: " + self.course


class Professor(Hogwarts):
    # Имя профессора, факультет, на котором он обучался, предмет, который он ведёт
    def __init__(self, name, house, subject):
        super().__init__(name, house)
        self.subject = subject

    # Вывод данных
    def show_character(self):
        return "Name: " + self.name + " House: " + self.house + " Subject: " + self.subject


class DeathEater(Hogwarts):
    #  Имя Пожирателя смерти, факультет, на котором он обучался
    def __init__(self, name, house):
        super().__init__(name, house)

    # Вывод данных
    def show_character(self):
        return "Name: " + self.name + " House: " + self.house


class OrderOfThePhoenix(Hogwarts):
    # Имя члена Ордена феникса, факультет, на котором он обучался
    def __init__(self, name, house):
        super().__init__(name, house)

    # Вывод данных
    def show_character(self):
        return "Name: " + self.name + " House: " + self.house


# Вывод описания персонажей с помощью полиморфизма
s = Student("Harry Potter", "Griffindor", "2")
p = Professor("Minerva McGonagall", "Griffindor", "Transfiguration")
de = DeathEater("Lucius Malfoy", "Slytherin")
characters = [s, de, p]
for character in characters:
    print(character.show_character())

# Изменение количества очков факультета
h = House("Griffindor")
h.show_house()
h.change_points()
h.show_house()
