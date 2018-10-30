# bme590hrm 
[![Build Status](https://travis-ci.org/matthew-huber/bme590hrm.svg?branch=master)](https://travis-ci.org/matthew-huber/bme590hrm)

This program reads in ECG data in the form of a CSV file, and exports a JSON file that contains the ECG metrics.
The metrics included in the JSON file are the ECG duration, voltage extremes, number of beats, times where beats were 
detected, and the beats per minute over a user specified interval.

To run the program, use the command `python main.py` when in this directory. You will be prompted for a filename, and if
 the file loads the duration of the ECG trace will be displayed, and the user will be asked to input times for detecting
 the beats per minute over. If all the information is entered correctly, a JSON file with the same name as the CSV file
 will be created hold all of the metrics.

