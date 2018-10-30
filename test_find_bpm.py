
import pytest

from analyze_data import find_bpm
from fileReader import load_csv

times, voltages = load_csv('./test_data/test_data1.csv')


@pytest.mark.parametrize("beat_times, range, expected", [
    ([0, 10, 20], (0, 20), 9)
])
def test_find_bpm(beat_times, range, expected):
    beat_times = find_bpm(beat_times, range)
    assert beat_times == pytest.approx(expected)


@pytest.mark.parametrize("beat_times, expected", [
    ([0, 10, 20], 12)
])
def test_find_bpm_default(beat_times, expected):
    beat_times = find_bpm(beat_times)
    assert beat_times == pytest.approx(expected)
