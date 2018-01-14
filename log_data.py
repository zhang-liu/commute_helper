# Using Python to periodically poll Google Maps for commute data in live
# traffic condition and log the data in a csv file.
#
# Google requires API key to access live traffic and the key can be obtained at
# https://developers.google.com/maps/documentation/directions/get-api-key
#
# David Liu, Nov 12, 2017

import requests
import datetime
import time
import os

# User inputs: addresses, api key, and sample time
from_address = ['1 Infinite Loop, Cupertino, California',
                '1 Hacker Way, Menlo Park, CA']

to_address = ['1 Hacker Way, Menlo Park, CA',
              '1 Infinite Loop, Cupertino, California']

api_key = 'AIzaSyBP0336TDvYULFtgALMLmd7AL0jCjpK4y4'  # Enter your own key here
sample_time = 15 * 60   # Sample time in seconds, 15 * 60 is 15 minutes

# Number of directions
num = len(from_address)

# Create csv data file and write header row
filename = []
for i in range(num):
    filename.append('data_%d_%s_%s.csv' % (i,
                    from_address[i].split(' ', 1)[0],
                    to_address[i].split(' ', 1)[0]))
    if not os.path.isfile(filename[i]):
        fh = open(filename[i], 'w')
        fh.write('Year,Month,Day,Hour,Min,Sec,Weekday,Miles,Minutes,Status\n')
        fh.close()

# URL and request parameters
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/directions/json'
params = []
for i in range(num):
    params.append({'origin': from_address[i],
                   'destination': to_address[i],
                   'departure_time': 'now',
                   'key': api_key})

# Periodically poll Google Maps for commute data
while True:
    for i in range(num):
        # Send request and get the response data
        req = requests.get(GOOGLE_MAPS_API_URL, params=params[i])
        res = req.json()

        # Extract commute data and write to csv file
        try:
            # Results
            status = str(res['status'])
            distance_m = res['routes'][0]['legs'][0]['distance']['value']
            duration_s = res['routes'][0]['legs'][0]['duration_in_traffic']['value']

            # Current time
            now = datetime.datetime.now()

            # Write to file
            fh = open(filename[i], 'a')
            line = now.strftime('%Y,%m,%d,%H,%M,%S') + ',%d,%.1f,%.1f,%s\n' \
                % (now.weekday(), distance_m/1609.34, duration_s/60, status)
            fh.write(line)
            fh.close()
        except Exception:
            print('*** Error ***')

        # Sleep 15 seconds
        time.sleep(15)

    # Sleep
    time.sleep(sample_time - 15*num)
