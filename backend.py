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

def insert(car_make,car_model,year,first_owner,vinnumber):
    conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT into carInventory(car_make,car_model,year,first_owner,vinnumber) VALUES (%s, %s, %s, %s, %s)", (car_make,car_model,year,first_owner,vinnumber))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM carInventory")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(car_make="",car_model="",year="",first_owner="",vinnumber=""):
    conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    sql="SELECT * FROM carInventory WHERE car_make=%s OR car_model=%s OR year=%s OR first_owner=%s OR vinnumber=%s"
    addr= (car_make,car_model,year,first_owner,vinnumber)
    cur.execute(sql, addr)
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM carinventory WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    
    
def update(id,car_make,car_model,year,first_owner,vinnumber): 
    conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE carinventory SET car_make=%s,car_model=%s,year=%s,first_owner=%s,vinnumber=%s WHERE id=%s",(car_make,car_model,year,first_owner,vinnumber,id))
    conn.commit()
    conn.close()
    
    
connect()
insert("Honda","Civic","2003",'true',"3sdfSKHAN")
#delete(816)
#print(view())
#update(1002,"Honda","Civic","2004","true","3sdfSKHAM")
#print(search(car_model="Camry"))