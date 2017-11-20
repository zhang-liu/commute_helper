# Utility function: extract time, distance, and duration data from csv file.
# Default only extracts statistics using weekdays data.
#
# Syntax: data = extract_data(filename)
#
# David Liu, Nov 12, 2017

import csv
import numpy as np
from math import floor


def extract_data(filename):
    time = []
    distance = []
    duration = []

    # Process csv data file
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')

        # Skip first line
        next(csvreader)

        for row in csvreader:
            # print(row)
            # print(row[3],row[4],row[6],row[7],row[8],row[9])
            if row[9] == 'OK':
                if int(row[6]) >= 0 and int(row[6]) <= 4:  # Weekdays
                    time.append(int(row[3])+int(row[4])/60)
                    distance.append(float(row[7]))
                    duration.append(float(row[8]))
            else:
                print('** Found Status = %s **' % row[9])

    # Compute averages of distance and duration based on time in bins
    bin_size = 0.25
    time_bin = np.arange(0, 24, bin_size)
    num_bin = len(time_bin)

    count = np.zeros(num_bin)
    distance_total = np.zeros(num_bin)
    duration_total = np.zeros(num_bin)

    for i in range(len(time)):
        j = floor((time[i]+bin_size/2)/bin_size) % num_bin
        count[j] += 1
        distance_total[j] += distance[i]
        duration_total[j] += duration[i]

    distance_ave = np.divide(distance_total, count)
    duration_ave = np.divide(duration_total, count)

    # Return results
    return time, distance, duration, time_bin, distance_ave, duration_ave
