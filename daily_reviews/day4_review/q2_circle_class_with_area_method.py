import math as m


class Circle:  
    """
    A simple Circle class that stores the radius and calculates the area.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        area(): Calculates and returns the area of the circle.
        __str__(): Returns a simple string representation of the Circle object.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = m.pi * self.radius **2
        return f"The area of {self} is {circle_area:.2f}"
    
    def __str__(self):
        return "Circle"
    

my_circle = Circle(5)


print(my_circle.area())

