import pytest
import time 
import src.my_functions as my_functions



def test_add():
    result = my_functions.add(10, 5)
    assert result == 15


def test_divide():
    result = my_functions.divide(10,5)
    assert result == 2


def test_divide_zero():
    with pytest.raises(ValueError):
            my_functions.divide(10,0)


@pytest.mark.slow
def test_very_slow():
     time.sleep(5)
     result = my_functions.divide(10,5)
     assert result == 2