
from analyze_data import combine_double_beats
import pytest

from fileReader import load_csv
times, voltages = load_csv('./test_data/test_data1.csv')


@pytest.mark.parametrize("times, voltages, beat_times, expected", [
    (times, voltages, [0.217, 0.3, 0.9, 1.7, 1.719], [0.217, 0.9, 1.719]),
    (times, voltages, [0.214, 1.028, 1.842, 2.631, 3.419, 4.208, 5.025, 5.025,
                       5.681, 6.675, 7.517, 8.328, 9.119, 9.889, 10.731, 11.586,
                       12.406, 13.236, 14.058, 14.058, 14.853, 15.65, 16.439,
                       17.264, 18.131, 18.956, 19.739, 20.536, 21.306, 22.092,
                       22.906, 23.719, 24.547, 25.394, 26.2, 26.972, 27.77],
     [0.214, 1.028, 1.842, 2.631, 3.419, 4.208, 5.025, 5.681, 6.675, 7.517,
      8.328, 9.119, 9.889, 10.731, 11.586, 12.406, 13.236, 14.058, 14.853,
      15.65, 16.439, 17.264, 18.131, 18.956, 19.739, 20.536, 21.306, 22.092,
      22.906, 23.719, 24.547, 25.394, 26.2, 26.972, 27.77])

])
def test_combine_double_beats(times, voltages, beat_times, expected):
    final_beats = combine_double_beats(times, voltages, beat_times)
    print(final_beats)
    assert final_beats == expected

