# hello world
print('Hello World')

# reading a a file in
# what does it mean to read a file in?

# 1. Tell Python which file we want to read

# To access a file in Python we say 'open'
# gives us a reference to the file we can use in Python
file = open('data.csv')


# 2. Load the data in 

# need to load it in to a "data structure"
data = dict()
data['name'] = "JE Fuller"

print(data)

# a dictionary is a collection of key-value pairs
# useful for storing something which has multiple types of values

reading_1 = dict()

reading_1['time'] = "1pm"
reading_1['sensor'] = "one"
reading_1['value'] = 2.0

reading_2 = dict()
reading_2['time'] = "2pm"
reading_2['sensor'] = "one"
reading_2['value'] = 1.5

# we can group togther all the readings in a list
readings = [reading_1, reading_2]
for reading in readings:
    print(reading)

# so now lets read the file in instead of hard coding 

# can ask Python to load a CSV file in to a collection of dictionaries
# use our first import:
from csv import DictReader

readings = DictReader(file)

# draw a chart:

# 1. filter just precip
# 2. create two axis

x = [] # from tips to inches
y = [] # from from a timestamp to an age

from datetime import datetime
from dateutil import parser

now = datetime.now()

for reading in readings:
    if reading['sensor'] == 'precip':
        tips = float(reading['value'])
        inches = tips * 0.0393701
        print(inches)

        time = parser.parse(reading['time'])
        age = now - time
        print(age.days)
        print()

        x.append(age.days)
        y.append(reading['value'])

from matplotlib import pyplot

chart = pyplot.plot(x, y)

pyplot.savefig('chart.png')
