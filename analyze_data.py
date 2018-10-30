import logging


def create_and_fill_dict(times, voltage):
    """
    calls analyze functions to fill metrics dictionary

    :param times: (list) time array taken from csv file
    :param voltage: (list) voltage array taken from csv file
    :return: dictionary metrics with the heart rate analytics
    """
    metrics = {}

    metrics["duration"] = find_duration(times)
    logging.info('duration added to metrics dictionary')
    metrics["voltage_extremes"] = min_max_voltage(voltage)
    logging.info('voltage_extremes added to metrics dictionary')
    metrics["beats"] = find_beat_times(times, voltage)
    logging.info('beats added to metrics dictionary')
    metrics["num_beats"] = total_beats(metrics["beats"])
    logging.info('num_beats added to metrics dictionary')

    print("The ECG duration is {} seconds".format(metrics["duration"]))
    bpm_start = input("Enter the start time over the interval to analyze: ")
    bpm_stop = input("Enter the stop time over the interval to analyze: ")

    try:
        if float(bpm_start) < 0:
            bpm_start = 0
            logging.warning('bpm_start changed to 0')
        if float(bpm_stop) > metrics["duration"]:
            bpm_stop = metrics["duration"]
            logging.warning('bpm_stop changed to maximum time')
        if float(bpm_stop) < float(bpm_stop):
            metrics["mean_hr_bpm"] = find_bpm(metrics["beats"])
            logging.warning('bpm_start>bpm_start. Running over default time')
        else:
            metrics["mean_hr_bpm"] = find_bpm(metrics["beats"],
                                              (bpm_start, bpm_stop))
    except:
        metrics["mean_hr_bpm"] = find_bpm(metrics["beats"])
        logging.warning('incorrect datatype in range. Running default time')

    logging.info('mean_hr_bpm added to metrics dictionary')

    if 50 < metrics["mean_hr_bpm"] < 200:
        metrics["mean_hr_bpm"] = "Error calculating BPM: does not fall " \
                                 "in expected values"
    logging.warning('heart rate not in realistic range')

    return metrics


def find_bpm(beat_times, bpm_range=(0, 10)):
    """
    calculates bpm over user specified (or default 0 to 10 second) range

    :param beat_times: (array) times that heart beats are recorded
    :param bpm_range: (tuple) start and stop second to calculate bpm over
    :return: heart rate in bpm over range
    """
    start = float(bpm_range[0])
    stop = float(bpm_range[1])

    beats_in_interval = 0
    for time in beat_times:
        if start <= float(time) <= stop:
            beats_in_interval = beats_in_interval + 1

    interval_minutes = (float(stop) - float(start))/60
    bpm = beats_in_interval/interval_minutes
    return bpm


def total_beats(beat_times):
    """
    Finds the total number of beats in the ECG trace

    :param beat_times: (list) array of beat times
    :return: integer number of beats in beat_times
    """
    num_beats = len(beat_times)
    return num_beats


def find_duration(times):
    """
    find the duration of the ECG trace

    :param times: (list) array of times
    :return: the maximum time in the time array
    """
    max_time = max(times)
    return max_time


def min_max_voltage(voltage):
    """
    outputs the minimum and maximum voltage recorded

    :param voltage: (list) array of voltages
    :return: tuple of the minimum and maximum voltages
    """
    min_voltage = min(voltage)
    max_voltage = max(voltage)
    min_max_voltages = (min_voltage, max_voltage)
    return min_max_voltages


def find_beat_times(times, voltage):
    """
    list of times in the ECG where a heartbeat is detected

    :param times: (list) array of all ECG times
    :param voltage: (list) array of all ECG voltages
    :return: list of times where a beat is observed
    """
    interval = 0.3

    beat_times = []
    time = interval
    while time < max(times):
        beat_result = beat_in_interval(times, voltage, time, interval)
        if beat_result is not False:
            beat_times.append(beat_result)
        time = time + interval/2
    beat_result = beat_in_interval(times, voltage, max(times), interval)
    if beat_result is not False:
        beat_times.append(beat_result)
    beat_times = combine_double_beats(times, voltage, beat_times)
    return beat_times


def combine_double_beats(times, voltage, beat_times):
    """
    Combines beats that are close in time to the higher voltage of those beats

    :param times: (list) array of all ECG times
    :param voltage: (list) array of all ECG voltages
    :param beat_times: (list) array of times where a beat is observed
    :return: array of times beat occurs, without doubly detected beats
    """
    condensed_beats = []
    skip = 0
    for i in range(0, len(beat_times)):
        if skip == 1:
            skip = 0
        elif i == len(beat_times)-1:
            condensed_beats.append(beat_times[i])
        else:
            if abs((beat_times[i] - beat_times[i+1])) < 0.3:
                v1 = voltage[times.index(beat_times[i])]
                v2 = voltage[times.index(beat_times[i+1])]
                true_beat = max(v1, v2)
                if true_beat == v1:
                    condensed_beats.append(beat_times[i])
                    skip = 1
                    logging.warning('Second beat of double beat removed')
            else:
                condensed_beats.append(beat_times[i])

    return condensed_beats


def extract_voltage_time_arrays(times, voltage, end_interval, interval):
    """
    extracts smaller voltage and time arrays from entire data for analysis

    :param times: (list) array of all ECG times
    :param voltage: (list) array of all ECG voltages
    :param end_interval: (float) end time of interval to extract
    :param interval: (float) length of interval to extract
    :return:
        times_subarray: array of times in interval
        voltage_subarray: array of voltages in interval
        start_index: index in times array that is start of the subarrays
    """
    start_interval = end_interval - interval

    end_index = len(times)

    x = 1
    start_index = 0
    for i in times:
        if i < start_interval:
            start_index = x
        if i > end_interval and x < end_index:
            end_index = x - 1
        x = x + 1

    voltage_subarray = voltage[start_index:end_index]
    times_subarray = times[start_index:end_index]
    return times_subarray, voltage_subarray, start_index


def process_voltage(voltage):
    """
    process voltage array by subtracting average and dividing by maximum

    :param voltage: (list) array of voltages to process
    :return: processed voltage list
    """
    array_average = sum(voltage) / len(voltage)

    avg_subtracted_voltage = []
    for i in voltage:
        avg_subtracted_voltage.append(i - array_average)

    max_voltage = max(avg_subtracted_voltage)

    normalized_voltage = []
    for i in avg_subtracted_voltage:
        normalized_voltage.append(i / max_voltage)

    return normalized_voltage


def is_beat_valid(voltages, times, QRS_threshold):
    """
    Determines whether a heartbeat is valid by seeing if it is above the noise

    :param voltages: (list) voltage interval over which to analyze
    :param times: (list) time interval over which to analyze
    :param QRS_threshold: length to QRS region to exclude from cutoff
    :return: boolean indicating whether there is a valid heartbeat
    """
    cutoff = 0.4
    index_max_val = voltages.index(1)

    x = 0
    end_front = 0
    for i in times:
        if i <= times[index_max_val]-QRS_threshold/2:
            end_front = x
        x = x + 1

    x = 0
    start_back = 0
    for i in times:
        if i < times[index_max_val]+QRS_threshold/2:
            start_back = x
        x = x + 1

    front_voltages = voltages[0:end_front]
    if (front_voltages == []):
        front_voltages = [0]
    back_voltages = voltages[start_back:len(voltages)]
    if (back_voltages == []):
        back_voltages = [0]
    max_front = max(front_voltages)
    max_back = max(back_voltages)
    if max_front > cutoff or max_back > cutoff:
        return False
    else:
        logging.info('valid beat detected')
        return True


def beat_in_interval(times, voltage, end_interval, interval):
    """
    returns time of heart beat in interval, or false if there is none

    :param times: (list) time interval over which to analyze
    :param voltage: (list) voltage interval over which to analyze
    :param end_interval: (float) end time of interval to extract
    :param interval: (float) length of interval to extract
    :return: time of heartbeat in interval, or false if no heartbeat
    """

    times_subarray, voltage_subarray, start_index = \
        extract_voltage_time_arrays(times, voltage, end_interval, interval)

    norm_voltage = process_voltage(voltage_subarray)

    index_max_val = norm_voltage.index(1)

    QRS_time_region = 0.1
    beat_valid = is_beat_valid(norm_voltage, times_subarray, QRS_time_region)

    beat_time = times[index_max_val+start_index]
    if beat_valid is False:
        return False
    else:
        return beat_time
