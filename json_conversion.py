import json
import logging


def convert_to_json(dict_to_convert, csv_file):
    """
    converts dictionary with metrics to json, saving with same name as csv

    :param dict_to_convert: (dictionary) values to be held in json file
    :param csv_file: (string) name of future json file as a csv file
    :return: 0, indicating successful termination
    """
    json_file = csv_to_json(csv_file)

    with open(json_file, 'w') as file:
        json.dump(dict_to_convert, file)

    logging.info('JSON file written with heart rate metrics')
    return 0


def csv_to_json(csv_filename):
    """
    converts string referencing csv file to a json file

    :param csv_filename: (string) name of data, as a csv file
    :return: string of json filename matching csv file
    """
    csv_trimmed = csv_filename[:-3]
    json_added = csv_trimmed + 'json'
    return json_added
