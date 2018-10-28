

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
    data_dict["num beats"] = total_beats(data_dict["beat times"])

    print("The duration of the ECG data is {} seconds".format(data_dict["duration"]))
    bpm_range = input("Enter a tuple with the range over which you would like the bpm to be calculated: ")
    data_dict["bpm"] = find_bpm(data_dict["beat times"], bpm_range)
    return data_dict


def find_bpm(beat_times, bpm_range=(0, 10)):
    start = bpm_range[0]
    stop = bpm_range[1]

    beats_in_interval = 0
    for time in beat_times:
        if start <= time <= stop:
            beats_in_interval = beats_in_interval + 1

    interval_minutes = (float(stop) - float(start))/60
    bpm = beats_in_interval/interval_minutes
    return bpm


def total_beats(beat_times):
    num_beats = len(beat_times)
    return num_beats


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
    time = interval
    while time < max(times):
        beat_result = beat_in_interval(times, voltage, time, interval)
        if beat_result is not False:
            beat_times.append(beat_result)
        time = time + interval/2
    beat_times = combine_double_beats(times, voltage, beat_times)
    print(beat_times)
    return beat_times


def combine_double_beats(times, voltage, beat_times):
    condensed_beats = []
    skip = 0
    for i in range(0, len(beat_times)-1):
        if skip == 1:
            skip = 0
        else:
            if abs((beat_times[i] - beat_times[i+1])) < 0.5:
                v1 = voltage[times.index(beat_times[i])]
                v2 = voltage[times.index(beat_times[i+1])]
                true_beat = max(v1, v2)
                if true_beat == v1:
                    condensed_beats.append(beat_times[i])
                    skip = 1
                else:
                    condensed_beats.append(beat_times[i+1])
                    skip = 1
            else:
                condensed_beats.append(beat_times[i])

    return condensed_beats


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
    return times_subarray, voltage_subarray, start_index


def process_voltage(voltage):
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
        return True


def beat_in_interval(times, voltage, end_interval, interval):

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
