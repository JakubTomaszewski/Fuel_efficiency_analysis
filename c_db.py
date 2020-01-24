import sqlite3

#creating db and a connection
conn = sqlite3.connect('database.db')
c = conn.cursor()

#importing and preparing data to be inserted
import pandas as pd

fuel = pd.read_csv('https://assets.datacamp.com/production/repositories/516/datasets/2f3d8b2156d5669fb7e12137f1c2e979c3c9ce0b/automobiles.csv', index_col='yr', parse_dates=True)
prices = pd.read_csv('GASREGCOVW.csv', index_col=0, parse_dates=True)
cars = fuel.loc[:,['name', 'origin']].drop_duplicates() #dropping duplicate values
cars = cars.set_index('name')
spec = fuel.loc[:,['name', 'hp', 'accel', 'displ', 'mpg', 'weight']].set_index('name')
prices = prices.rename(columns={'GASREGCOVW':'price_gallon'}, errors='raise')



#resampling data by 6 months
prices = prices.resample('6M').mean()
prices['region'] = 'US'

print(cars.head())

