
from analyze_data import extract_voltage_time_arrays
import pytest

from fileReader import load_csv
times, voltages = load_csv('./test_data/test_data3.csv')


@pytest.mark.parametrize("end,interval,expected", [
    (0.025, 0.025,
     [-0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.2, -0.19, -0.175]),
    (1.001, 0.012, [-0.28, -0.29, -0.305, -0.3, -0.305]),
    (1.001, 0.013, [-0.28, -0.29, -0.305, -0.3, -0.305]),
    (1.001, 0.011, [-0.29, -0.305, -0.3, -0.305]),
])
def test_extract_voltage_time_arrays_voltage(end, interval, expected):
    t, v, i = extract_voltage_time_arrays(times, voltages, end, interval)
    assert v == expected


@pytest.mark.parametrize("end,interval,expected", [
    (0.025, 0.025,
     [0, 0.003, 0.006, 0.008, 0.011, 0.014, 0.017, 0.019, 0.022, 0.025]),
    (1.001, 0.012, [0.989, 0.992, 0.994, 0.997, 1]),
    (1.001, 0.013, [0.989, 0.992, 0.994, 0.997, 1]),
    (1.001, 0.011, [0.992, 0.994, 0.997, 1]),
])
def test_extract_voltage_time_arrays_time(end, interval, expected):
    t, v, i = extract_voltage_time_arrays(times, voltages, end, interval)
    assert t == expected


@pytest.mark.parametrize("end,interval,expected", [
    (0.025, 0.025, 0),
    (1.001, 0.012, 356),
    (1.001, 0.013, 356),
    (1.001, 0.011, 357),
])
def test_extract_voltage_time_arrays_time(end, interval, expected):
    t, v, i = extract_voltage_time_arrays(times, voltages, end, interval)
    assert i == expected
