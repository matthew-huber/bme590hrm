from fileReader import interp_missing_data
import pytest


@pytest.mark.parametrize("array, expected, prob_index", [
    ([5, 6, 1, 'NAN', 5], [5, 6, 1, 3, 5], 3),
    ([5, 6, 'NAN', 'NAN', 5], [5, 6, 5.6666666, 5.33333333, 5], 2),
    ([1, 5, 4, -1, -4, 'NAN', 8], [1, 5, 4, -1, -4, 2, 8], 5),
])
def test_amend_missing_data(array, expected, prob_index):
    output_array = interp_missing_data(array, prob_index, 1)
    assert output_array == pytest.approx(expected)
