
from analyze_data import is_beat_valid
import pytest

from fileReader import load_csv
from analyze_data import process_voltage

times, voltages = load_csv('./test_data/test_data1.csv')
voltage_thru_beat = process_voltage(voltages[600:750])
time_thru_beat = times[600:750]

voltage_no_beat = process_voltage(voltages[1025:1175])
time_no_beat = times[1025:1175]

@pytest.mark.parametrize("voltages, times, qrs_threshold, expected", [
    (voltage_thru_beat, time_thru_beat, 0.1, True),
    (voltage_no_beat, time_no_beat, 0.1, False),
])
def test_process_voltage(voltages, times, qrs_threshold, expected):
    validity = is_beat_valid(voltages, times, qrs_threshold)
    assert validity == expected
