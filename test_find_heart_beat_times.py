
import pytest

from analyze_data import find_beat_times
from  fileReader import load_csv

times, voltages = load_csv('./test_data/test_data1.csv')


@pytest.mark.parametrize("time, voltage, expected", [
    (times, voltages, [0.214, 1.028, 1.842, 2.631, 3.419, 4.208, 5.025,
                       5.681, 6.067, 6.675, 7.517, 8.328, 9.119, 9.889, 10.731,
                       11.586, 12.406, 13.236, 14.058, 14.853, 15.65, 16.439,
                       17.264, 18.131, 18.956, 19.739, 20.536, 21.306, 22.092,
                       22.906, 23.719, 24.547, 25.394, 26.2, 26.972, 27.772])
])
def test_find_beat_times(time, voltage, expected):
    beat_times = find_beat_times(times, voltages)
    assert beat_times == pytest.approx(expected)
