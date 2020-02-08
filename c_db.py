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

#adding a new category col with region
prices['region'] = 'US'
prices['region'] = prices['region'].astype('category')


#creating db and a connection
import sqlite3

class Server():
    def __init__(self, path): #connecting to a db and creating a cursor
        self.conn = sqlite3.connect(path)
        self.c = self.conn.cursor()

    def execute(self, command, values=None):
        self.c.execute(command, values)

    def commit(self):
        self.conn.commit()


db = Server('database.db')

# tables
#             Cars(
#             mark_model text PRIMARY KEY,
#             origin char(2)
#             )

#             Spec(
#             hp integer,
#             accel_time numeric,
#             range numeric,
#             mpg numeric,
#             weight integer
#             )

#             Prices(
#             date date,
#             price_gallon float,
#             region char(2)
#             )


#inserting data into db
[(db.execute('INSERT INTO Cars VALUES (?, ?)', (cars.index[i], cars.iloc[i, 0]))) for i in range(len(cars))]
prices.to_sql(name='Prices', con=db.conn)
spec.to_sql(name='Spec', con=db.conn)
db.commit()
