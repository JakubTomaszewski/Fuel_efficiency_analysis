#importing and preparing data to be inserted
import pandas as pd
import numpy as np

url_cars = 'https://assets.datacamp.com/production/repositories/516/datasets/2f3d8b2156d5669fb7e12137f1c2e979c3c9ce0b/automobiles.csv'
url_fuel_price = 'https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23e1e9f0&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=1168&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=GASREGCOVW&scale=left&cosd=1990-08-20&coed=2020-03-02&line_color=%234572a7&link_values=false&line_style=solid&mark_type=none&mw=3&lw=2&ost=-99999&oet=99999&mma=0&fml=a&fq=Weekly&fam=avg&fgst=lin&fgsnd=2009-06-01&line_index=1&transformation=lin&vintage_date=2020-03-06&revision_date=2020-03-06&nd=1990-08-20'

# Fuel prices table
prices = pd.read_csv(url_fuel_price, index_col=0, parse_dates=True)
prices = prices.rename(columns={'GASREGCOVW':'price_gallon'}, errors='raise')
# cleaning missing values
prices['price_gallon'] = pd.to_numeric(prices['price_gallon'], errors='coerce')
prices.replace('.', np.NaN, inplace=True)
prices = prices.fillna(method='ffill')

# Cars and Spec table
car_info = pd.read_csv(url_cars, index_col='yr', parse_dates=True)
car_info = car_info.drop_duplicates(subset=['name'])



spec = car_info.loc[:,['hp', 'weight' ,'accel', 'displ', 'mpg']].reset_index(drop=True)
spec['hp'] = spec['hp'].astype('float')
spec['weight'] = spec['weight'].astype('float')

cars = car_info.loc[:,['name', 'origin']]
cars = cars.set_index('name')
cars['horse_power'] = spec['hp'].values

#resampling data monthly
prices = prices.resample('M').mean()

#adding a new category col with region
prices['region'] = 'US'
prices['region'] = prices['region'].astype('category')



#creating db and a connection
import sqlite3

class Server():
    def __init__(self, path): #connecting to a db and creating a cursor
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()

    def execute(self, command):
        self.c.execute(command)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()



db = Server('database.db')


#creating tables Cars, Spec
db.execute('''CREATE TABLE Cars(
            id INTEGER PRIMARY KEY,
            mark_model text,
            origin char(2)
            );''')



db.execute('''CREATE TABLE Spec(
            car_id INTEGER PRIMARY KEY,
            hp numeric,
            weight numeric,
            acc_time numeric,
            range_miles numeric,
            mpg numeric,
            FOREIGN KEY (car_id) REFERENCES Cars (id)
            );''')

db.commit()


#inserting data into db
# That's a huge mess however, sqlite does not support add constraint syntax to i have to do it like this
[(db.conn.execute('INSERT INTO Cars VALUES (?, ?, ?);', (i, cars.index[i], cars.iloc[i, 0]))) for i in range(len(cars))]
for i in range(len(spec)):
    db.conn.execute('INSERT INTO Spec VALUES (?, ?, ?, ?, ?, ?);', (i, spec.iloc[i, 0], spec.iloc[i, 1], spec.iloc[i, 2], spec.iloc[i, 3], spec.iloc[i, 4]))

db.commit()

# spec.to_sql(name='Spec', con=db.conn, index=False)
prices.to_sql(name='Prices', con=db.conn)

db.close()


'''Testing'''

# db.execute("SELECT name from sqlite_master WHERE type='table';")
# print(db.c.fetchall())

# car = pd.read_sql_query('SELECT * FROM Cars LIMIT 5;', db.conn)
# prc = pd.read_sql_query('SELECT * FROM Prices LIMIT 5;', db.conn)
# spec = pd.read_sql_query('SELECT * FROM Spec LIMIT 5;', db.conn)

# db.execute("SELECT sql FROM sqlite_master WHERE type = 'table' AND name = 'Spec';")
# print(db.c.fetchall())