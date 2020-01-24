import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

#importing and preparing data to be inserted
import pandas as pd

fuel = pd.read_csv('https://assets.datacamp.com/production/repositories/516/datasets/2f3d8b2156d5669fb7e12137f1c2e979c3c9ce0b/automobiles.csv', index_col='yr', parse_dates=True)
prices = pd.read_csv('GASREGCOVW.csv', index_col=0, parse_dates=True)
cars = fuel.loc[:,['name', 'origin']] #.set_index('name')
spec = fuel.loc[:,['name', 'hp', 'accel', 'displ', 'mpg', 'weight']].set_index('name')
prices = prices.rename(columns={'GASREGCOVW':'price_gallon'}, errors='raise')

#resampling data by 6 months
prices = prices.resample('6M').mean()
prices['region'] = 'US'




# c.execute('''
#         CREATE TABLE cars(
#         mark_model text,
#         origin varchar(6)
#         );
#         ''')

# c.execute('''
#         CREATE TABLE spec(
#         car_name text PRIMARY KEY,
#         hp integer,
#         displ numeric(4,2),
#         mpg numeric(3,2),
#         weight numeric(4,2)
#         );
#         ''')

# c.execute('''CREATE TABLE fuel(
#         date DATE NOT NULL,
#         price numeric(2,4) NOT NULL,
#         region char(2)
#         );
#         ''')
#
# conn.commit()
#
# #insert car data from cars
# print(cars.head())

#def insert_to_db()
# for row in cars.values:
#     #c.execute('INSERT INTO cars VALUES(:mark_model, :origin)', {'mark_model':cars['name'][row], 'origin':cars['origin'][row]})
#     c.execute('INSERT INTO cars VALUES(?, ?)', (row[0], row[1]))
#
# for row in
#
# conn.commit()
#
# rs = c.execute('SELECT * FROM cars')
# conn.commit()

spec = spec.drop_duplicates()

# cars = pd.DataFrame(rs.fetchall())
for row in spec.values:
    c.execute('INSERT INTO spec VALUES(:hp, :accel, :displ, :mpg, :weight)', {'hp':row[0], 'accel':row[1], 'displ':row[2], 'mpg':row[3], 'weight':row[4]})

conn.commit()
rs = c.execute('SELECT * FROM spec')
specs = pd.DataFrame(rs.fetchall())
print(specs.head())

conn.close()

# spec(
#         car_name text PRIMARY KEY,
#         hp integer,
#         displ numeric(4,2),
#         mpg numeric(3,2),
#         weight numeric(4,2)


