import pytest

from analyze_data import total_beats
@pytest.mark.parametrize("beat_times, expected", [
    ([0.214, 1.028, 1.842, 2.631, 3.419, 4.208, 5.025,
      5.681, 6.675, 7.517, 8.328, 9.119, 9.889, 10.731,
      11.586, 12.406, 13.236, 14.058, 14.853, 15.65, 16.439,
      17.264, 18.131, 18.956, 19.739, 20.536, 21.306, 22.092,
      22.906, 23.719, 24.547, 25.394, 26.2, 26.972, 27.77], 35)
])
def test_total_beats(beat_times, expected):
    num_beats = total_beats(beat_times)
    assert num_beats == pytest.approx(expected)
