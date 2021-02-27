import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
place_name = ''
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        # Grab the station name, if it's not already set.
        if not place_name:
            place_name = row[name_index]
            print(place_name)
            
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high and low temperatures.

fig, a = plt.subplots(2,1)


a[0].plot(dates, highs, c = 'red')
a[0].plot(dates, lows, c= 'blue')
a[0].fill_between(dates,highs, lows, facecolor='blue', alpha = .1) 
a[0].set_title(f"Daily high and low temperatures - 2018\n{place_name} ", fontsize = 16)
a[0].set_xlabel("",fontsize = 12)
a[0].set_ylabel("Temperature (F)",fontsize = 10)
a[0].tick_params(axis="both", labelsize = 10)

filename = 'death_valley_2018_simple.csv'
place_name = ''
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')

    # Get dates, and high and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        # Grab the station name, if it's not already set.
        if not place_name:
            place_name = row[name_index]
            print(place_name)
            
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


a[1].plot(dates, highs, c = 'red')
a[1].plot(dates, lows, c= 'blue')
a[1].fill_between(dates,highs, lows, facecolor='blue', alpha = .1) 
a[1].set_title(f"{place_name} ", fontsize = 16)
a[1].set_xlabel("",fontsize = 12)
a[1].set_ylabel("Temperature (F)",fontsize = 10)
a[1].tick_params(axis="both", labelsize = 10)

fig.autofmt_xdate()


plt.show()