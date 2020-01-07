'''
import 2 datasets from the web, later download them and store as a relational db
query the appropriate columns

try to get the average fuel costs after 1982 and concatenate them to the table axis=0
compute the average cost of 100 miles for each car
get the average mileage from the web and compute which car is the most economic
'''



import sqlite3
import pandas as pd

# fuel efficiency - 'https://assets.datacamp.com/production/repositories/516/datasets/2f3d8b2156d5669fb7e12137f1c2e979c3c9ce0b/automobiles.csv'

fuel = pd.read_csv('https://assets.datacamp.com/production/repositories/516/datasets/2f3d8b2156d5669fb7e12137f1c2e979c3c9ce0b/automobiles.csv', index_col='yr', parse_dates=True)
prices = pd.read_csv('https://assets.datacamp.com/production/repositories/516/datasets/707566cf46c4dd6290b9029f5e07a92baf3fe3f7/oil_price.csv', index_col='Date', parse_dates=True)
#print(fuel.head())
prices.resample('A').mean()
print(prices.head())


#Change the colnames: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rename.html


'''
get also the oil price csv and calculate, the average amount spent this year for every of this cars. Get the average yearly mileage (using requests mayme? http F12?)


       Date  Price
0 1970-01-01   3.35
1 1970-02-01   3.35
2 1970-03-01   3.35
3 1970-04-01   3.35
4 1970-05-01   3.35

auto
    mpg  cyl  displ   hp  weight  accel         yr origin                       name
0  18.0    8  307.0  130    3504   12.0 1970-01-01     US  chevrolet chevelle malibu
1  15.0    8  350.0  165    3693   11.5 1970-01-01     US          buick skylark 320
2  18.0    8  318.0  150    3436   11.0 1970-01-01     US         plymouth satellite
3  16.0    8  304.0  150    3433   12.0 1970-01-01     US              amc rebel sst
4  17.0    8  302.0  140    3449   10.5 1970-01-01     US                ford torino
'''


