# Plot commute duration and distance statistics.
# Default only plots statistics using data from Monday through Friday.
#
# Syntax: python plot_data <filename>
# Example: python plot_data data_0_123_456.csv
#
# David Liu, Nov 12, 2017

import sys
import matplotlib.pyplot as plt
import numpy as np
from extract_data import extract_data

# Get time, distance, and duration data from csv data file
filename = sys.argv[1]
time, distance, duration, time_bin, distance_ave, duration_ave = \
    extract_data(filename)

# Plot duration and distance statistics
plt.figure(1, figsize=(10, 4))
plt.plot(time, duration, '.', markersize=3)
plt.plot(time_bin, duration_ave, '.-')
plt.plot(time, distance, '.', markersize=3)
plt.plot(time_bin, distance_ave, '.-')
plt.grid(True)
plt.xlabel('Time of Day (Hr)')
plt.ylabel('Duration (Min) and Distance (Mile)')
plt.legend(('Duration Samples', 'Average Duration',
            'Distance Samples', 'Average Distance'), loc=0)
plt.title('Commute Statistics from %s to %s' % (filename.split('_')[2],
                                                filename.split('_')[3]))
plt.xticks(np.arange(0, 25, 2))
plt.xlim((0, 24))
plt.savefig(filename[:-4]+'_fig.png')
