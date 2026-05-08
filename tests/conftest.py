import pytest

import src.shape as shape 

@pytest.fixture 

def my_rectangle():
    return shape.Rectangle(10,5)