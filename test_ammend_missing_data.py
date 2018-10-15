from fileReader import amend_missing_data
import pytest


@pytest.mark.parametrize("array, expected", [
    ([5, 6, 1, 'NAN', 5], [5, 6, 1, 3, 5]),
    ([5, 6, 'NAN', 'NAN', 5], [5, 6, 6-1/3, 6-2/3, 5]),
    ([4, 3, 2, 6, 'NAN', 5, 'NAN', 9], [4, 3, 2, 6, 5.5, 5, 7, 9]),
    ([1, 5, 4, -1, -4, 'NAN', 8], [1, 5, 4, -1, -4, 2, 8]),
])
def test_amend_missing_data(array, expected):
    output_array = amend_missing_data(array)
    assert output_array == pytest.approx(expected)
