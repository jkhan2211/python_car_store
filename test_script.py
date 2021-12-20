import psycopg2

conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS carInventory(
    id SERIAL PRIMARY KEY NOT NULL,
    car_make text,
    car_model text,
    year varchar(17),
    first_owner varchar(17),
    vinnumber varchar(17)
)
""")

with open('MOCK_DATA.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f) # Skip the header row.
    next(f)
    next(f)
    cur.copy_from(f, 'carinventory', sep=',')

conn.commit()

    
    