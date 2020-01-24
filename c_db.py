#importing and preparing data to be inserted
import pandas as pd

fuel = pd.read_csv('https://assets.datacamp.com/production/repositories/516/datasets/2f3d8b2156d5669fb7e12137f1c2e979c3c9ce0b/automobiles.csv', index_col='yr', parse_dates=True)
fuel = fuel.drop_duplicates(subset=['name']) #dropping duplicate cars
prices = pd.read_csv('GASREGCOVW.csv', index_col=0, parse_dates=True)
cars = fuel.loc[:,['name', 'origin']]
cars = cars.set_index('name')
spec = fuel.loc[:,['name', 'hp', 'accel', 'displ', 'mpg', 'weight']].set_index('name')

prices = prices.rename(columns={'GASREGCOVW':'price_gallon'}, errors='raise')

#resampling data by 6 months
prices = prices.resample('6M').mean()
prices['region'] = 'US'


#creating db and a connection
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()
'''
create tables in a db
CARS with car models and their origin
SPEC with the cars specification data (foreign key the 'name' with the cars table)
FUEL with fuel cost data for each year/6months (resampled)
'''

c.execute('''CREATE TABLE Cars(
            mark_model text PRIMARY KEY,
            origin char(2)
            );''')


# conn.commit()
#create spec db
c.execute('''CREATE TABLE spec
            hp real
            accel real
            distance real


            ''')