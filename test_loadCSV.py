from fileReader import load_csv
import pytest


@pytest.mark.parametrize("candidate,index,expected", [
    ('./test_data/test_data1.csv', 0, 0),
    ('./test_data/test_data1.csv', 9999, 27.775),
    ('./test_data/test_data1.csv', 3726, 10.35),
    ('./test_data/test_data3.csv', 24, 0.067),
    ('./test_data/test_data31.csv', 28, 'NAN'),
    ('./test_data/test_data31.csv', 29, 0.04),
    ('./test_data/test_data30.csv', 965, 'NAN'),
    ('./test_data/test_data30.csv', 966, 3.864),
])
def test_load_csv_times(candidate, index, expected):
    times, voltage = load_csv(candidate)
    assert times[index] == expected


@pytest.mark.parametrize("candidate,index,expected", [
    ('./test_data/test_data1.csv', 0, -0.145),
    ('./test_data/test_data1.csv', 9999, 0.72),
    ('./test_data/test_data1.csv', 1883, -0.38),
    ('./test_data/test_data3.csv', 24, -0.26),
    ('./test_data/test_data31.csv', 28, 0.7),
    ('./test_data/test_data31.csv', 29, 0.73125),
    ('./test_data/test_data30.csv', 972, 'NAN'),
    ('./test_data/test_data30.csv', 973, 0),
])
def test_load_csv_voltage(candidate, index, expected):
    times, voltage = load_csv(candidate)
    assert voltage[index] == expected
