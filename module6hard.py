import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self._sides = []
        self.__color = list(color)
        self.filled = False
        
        if len(sides) == self.sides_count:
            self.set_sides(*sides)
        else:
            self.set_sides(*[1] * self.sides_count)  

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)  

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self._sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, length):
        super().__init__(color, length)
        self.__radius = self._sides[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, length):
        super().set_sides(length)
        self.__radius = length / (2 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def get_square(self):
        s = sum(self._sides) / 2
        return (s * (s - self._sides[0]) * (s - self._sides[1]) * (s - self._sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, side)

    def set_sides(self, side):
        self._sides = [side] * self.sides_count

    def get_volume(self):
        return self._sides[0] ** 3  


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)  
print(circle1.get_color())
cube1.set_color(300, 70, 15)  
print(cube1.get_color())


cube1.set_sides(5, 3, 12, 4, 5)  
print(cube1.get_sides())
circle1.set_sides(15)  
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
