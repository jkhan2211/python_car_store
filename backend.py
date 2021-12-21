import psycopg2

class Database: 
    
    def __init__(self, db):
        self.conn=psycopg2.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS carInventory(
            id SERIAL PRIMARY KEY NOT NULL,
            car_make text,
            car_model text,
            year varchar(17),
            first_owner varchar(17),
            vinnumber varchar(17)
        )
        """)
        self.conn.commit()

    def insert(self,car_make,car_model,year,first_owner,vinnumber):
        self.cur.execute("INSERT into carInventory(car_make,car_model,year,first_owner,vinnumber) VALUES (%s, %s, %s, %s, %s)", (car_make,car_model,year,first_owner,vinnumber))
        self.conn.commit()
        
    def view(self):
        self.cur.execute("SELECT * FROM carInventory")
        rows=self.cur.fetchall()
        return rows

    def search(self,car_make="",car_model="",year="",first_owner="",vinnumber=""):
        sql="SELECT * FROM carInventory WHERE car_make=%s OR car_model=%s OR year=%s OR first_owner=%s OR vinnumber=%s"
        addr= (car_make,car_model,year,first_owner,vinnumber)
        self.cur.execute(sql,addr)
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM carinventory WHERE id=%s", (id,))
        self.conn.commit()        
        
    def update(self,id,car_make,car_model,year,first_owner,vinnumber): 
        self.cur.execute("UPDATE carinventory SET car_make=%s,car_model=%s,year=%s,first_owner=%s,vinnumber=%s WHERE id=%s",(car_make,car_model,year,first_owner,vinnumber,id))
        self.conn.commit()    
    
    def __del__(self):
        self.conn.close()

#TODO: create a funationality, that will sort the db