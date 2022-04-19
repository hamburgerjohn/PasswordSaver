import python.build.database
from python.build.database import Database
from pass_settings import pass_construct
from pickletools import pybytes, pyunicode


data = Database("localhost", "", "", "")

def formatOutput(op, arg, st) -> str:
    string = op + arg 
    
    while len(string) < 50:
        string += " "
    if st == 1:
        return string
    else:
        return "******************************************************\n* " + string + " *\n******************************************************"

createdpass = ""

while True:
    c = int(input("1: Tables\n2: Edit Passwords\n3: Get Password\n4: Create Password\n"))
    

    if c == 1:
        x = int(input("1: Create Table\n2: Delete Table\n3: Select Table\n"))
        table = input("Enter Table Name: ")
        if x == 1:
            data.CreateTable(table)
        elif x == 2:
            data.DropTable(table)
        elif x == 3:
            data.SetTable(table)
        else:
            print("retad")

    elif c == 2:
        x = int(input("1: Add Password\n2: Remove Password\n3: Change Password\n"))
        if x == 1:
            y = input("Use password: " + createdpass + "? (y/n)")
            print(formatOutput("Adding to ", data.GetTable(), 0))
            if y == 'y':
                data.Insert(input("Enter Domain: "), input("Enter Username: "), createdpass)
            else:
                data.Insert(input("Enter Domain: "), input("Enter Username: "), input("Enter Password: "))
        elif x == 2:
            print(formatOutput("Removing from ", data.GetTable(), 0))
            data.Remove(input("Enter Domain: "), input("Enter Username: "))
        elif x == 3:
            print(formatOutput("Updating ", data.GetTable(), 0))
            data.Update(input("Enter Domain: "), input("Enter Username: "), input("Enter Password: "))
        else:
            print("stupid")

    elif c == 3:
        domain = input("Enter Domain: ")
        user = input("Enter Username: ")
        print("*****************************************************")
        print("* " + formatOutput("Domain: ", domain,1) + "*")
        print("* " + formatOutput("User: ", user,1) + "*")
        print("* " + formatOutput("Password: ", data.GetPassword(domain, user,1)) + "*")
        print("*****************************************************")
    elif c == 4:
        passw = pass_construct()
        print(formatOutput("Created Password: ", passw, 0))
        
        x = input("Save Password? (y/n)")
        if x == "y":
            createdpass = passw
    else:
        print("Retard")