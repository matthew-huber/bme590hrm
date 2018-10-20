from analyze_data import min_max_voltage
import pytest


@pytest.mark.parametrize("candidate,expected", [
    ([1, 0, 8, 3, 8], (0, 8)),
    ([6, 0, 8, -4, 9], (-4, 9)),
    ([0.0, 8.23, 1.423, -1.663, 6.90], (-1.663, 8.23)),
])
def test_find_duration(candidate, expected):
    min_max_vals = min_max_voltage(candidate)
    assert min_max_vals == expected
