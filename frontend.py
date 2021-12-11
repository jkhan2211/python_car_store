from tkinter import *
#import backend
import backend

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(make_text.get(),model_text.get(),year_text.get(),firstOwner_text.get(),vin_text.get()):
        list1.insert(END,row)


def add_command():
    backend.insert(make_text.get(),model_text.get(),year_text.get(),firstOwner_text.get(),vin_text.get())


window = Tk()

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


b1=Button(window, text="View all", width=12,command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12,command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=3, column=4)

b4=Button(window, text="Update Selected", width=12)
b4.grid(row=4, column=3)

b5=Button(window, text="Delete Selected", width=12)
b5.grid(row=5, column=3)


b5=Button(window, text="Close", width=12)
b5.grid(row=6, column=3)
window.mainloop()