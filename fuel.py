'''
-compute the average cost of 100 miles for each car - need to calculate first it from gallons

+get the average mileage from the web and compute which car is the most economic(which yearly cost is the smallest)

+show on a plot how the fuel price changed within time

-predict the future prices

-based on the cars spec features, predict its mpg
'''

# Getting the average mileage per year
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get('https://www.google.com/search?q=average+mileage+per+year&oq=average+mile&aqs=chrome.1.69i57j69i59.3633j0j7&sourceid=chrome&ie=UTF-8')
# avg_mileage = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[1]').text
#
# driver.close()

# print(avg_mileage.split()[0])

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

class Server():
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.c = self.conn.cursor()
        except sqlite3.Error:
            print('Error while connecting to database')

    def execute(self, command):
        self.c.execute(command)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

db = Server('database.db')


cars = pd.read_sql_query("SELECT mark_model, hp, weight, acc_time, range_miles, mpg FROM Cars JOIN Spec ON Cars.id = Spec.car_id WHERE origin='US'", db.conn)
fuel_prices = pd.read_sql_query("SELECT date, price_gallon FROM Prices WHERE region = 'US';", db.conn, index_col='DATE')
fuel_prices.index = pd.to_datetime(fuel_prices.index)

# print(fuel_prices.head())
# print(cars.head())



# print('Difference between the prices from 1991 and 2020')


# print(fuel_prices.loc['1991'].index.strftime('%d-%m'))

from datetime import datetime

yr_91 = fuel_prices.loc['1991', 'price_gallon'].values
yr_00 = fuel_prices.loc['2000', 'price_gallon'].values
yr_19 = fuel_prices.loc['2019', 'price_gallon'].values
chg_idx = fuel_prices.loc['1991', 'price_gallon'].index.strftime('%d-%m')

chg = pd.DataFrame({'1991': yr_91,'2000':yr_00 ,'2019':yr_19}, index=chg_idx)
print(chg)

chg.plot()
plt.xlabel('Date')
plt.ylabel('Gallon price [$]')
plt.legend
plt.show()

# Change in the fuel price
print(chg['2019'] - chg['1991'])


# # Calculating the yearly percentage change
# yearly_change = fuel_prices.resample('A').last().pct_change() * 100
# print(yearly_change)
#
# # plotting the yearly price fluctuations
# yearly_change.plot()
#
# plt.title('Percentage price fluctuations')
# plt.ylabel('Pct price change')
# plt.xlabel('Year')
# plt.show()
#
#
# # Plotting the fuel price change over the last 20 years
# fuel_prices.plot()
# plt.title('Fuel price change [$]')
# plt.xlabel('Date')
# plt.ylabel('Price per gallon')
# plt.xticks(rotation=0)
# plt.show()
