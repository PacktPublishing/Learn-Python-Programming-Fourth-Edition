# duck.typing.py


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius**2)


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def print_shape_info(shape):
    print(f"{shape.__class__.__name__} area: {shape.area()}")


circle = Circle(5)
rectangle = Rectangle(4, 6)

print_shape_info(circle)  # Circle area: 78.53975
print_shape_info(rectangle)  # Rectangle area: 24
