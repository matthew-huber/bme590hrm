import json


def convert_to_json(dict_to_convert, csv_file):
    json_file = csv_to_json(csv_file)

    with open(json_file, 'w') as file:
        json.dump(dict_to_convert, file)


def csv_to_json(csv_filename):
    csv_trimmed = csv_filename[:-3]
    json_added = csv_trimmed + 'json'
    return json_added
