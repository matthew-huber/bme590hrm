
import pytest

from analyze_data import find_beat_times
from  fileReader import load_csv

times, voltages = load_csv('./test_data/test_data1.csv')


@pytest.mark.parametrize("time, voltage, expected", [
    (times, voltages, [0.214, 1.028, 1.842, 2.631, 3.419, 4.208, 5.025,
                       5.681, 6.675, 7.517, 8.328, 9.119, 9.889, 10.73,
                       11.59, 12.41, 13.24, 14.06, 14.85, 15.65, 16.44,
                       17.26, 18.13, 18.96, 19.74, 20.54, 21.31, 22.09,
                       22.91, 23.72, 24.55, 25.39, 26.20, 26.97, 27.77])
])
def test_find_beat_times(time, voltage, expected):
    beat_times = find_beat_times(times, voltages)
    assert beat_times == pytest.approx(expected)
