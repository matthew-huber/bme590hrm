

def create_and_fill_dict(times, voltage):

    data_dict = {"duration": '',
                 "bpm": -1,
                 "beat times": -1,
                 "min max": -1,
                 "num beats": -1
                 }

    data_dict["duration"] = find_duration(times)
    data_dict["min max"] = min_max_voltage(voltage)
    return data_dict


def find_duration(times):
    max_time = max(times)
    return max_time


def min_max_voltage(voltage):
    min_voltage = min(voltage)
    max_voltage = max(voltage)
    min_max_voltages = (min_voltage, max_voltage)
    return min_max_voltages
