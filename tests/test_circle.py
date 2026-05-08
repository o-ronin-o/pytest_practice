import pytest
import src.shape as shape 
import math 


class TestCircle:

    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = shape.Circle(10)


    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle


    

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
