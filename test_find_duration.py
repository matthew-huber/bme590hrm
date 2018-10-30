from analyze_data import find_duration
import pytest


@pytest.mark.parametrize("candidate,expected", [
    ([1, 0, 8, 3, 8], 8),
    ([6, 0, 8, -4, 9], 9),
    ([-1.663, 0.0, 1.423, 6.90, 8.23], 8.23),
])
def test_find_duration(candidate, expected):
    duration = find_duration(candidate)
    assert duration == expected
