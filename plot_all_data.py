# Plot statistics of all commute data
#
# David Liu, Nov 12, 2017

import os
import subprocess

# Get all files
files = os.listdir('.')

# Process all csv files
for file in files:
    if file.endswith('.csv'):
        subprocess.run('python plot_data.py %s' % file, shell=True)
