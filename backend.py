import psycopg2

def connect():
   conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
   cur=conn.cursor()
   cur.execute("""CREATE TABLE IF NOT EXISTS carInventory(
    id integer PRIMARY KEY,
    car_make text,
    car_model text,
    year integer,
    first_owner boolean,
    vinnumber varchar(17)
)
""")
   conn.commit()
   conn.close()

def insert(id,car_make,car_model,year,first_owner,vinnumber):
    conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO carInventory VALUES('%s','%s','%s','%s','%s','%s')" % (id,car_make,car_model,year,first_owner,vinnumber))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM carInventory")
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
insert("1002","Honda","Civic","2003",'true',"3sdfSKHAN")
print(view())