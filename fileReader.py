import csv


def filename_to_read():
    """
    prompt user for filename

    :return: filename: user entered filename (string)
    """

    filename = input('Enter a filename to evaluate: ')
    return filename


def load_csv(filename):
    """
    loads data from given filename

    :param filename: (string) csv file to load
    :return: two columns
    """

    with open(filename, 'r') as dest_f:
        data_iter = csv.reader(dest_f, delimiter=',')
        data = [data for data in data_iter]

    times = []
    voltage = []
    for row in data:
        try:
            times.append(float(row[0]))
        except ValueError:
            times.append('NAN')
        try:
            voltage.append(float(row[1]))
        except ValueError:
            voltage.append('NAN')

    return times, voltage

# def amend_missing_data(rawarray):
#    for value in rawarray:
#        if (value == -1)
