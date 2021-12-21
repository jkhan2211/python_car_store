import psycopg2

class Database: 
    
    def __init__(self, db):
        conn=psycopg2.connect(db)
        cur=conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS carInventory(
            id SERIAL PRIMARY KEY NOT NULL,
            car_make text,
            car_model text,
            year varchar(17),
            first_owner varchar(17),
            vinnumber varchar(17)
        )
        """)
        conn.commit()
        conn.close()

    def insert(self,car_make,car_model,year,first_owner,vinnumber):
        conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("INSERT into carInventory(car_make,car_model,year,first_owner,vinnumber) VALUES (%s, %s, %s, %s, %s)", (car_make,car_model,year,first_owner,vinnumber))
        conn.commit()
        conn.close()

    def view(self):
        conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("SELECT * FROM carInventory")
        rows=cur.fetchall()
        conn.close()
        return rows

    def search(self,car_make="",car_model="",year="",first_owner="",vinnumber=""):
        conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
        cur=conn.cursor()
        sql="SELECT * FROM carInventory WHERE car_make=%s OR car_model=%s OR year=%s OR first_owner=%s OR vinnumber=%s"
        addr= (car_make,car_model,year,first_owner,vinnumber)
        cur.execute(sql,addr)
        rows=cur.fetchall()
        conn.close()
        return rows

    def delete(self,id):
        conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("DELETE FROM carinventory WHERE id=%s", (id,))
        conn.commit()
        conn.close()
        
        
    def update(self,id,car_make,car_model,year,first_owner,vinnumber): 
        conn=psycopg2.connect("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")
        cur=conn.cursor()
        cur.execute("UPDATE carinventory SET car_make=%s,car_model=%s,year=%s,first_owner=%s,vinnumber=%s WHERE id=%s",(car_make,car_model,year,first_owner,vinnumber,id))
        conn.commit()
        conn.close()
    
    


#TODO: create a funationality, that will sort the db