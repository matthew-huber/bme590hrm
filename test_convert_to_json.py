from json_conversion import csv_to_json
from json_conversion import convert_to_json
import pytest
import os


@pytest.mark.parametrize("dict, csv_file", [
    ({"duration": 10, "voltage_extremes": (12, 20)}, './test_data/test_data1.csv'),
])
def test_convert_to_json(dict, csv_file):
    json_file = csv_to_json(csv_file)
    exists = os.path.isfile(json_file)
    if exists:
        os.remove(json_file)

    convert_to_json(dict, csv_file)

    exists = os.path.isfile(json_file)
    assert exists is True
