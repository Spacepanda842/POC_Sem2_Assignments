from math import hypot
class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
            return (1/2) * self.base * self.height
    def hypotnuse(self):
        return hypot(self.base, self.height)
    def perimeter(self):
        return self.base + self.height + self.hypotnuse()

triangle_1 = RightTriangle(3, 4)
print("The area of triange_1 is", triangle_1.area())
print("The hypotenuse of triangle_1 is", triangle_1.hypotnuse())
print("The perimeter of triangle_1 is", triangle_1.perimeter())
triangle_2 = RightTriangle(4,8)
print("The area of triange_2 is", triangle_1.area())
print("The hypotenuse of triangle_2 is", triangle_1.hypotnuse())
print("The perimeter of triangle_2 is", triangle_1.perimeter())
triangle_3 = RightTriangle(5, 6)
print("The area of triange_3 is", triangle_1.area())
print("The hypotenuse of triangle_3 is", triangle_1.hypotnuse())
print("The perimeter of triangle_3 is", triangle_1.perimeter())


