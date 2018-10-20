

def create_and_fill_dict(times, voltage):

    data_dict = {"duration": '',
                 "bpm": -1,
                 "beat times": -1,
                 "min max": -1,
                 "num beats": -1
                 }

    data_dict["duration"] = find_duration(times)

    return data_dict

def find_duration(times):
    max_time = max(times)
    return max_time