import csv
import logging


def load_csv(filename):
    """
    loads data from given filename

    :param filename: (string) csv file to load
    :return: two columns
    """

    try:
        with open(filename, 'r') as dest_f:
            data_iter = csv.reader(dest_f, delimiter=',')
            data = [data for data in data_iter]

        times = []
        voltage = []
        for row in data:
            try:
                times.append(float(row[0]))
            except ValueError:
                logging.warning('Non-numeric time in csv file. NAN written')
                times.append('NAN')
            try:
                voltage.append(float(row[1]))
            except ValueError:
                logging.warning('Non-numeric voltage in csv file. NAN written')
                voltage.append('NAN')

        return times, voltage

    except IOError:
        logging.error('invalid filename entered')
        return 1, 1


def amend_missing_data(raw_array):
    length_array = len(raw_array)
    for i in range(0, length_array):
        if raw_array[i] == 'NAN':
            raw_array = interp_missing_data(raw_array, i, 1)
            logging.info('NAN value in array replaced with interpolated value')
    return raw_array


def interp_missing_data(array, prob_index, dist_good_val):
    if array[prob_index + 1] == 'NAN':
        interp_missing_data(array, prob_index+1, dist_good_val+1)

    next_val = array[prob_index + 1]
    last_good_val = array[prob_index - dist_good_val]
    array[prob_index] = next_val - (next_val-last_good_val)/(dist_good_val + 1)
    return array
