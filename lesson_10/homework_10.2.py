from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return math.pi * self.__radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.__radius



class Rectangle(Figure):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c

    def area(self):
        half_perimeter = (
            self.__side_a + self.__side_b + self.__side_c
        ) / 2

        return math.sqrt(
            half_perimeter *
            (half_perimeter - self.__side_a) *
            (half_perimeter - self.__side_b) *
            (half_perimeter - self.__side_c)
        )

    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c


figures = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4, 5)
]


for figure in figures:
    print("Площа:", round(figure.area(), 2))
    print("Периметр:", round(figure.perimeter(), 2))
    print("----------------------")