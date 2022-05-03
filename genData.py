import csv
from datetime import datetime, timedelta
from math import sin

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['time', 'station', 'sensor', 'value'])
    for i in range(0, 72*4):
        time = datetime.now() - timedelta(minutes=i*15) 
        if i in range(1*4, 8*4):
            ratio = (i-1*4) / (7*4)
            precip = round(sin(ratio * 3.14) * 3, 2)
        elif i in range(60*4, 70*4):
            ratio = (i-60*4) / (10*4)
            precip = round(sin(ratio * 3.14) * 4, 2)
        else:
            precip = 0
        writer.writerow([time, 53310, 'precip', precip])
        writer.writerow([time, 53310, 'stage', 2.0 + precip])

        writer.writerow([time, 53313, 'precip', 0.0])
        writer.writerow([time, 53313, 'stage', 3.0])