class Rectangle(object):

    # initialize width and height
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # change output
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    # change width
    def set_width(self, width):
        self.width = width

    # change height
    def set_height(self, height):
        self.height = height

    # calculate area
    def get_area(self):
        return self.width * self.height

    # calculate perimeter
    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    # calculate diagonal
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if (self.width >= 50) or (self.height >= 50):
            return "Too big for picture."
        else:
            width_line = "".join(["*" for i in range(0, self.width)])
            shape = ""
            for height_level in range(0, self.height):
                shape += width_line + "\n"
        return shape

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(width=side, height=side)

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        super().set_width(side)
        super().set_height(side)
