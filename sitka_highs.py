import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = './sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #shows indexes of column headers
    """ for index, coloumn_header in enumerate(header_row):
        print(index, coloumn_header) """
    
    #get high temps
    dates, highs, lows = [], [], []
    for row in reader:
        current_date =  datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#print(highs)

#plot high temps
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title('Sitka, AK daily high/low temperatures - 2018', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()