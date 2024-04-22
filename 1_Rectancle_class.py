class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Create an instance of the Rectangle class
rectangle = Rectangle(5, 7)

# Print the area and perimeter
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())