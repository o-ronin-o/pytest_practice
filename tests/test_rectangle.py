import pytest 
import math 
import src.shape as shape



def test_area(my_rectangle):
    assert my_rectangle.area() == 50 

def test_perimeter(my_rectangle):
    with pytest.raises(AssertionError):
        print("Assertion error raised")
        assert my_rectangle.perimeter() == 15