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
# # Getting the average mileage per year
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get('https://www.google.com/search?q=average+mileage+per+year&oq=average+mile&aqs=chrome.1.69i57j69i59.3633j0j7&sourceid=chrome&ie=UTF-8')
# avg_mileage = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div[1]/div/div[1]').text
# print(avg_mileage)
#
# driver.close()

import pandas as pd
import matplotlib.pyplot
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
db.execute("SELECT * FROM Cars WHERE origin = 'US';")

res = db.c.fetchall()

[print(line) for line in res]





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
