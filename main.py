from fileReader import load_csv
from analyze_data import create_and_fill_dict
from json_conversion import convert_to_json


def main():
    file_to_read = input("Input a filename to read: ")
    times, voltages = load_csv(file_to_read)
    if times == 1 and voltages == 1:
        print("Error: File not found")
        return 1
    else:
        metrics = create_and_fill_dict(times, voltages)

        convert_to_json(metrics, file_to_read)


if __name__ == "__main__":
    main()
