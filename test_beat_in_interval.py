
from analyze_data import beat_in_interval
import pytest

from fileReader import load_csv
times, voltages = load_csv('./test_data/test_data1.csv')


@pytest.mark.parametrize("times, voltage, end_interval, interval, expected", [
    (times, voltages, 1.75, 0.5, False),
    (times, voltages, 1.25, 0.5, 1.028),
])
def test_beat_in_interval(times, voltage, end_interval, interval, expected):
    beat_result = beat_in_interval(times, voltage, end_interval, interval)
    assert beat_result == expected
