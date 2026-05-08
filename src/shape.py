
import math
class shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    

class Rectangle(shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    

class Square(Rectangle):
    def __init__(self, side_len):
        super().__init__(side_len,side_len) 

