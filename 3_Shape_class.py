
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.height * self.width
        return area


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)


class Square(Shape):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


while True:

    choice = input(
        "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀" +
        "\n≀   Press 1 for Rectangle area calculation            ≀" +
        "\n≀   Press 2 for Square area calculation               ≀" +
        "\n≀   Press 3 to exit                                   ≀" +
        "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀\n")

    if choice == "1":
        try:
            width = int(input("Please enter the width of the rectangle: "))
            height = int(input("Please enter the height of the rectangle: "))
            rectangle = Rectangle(width, height)
            print("Rectangle Area:", rectangle.calculate_area())
        except ValueError:
            print("Please enter a number.")

    elif choice == "2":
        try:
            side_length = int(input("Please enter the side length of the square: "))
            square = Square(side_length)
            print("Square Area:", square.calculate_area())
        except ValueError:
            print("Please enter a number.")

    elif choice == "3":
        break

    elif choice not in ["1", "2", "3"]:
        print("Please enter a valid choice.")