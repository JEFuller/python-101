# DRAW A CHART

# 1. filter single sensor

# 2. data for axis


from csv import DictReader

file = open('data.csv')

readings = DictReader(file)

x = [] # from tips to inches
y = [] # from from a timestamp to an age

from parser import convertToHoursAgo

for reading in readings:
    if reading['station'] == '53310' and reading['sensor'] == 'precip':

        tips = float(reading['value'])
        inches = tips * 0.0393701
        age = convertToHoursAgo(reading['time'])
        print(age, inches)

        x.append(age)
        y.append(inches)


from matplotlib import pyplot

chart = pyplot.plot(x, y)

pyplot.savefig('chart.png')
