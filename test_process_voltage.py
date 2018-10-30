
from analyze_data import process_voltage
import pytest

from fileReader import load_csv
times, voltages = load_csv('./test_data/test_data3.csv')


@pytest.mark.parametrize("voltage_array,expected", [
    ([-0.19, -0.205, -0.21, -0.2, -0.195, -0.21, -0.23, -0.235, -0.245],
     [1, 0.357142857, 0.142857143, 0.571428571, 0.785714286, 0.142857143,
      -0.714285714, -0.928571429, -1.357142857]),
])
def test_process_voltage(voltage_array, expected):
    voltage = process_voltage(voltage_array)
    assert voltage == pytest.approx(expected)
