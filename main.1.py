# ASSIGNMENT    PRINT

message = 'hello world'

print(message)

x = 10
y = 2

z = x + y

print(z)

# COLLECTIONS 

numbers = [x,y]

print(numbers[0])

for number in numbers:
    if number > 5:
        print(number)


# DICTIONARIES

station = dict()
station['id'] = "53310"
station['name'] = "Tabletop Wilderness"


print(station)

reading_1 = dict()
reading_1['time'] = "1pm"
reading_1['station'] = "53310"
reading_1['value'] = 2.0

reading_2 = {'time': '2pm', 'sensor': '53310', 'value': 1.5}

# LIST OF DICTIONARIES

readings = [reading_1, reading_2]
for reading in readings:
    print(reading)

# BUT NO ONE DOES THIS

# READ FROM FILE / PORT SERVER 

from csv import DictReader


# reading a a file in
# what does it mean to read a file in?

# 1. Tell Python which file we want to read

# To access a file in Python we say 'open'
# gives us a reference to the file we can use in Python
file = open('data.csv')

readings = DictReader(file)

for reading in readings:
    print(reading) # NOTE ALL VALUES ARE STRINGS
