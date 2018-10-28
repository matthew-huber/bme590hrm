from json_conversion import csv_to_json
import pytest


@pytest.mark.parametrize("csv_file, json_file", [
    ('./test_data/test_data1.csv', './test_data/test_data1.json'),
    ('./test_data/test_data31.csv', './test_data/test_data31.json'),
])
def test_csv_to_json(csv_file, json_file):
    file_result = csv_to_json(csv_file)
    assert file_result == json_file
