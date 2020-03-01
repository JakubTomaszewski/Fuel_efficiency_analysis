#importing and preparing data to be inserted
import pandas as pd

fuel = pd.read_csv('https://assets.datacamp.com/production/repositories/516/datasets/2f3d8b2156d5669fb7e12137f1c2e979c3c9ce0b/automobiles.csv', index_col='yr', parse_dates=True)
fuel = fuel.drop_duplicates(subset=['name']) #dropping duplicate cars
prices = pd.read_csv('GASREGCOVW.csv', index_col=0, parse_dates=True)
cars = fuel.loc[:,['name', 'origin']]
cars = cars.set_index('name')
spec = fuel.loc[:,['hp', 'accel', 'displ', 'mpg']].reset_index(drop=True)
spec['model'] = fuel['name'].values
# spec = spec.drop(['yr'], axis=1)
car_name = fuel.name.values
# spec = fuel.loc[:,['name', 'hp', 'accel', 'displ', 'mpg']].set_index('name')

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

    def execute(self, command):
        self.c.execute(command)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()



db = Server('database.db')


#creating tables Cars, Spec
db.execute('''CREATE TABLE Cars(
            mark_model text PRIMARY KEY,
            origin char(2)
            );''')

db.execute('''CREATE TABLE Spec(
            hp integer,
            acc_time numeric,
            range_miles numeric,
            mpg numeric,
            mark_model text REFERENCES Cars(mark_model)
            );''')

db.commit()
# print(spec.head())

# #inserting data into db
# # That's a huge mess however, sqlite does not support add constraint syntax to i have to do it like this
[(db.conn.execute('INSERT INTO Cars VALUES (?, ?)', (cars.index[i], cars.iloc[i, 0]))) for i in range(len(cars))]
[(db.conn.execute('INSERT INTO Spec VALUES (?, ?, ?, ?, ?)', (spec.iloc[i, 0], spec.iloc[i, 1], spec.iloc[i, 2], spec.iloc[i, 3], spec.iloc[i, 4]))) for i in range(len(spec))]


# spec.to_sql(name='Spec', con=db.conn, index=False)
prices.to_sql(name='Prices', con=db.conn)


'''db.execute('ALTER TABLE Spec ADD car_name text REFERENCES Cars (mark_model);')

for n in car_name:
    db.conn.execute('INSERT INTO Spec (car_name) VALUES (?);', (n,))'''

db.commit()


db.execute("SELECT name from sqlite_master WHERE type='table';")
print(db.c.fetchall())


car = pd.read_sql_query('SELECT * FROM Cars LIMIT 5', db.conn)
prc = pd.read_sql_query('SELECT * FROM Prices LIMIT 5', db.conn)
spec = pd.read_sql_query('SELECT hp, acc_time FROM Spec LIMIT 5', db.conn)

print('CARS\n',car)
print('PRICES\n',prc)
print('SPEC\n',spec)

# SQLite does not support the ALTER TABLE syntax so i cannot use the commands below
# db.execute('ALTER TABLE Spec ADD CONSTRAINT spec_primary PRIMARY KEY (name);')
# db.execute('ALTER TABLE Spec ADD CONSTRAINT car_spec_name FOREIGN KEY (name) REFERENCES Cars (mark_model) ;')

db.commit()

# print(spec.head())

#transform it to a df using pd.read_sql_query()
#drop all values where origin is not US

db.close()


# delete db file for testing
import os

os.system('del /f database.db')