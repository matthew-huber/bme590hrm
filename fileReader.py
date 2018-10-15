import csv
import numpy as np

def filenameToRead():
    """
    prompt user for filename

    :return: filename: user entered filename (string)
    """

    filename = input('Enter a filename to evaluate: ')
    return filename

def loadCSV(filename):
    """
    loads data from given filename

    :param filename: (string) csv file to load
    :return: two columns
    """

    with open(filename, 'r') as dest_f:
        data_iter = csv.reader(dest_f, delimiter = ',')
        data = [data for data in data_iter]

    times = []
    voltage = []
    for row in data:
        times.append(row[0])
        voltage.append(row[1])

    return times, voltage