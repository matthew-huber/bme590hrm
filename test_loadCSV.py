from fileReader import loadCSV
import pytest


@pytest.mark.parametrize("candidate,index,expected", [
    ('./test_data/test_data1.csv', 0, 0),
    ('./test_data/test_data1.csv', 9999, 27.775),
    ('./test_data/test_data1.csv', 3726, 10.35),
    ('./test_data/test_data3.csv', 24, 0.067),
])
def test_loadcsv_times(candidate, index, expected):
    times, voltage = loadCSV(candidate)
    assert times[index] == expected


@pytest.mark.parametrize("candidate,index,expected", [
    ('./test_data/test_data1.csv', 0, -0.145),
    ('./test_data/test_data1.csv', 9999, 0.72),
    ('./test_data/test_data1.csv', 1883, -0.38),
    ('./test_data/test_data3.csv', 24, -0.26),
])
def test_loadcsv_times(candidate, index, expected):
    times, voltage = loadCSV(candidate)
    assert voltage[index] == expected
