'''
create tables in a db
CARS with car models and their origin
SPEC with the cars specification data (foreign key the 'name' with the cars table)
FUEL with fuel cost data for each year/6months (resampled)


-compute the average cost of 100 miles for each car - need to calculate first it from gallons

-get the average mileage from the web and compute which car is the most economic(which yearly cost is the smallest)

-show on a plot how the fuel price changed within time

-predict the future prices
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







# #how the fuel price changed
# prices['price_gallon'].plot()
# #cust
# plt.title('Fuel price change')
# plt.xlabel('Date')
# plt.ylabel('Price for gallon')
# #displ
# plt.show()

#transform it to a df using pd.read_sql_query()
#drop all values where origin is not US or select all values where the origin is equal to 'US'
