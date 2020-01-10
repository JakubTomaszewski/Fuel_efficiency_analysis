import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()


c.execute('''
        CREATE TABLE cars(
        mark_model text PRIMARY KEY,
        id serial
        );
        ''')
conn.commit()


c.execute('''
        CREATE TABLE spec(
        car_name text PRIMARY KEY,
        hp integer,
        displ numeric(4,2),
        mpg numeric(3,2),
        weight numeric(4,2)
        );
        ''')
conn.commit()

#'hp', 'accel', 'displ', 'mpg', 'weight'