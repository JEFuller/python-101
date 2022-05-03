from csv import DictReader
file = open('data.csv')
readings = DictReader(file)

x = []
y = []

from parser import convertToHoursAgo

lastHour = 0

for reading in readings:
    if reading['station'] == '53310' and reading['sensor'] == 'precip' :
        tips = float(reading['value'])

        inches = tips * 0.0393701
        age = convertToHoursAgo(reading['time'])
        print(age, inches)

        x.append(age)
        y.append(inches)

        if age < 24:
            lastHour += inches

from matplotlib import pyplot

chart = pyplot.plot(x, y)

pyplot.savefig('chart.png')

# now send an email
# ... but set up to not really

from mail import send

subject = "it's raining"
message = f"last hour rainfall is {lastHour} inches"  
send("conf@alert.org", "dave@test.com", subject, message)


# attach an image
# no need to write to a file
import io
image = io.BytesIO()
pyplot.savefig(image, format='png')
send("conf@alert.org", "dave@test.com", "here's a chart", message, image)

