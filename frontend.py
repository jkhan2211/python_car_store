from tkinter import *
from backend import Database


database=Database("dbname='Car_Inventory_db' user='postgres' password='password' host='localhost' port='5432'")

def get_selected_row(event):
    
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
        e5.delete(0,END)
        e5.insert(END,selected_tuple[5])
    except IndexError:
        pass
        
   
    

# this will view all the items in currently in the database 
def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

# this command will search the items in currently in the database(backend)
def search_command():
    list1.delete(0,END)
    for row in database.search(make_text.get(),model_text.get(),year_text.get(),firstOwner_text.get(),vin_text.get()):
        list1.insert(END,row)

# this command add new items in the database(backend)
def add_command():
    database.insert(make_text.get(),model_text.get(),year_text.get(),firstOwner_text.get(),vin_text.get())
    list1.delete(0,END)
    list1.insert(END,(make_text.get(),model_text.get(),year_text.get(),firstOwner_text.get(),vin_text.get()))


def delete_command():
    database.delete(selected_tuple[0])


def update_command():
    database.update(selected_tuple[0],make_text.get(),model_text.get(),year_text.get(),firstOwner_text.get(),vin_text.get())

window = Tk()

window.wm_title("Car Store Inventory")

l1=Label(window, text="Make")
l1.grid(row=0,column=0)

l2=Label(window, text="Model")
l2.grid(row=0,column=2)

l3=Label(window, text="Year")
l3.grid(row=3,column=0)

l4=Label(window, text="First Owner")
l4.grid(row=1,column=0)

l5=Label(window, text="VIN#")
l5.grid(row=1,column=2)

make_text=StringVar()
e1=Entry(window,textvariable=make_text)
e1.grid(row=0,column=1)

model_text=StringVar()
e2=Entry(window,textvariable=model_text)
e2.grid(row=0,column=3)


year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=3,column=1)


firstOwner_text=StringVar()
e4=Entry(window,textvariable=firstOwner_text)
e4.grid(row=1,column=1)

vin_text=StringVar()
e5=Entry(window,textvariable=vin_text)
e5.grid(row=1,column=3)


list1=Listbox(window, height=6,width=35)
list1.grid(row=4,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=4,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(orient='vertical', command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window, text="View all", width=12,command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12,command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=3, column=4)

b4=Button(window, text="Update Selected", width=12, command=update_command)
b4.grid(row=4, column=3)

b5=Button(window, text="Delete Selected", width=12,command=delete_command)
b5.grid(row=5, column=3)


b5=Button(window, text="Close", width=12, command=window.destroy)
b5.grid(row=6, column=3)
window.mainloop()


#TODO: Create a sort button, which will allow user to sort by id