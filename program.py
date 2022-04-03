from json.encoder import py_encode_basestring, py_encode_basestring_ascii
from quopri import decodestring
import python.build.database
from python.build.database import Database
from tkinter import *
from pickletools import pybytes, pyunicode


root = Tk()
data = Database("localhost", "erick", "1234", "passwords")
data.SetTable("tim")

a = data.GetTable()
data.Insert("am", "er", "1234")
#############edit tables##############
Label(root, text="Table Name", width=20, height=1, font=("Ariel", 12)).grid(row=0, column=0)
tt1 = Entry(root, width=20, borderwidth=5, font=("Ariel", 18))
tt1.grid(row=1, column=0)



#############edit passwords##############
Label(root, text="Domain", width=20, font=("Ariel", 12)).grid(row=0, column=1)
pt1 = Entry(root, width=20,  borderwidth=5, font=("Ariel", 18))
Label(root, text="Username", width=20, font=("Ariel", 12)).grid(row=2, column=1)
pt2 = Entry(root, width=20,  borderwidth=5, font=("Ariel", 18))
Label(root, text="Password", width=20, font=("Ariel", 12)).grid(row=4, column=1)
pt3 = Entry(root, width=20,  borderwidth=5, font=("Ariel", 18))
pt1.grid(row=1, column=1)
pt2.grid(row=3, column=1)
pt3.grid(row=5, column=1)

##################table evt#################
def evt_table_add():
    data.CreateTable(tt1.get())
def evt_table_delete():
    data.DropTable(tt1.get())
def evt_table_select():
    print(tt1.get())
    data.SetTable(tt1.get())

#################password evt###################
def evt_password_add():
    data.Insert(pt1.get(), pt2.get(), pt3.get())
def evt_password_delete():
    data.Remove(pt1.get(), pt2.get())
def evt_password_update():
    data.Update(pt1.get(), pt2.get(), pt3.get())

###################table buttons###############
t1 = Button(root, text="Create Table", command=evt_table_add,padx=65, pady=15, font=("Ariel", 12))
t2 = Button(root, text="Delete Table", command=evt_table_delete,padx=65, pady=15, font=("Ariel", 12))
t3 = Button(root, text="Select Table", command=evt_table_select,padx=65, pady=15, font=("Ariel", 12))
t1.grid(row=2, column=0)
t2.grid(row=3, column=0)
t3.grid(row=4, column=0)

##################password buttons###############
p1 = Button(root, text="Add Password", command=evt_password_add,padx=81, pady=15, font=("Ariel", 12))
p2 = Button(root, text="Remove Password", command=evt_password_delete,padx=65, pady=15, font=("Ariel", 12))
p3 = Button(root, text="Change Password", command=evt_password_update,padx=67, pady=15, font=("Ariel", 12))
p1.grid(row=6, column=1)
p2.grid(row=7, column=1)
p3.grid(row=8, column=1)

root.mainloop()

