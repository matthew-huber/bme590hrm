
from analyze_data import combine_double_beats
import pytest

from fileReader import load_csv
times, voltages = load_csv('./test_data/test_data1.csv')


@pytest.mark.parametrize("times, voltages, beat_times, expected", [
    (times, voltages, [0.217, 0.3, 0.9, 1.7, 1.719], [0.217, 0.9, 1.719]),
])
def test_combine_double_beats(times, voltages, beat_times, expected):
    final_beats = combine_double_beats(times, voltages, beat_times)
    assert final_beats == expected
