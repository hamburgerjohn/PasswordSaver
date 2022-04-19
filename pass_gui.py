from turtle import width
import python.build.database
from python.build.database import Database
from tkinter import *
from pass_settings import *
from pickletools import pybytes, pyunicode



root = Tk()
data = Database("localhost", "erick", "1234", "passwords")
root.config(padx=10, pady=10)

#############edit tables##############
Label(root, text="Table Name", width=20, height=1, font=("Ariel", 12)).grid(row=0, column=0)
te1 = Entry(root, width=20, borderwidth=5, font=("Ariel", 18))
te1.grid(row=0, column=1)

#############edit passwords##############
Label(root, text="Domain", width=10, font=("Ariel", 12)).grid(row=2, column=0)
pe1 = Entry(root, width=20,  borderwidth=5, font=("Ariel", 18))
Label(root, text="Username", width=10, font=("Ariel", 12)).grid(row=3, column=0)
pe2 = Entry(root, width=20,  borderwidth=5, font=("Ariel", 18))
Label(root, text="Password", width=10, font=("Ariel", 12)).grid(row=4, column=0)
pe3 = Entry(root, width=20,  borderwidth=5, font=("Ariel", 18))
pe1.grid(row=2, column=1, padx=30)
pe2.grid(row=3, column=1)
pe3.grid(row=4, column=1)

pl1 = Label(root, text="", width=15, font=("Ariel", 12))
pl1.grid(row=3, column=2)
pe4 = Text(root, width=13, height=1,  borderwidth=4, font=("Ariel", 18))
pe4.grid(row=4, column=2)
pe4.config(state=DISABLED)


##################Output#########################
ot1 = Text(root, width=20, height=1,borderwidth=5, font=("Ariel", 18))
ot1.grid(row=8, column=1)
ot1.config(state=DISABLED)
Label(root, text="Domain", width=10, font=("Ariel", 12)).grid(row=6, column=0)
Label(root, text="Username", width=10, font=("Ariel", 12)).grid(row=7, column=0)
oe1 = Entry(root, width=20,  borderwidth=5, font=("Ariel", 18))
oe1.grid(row=6, column=1)
oe2 = Entry(root, width=20,  borderwidth=5, font=("Ariel", 18))
oe2.grid(row=7, column=1)

###################Create Password#################
ct1 = Text(root, width=20, height=1,borderwidth=5, font=("Ariel", 18))
ct1.grid(row=9, column=1, pady=10)
ct1.config(state=DISABLED)

##################table evt#################
def evt_table(arg : str):
    pe4.config(state=NORMAL)
    pe4.delete("1.0", END)

    if arg == "Created":
        data.CreateTable(te1.get())
    elif arg == "Deleted":
        data.DropTable(te1.get())
    elif arg == "Selected":
        data.SetTable(te1.get())
    
    
    pl1.config(text="Table " + arg)
    pe4.insert(END, te1.get())
    te1.delete(0, END)
    pe4.config(state=DISABLED)

#################password evt###################
def evt_password_add():
    data.Insert(pe1.get(), pe2.get(), pe3.get())
def evt_password_delete():
    data.Remove(pe1.get(), pe2.get())
def evt_password_update():
    data.Update(pe1.get(), pe2.get(), pe3.get())

def evt_password(arg : str):
    if arg == "Insert":
        data.Insert(pe1.get(), pe2.get(), pe3.get())
    elif arg == "Remove":
        data.Remove(pe1.get(), pe2.get())
    else:
        data.Update(pe1.get(), pe2.get(), pe3.get())

    pe1.delete(0, END)
    pe2.delete(0, END)
    pe3.delete(0, END)

#################output evt####################
def evt_password_show():
    ot1.config(state=NORMAL)
    ot1.delete("1.0", END)
    ot1.insert(INSERT,data.GetPassword(oe1.get(), oe2.get()))
    ot1.config(state=DISABLED)
    oe1.delete(0, END)
    oe2.delete(0, END)

def evt_password_create():
    global special_chars
    special_chars = 0
    ct1.config(state=NORMAL)
    ct1.delete("1.0", END)
    ct1.insert(INSERT, pass_construct())
    ct1.config(state=DISABLED)

def evt_password_settings():
    pass_settings(root)

###################table buttons###############
tb1 = Button(root, text="Create Table", command=lambda: evt_table("Created"),pady=10,width=20, font=("Ariel", 12))
tb2 = Button(root, text="Delete Table", command=lambda: evt_table("Deleted"),pady=10,width=20, font=("Ariel", 12))
tb3 = Button(root, text="Select Table", command=lambda: evt_table("Selected"),pady=10,width=20, font=("Ariel", 12))
tb1.grid(row=1, column=0, pady=10)
tb2.grid(row=1, column=1)
tb3.grid(row=1, column=2)

##################password buttons###############
pb1 = Button(root, text="Add Password", command=lambda: evt_password("Insert"),pady=10,width=20, font=("Ariel", 12))
pb2 = Button(root, text="Remove Password", command=lambda: evt_password("Remove"),pady=10,width=20, font=("Ariel", 12))
pb3 = Button(root, text="Change Password", command=lambda: evt_password("Update"),pady=10,width=20, font=("Ariel", 12))
pb1.grid(row=5, column=0, pady=10)
pb2.grid(row=5, column=1)
pb3.grid(row=5, column=2)

##################Output Buttons#################
ob1 = Button(root, text="Show Password", command=evt_password_show,pady=10,width=20, font=("Ariel", 12))
ob1.grid(row=8, column=0)

##################Create Buttones###############
cb1 = Button(root, text="Create Password", command=evt_password_create, pady=10,width=20,font=("Ariel", 12))
cb1.grid(row=9, column=0)
cb1 = Button(root, text="Password Settings", command=evt_password_settings, pady=10,width=20, font=("Ariel", 12))
cb1.grid(row=9, column=2, pady=30)

root.mainloop()

