import pytest

import src.shape as shape


@pytest.mark.parametrize("side_len, expected_area", [(5,25),(4,16),(3,9),(0,0)])

def test_multiple_params(side_len, expected_area):
    assert shape.Square(side_len).area() == expected_area

    