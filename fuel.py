'''
create tables in a db
CARS with car models and their origin
SPEC with the cars specification data (foreign key the 'name' with the cars table)
FUEL with fuel cost data for each year/6months (resampled)



-compute the average cost of 100 miles for each car - need to calculate first it from gallons

-get the average mileage from the web and compute which car is the most economic(which yearly cost is the smallest)

-show on a plot how the fuel price changed within time
'''





# import requests
# from bs4 import BeautifulSoup
#
# #pulling the mileage data
# # r = requests.get('https://www.google.com/search?q=average+mileage+per+year&oq=average+&aqs=chrome.1.69i57j69i59l3j35i39j0l3.3156j0j7&sourceid=chrome&ie=UTF-8').text
# # soup = BeautifulSoup(r, 'html.parser')
# # soup = soup.find('div', class_="BNeawe s3v9rd AP7Wnd")
# # print(soup)

import matplotlib.pyplot as plt
import pandas as pd



fuel = pd.read_csv('https://assets.datacamp.com/production/repositories/516/datasets/2f3d8b2156d5669fb7e12137f1c2e979c3c9ce0b/automobiles.csv', index_col='yr', parse_dates=True)
prices = pd.read_csv('GASREGCOVW.csv', index_col=0, parse_dates=True)
cars = fuel.loc[:,['name', 'origin']].set_index('name')
spec = fuel.loc[:,['name', 'hp', 'accel', 'displ', 'mpg', 'weight']].set_index('name')
prices = prices.rename(columns={'GASREGCOVW':'price_gallon'}, errors='raise')


#resampling data by 6 months
prices = prices.resample('6M').mean()
prices['region'] = 'US'

print(prices.head())
print(prices.columns)

# #how the fuel price changed
# prices['price_gallon'].plot()
# #cust
# plt.title('Fuel price change')
# plt.xlabel('Date')
# plt.ylabel('Price for gallon')
# #displ
# plt.show()


