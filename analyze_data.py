

def create_and_fill_dict(times, voltage):

    data_dict = {"duration": '',
                 "bpm": -1,
                 "beat times": -1,
                 "min max": -1,
                 "num beats": -1
                 }

    data_dict["duration"] = find_duration(times)
    data_dict["min max"] = min_max_voltage(voltage)
    data_dict["beat times"] = find_duration(times, voltage)
    return data_dict


def find_duration(times):
    max_time = max(times)
    return max_time


def min_max_voltage(voltage):
    min_voltage = min(voltage)
    max_voltage = max(voltage)
    min_max_voltages = (min_voltage, max_voltage)
    return min_max_voltages

def find_beat_times(times, voltage):
    interval = 0.5
    threshold = 0.75

    beat_times = []
    for time in range(interval, max(times), interval/2):
        beat_times.append(beat_in_interval(times, voltage, time, interval))

    beat_times = combine_double_beats(times, voltage, beat_times)
    return beat_times


def extract_voltage_time_arrays(times, voltage, end_interval, interval):
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
    return times_subarray, voltage_subarray

def beat_in_interval(times, voltage, end_interval, interval):

    times_subarray, voltage_subarray = extract_voltage_time_arrays(times, voltage, end_interval, interval)

    avg_subtracted_voltage = []
    subarray_average = sum(voltage_subarray)/len(voltage_subarray)
    for i in voltage_subarray:
        avg_subtracted_voltage.append(i - subarray_average)

    max_voltage = max(avg_subtracted_voltage)
    normalized_voltage = []
    for i in avg_subtracted_voltage:
        normalized_voltage.append(i/max_voltage)

    index_max_val = normalized_voltage.index(1)

    QRS_time_region = 0.1

    time_before_QRS = 0

    return 0

    #
    #for i in times_subarray:
    #    if i < times[]