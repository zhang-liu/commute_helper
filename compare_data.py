# Compare commute duration and distance statistics between multiple csv files.
#
# Syntax: python compare_data <filename0> <filename1>
# Example: python compare_data data_0_123_456.csv data_1_123_789.csv
#
# David Liu, Nov 12, 2017

import sys
import matplotlib.pyplot as plt
import numpy as np
from extract_data import extract_data

# Initialize figure
plt.figure(1, figsize=(10, 4*2))

# Get data and plot
for i in range(1, len(sys.argv)):
    filename = sys.argv[i]
    time, distance, duration, time_bin, distance_ave, duration_ave = \
        extract_data(filename)

    # Plot duration and distance statistics
    plt.subplot(2, 1, 1)
    plt.plot(time_bin, duration_ave, '.-')
    plt.subplot(2, 1, 2)
    plt.plot(time_bin, distance_ave, '.-')

# Set title, x and y labels, grid on, xticks, xlim, and legend
plt.subplot(2, 1, 1)
plt.title('Compare Commute Statistics')
plt.ylabel('Average Duration (Min)')
plt.grid(True)
plt.xticks(np.arange(0, 25, 2))
plt.xlim((0, 24))
plt.legend(sys.argv[1:], loc=0)
plt.subplot(2, 1, 2)
plt.ylabel('Average Distance (Mile)')
plt.grid(True)
plt.xticks(np.arange(0, 25, 2))
plt.xlim((0, 24))
plt.xlabel('Time of Day (Hr)')
plt.legend(sys.argv[1:], loc=0)

# Save figure
plt.savefig('compare_data_fig.png')
