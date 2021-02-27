


import csv
from datetime import datetime

open_file =open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)




for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []
lows = []
dates = []












'''

somedate = '2018-07-01'
converted_date = datetime.strptime(somedate,"%Y-%m-%d")

print(converted_date)
'''


for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")

    except ValueError:
        print(f"Missing data for {converted_date}")  #f can allow us to use variables without hassle

    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(converted_date)

    

#print(highs)


    

#print(dates)
#print(lows)


import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates,highs, lows, facecolor='blue', alpha = .1) # alpha is the transparency of blue i.e light blue
#fill_between fills the color in between, x-axis, y1 Axis, y2 axis, facecolor, alpha if required)

plt.title("Daily high and low temperature - 2018", fontsize = 16)
plt.xlabel("",fontsize = 12)
plt.ylabel("Temperature (F)",fontsize = 10)
plt.tick_params(axis="both", labelsize = 10)

fig.autofmt_xdate()

plt.show()




'''


fig2, a = plt.subplots(2)

a[0].plot(dates, highs, c = 'red')
a[1].plot(dates, lows, c= 'blue')

plt.show()
'''
