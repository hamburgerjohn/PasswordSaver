
import random
from tkinter import *
from tkinter.tix import CheckList

pass_length = 24
special_length = 4
integer_length = 4
special_chars = "!@#$%^&*"

def pass_construct() -> str:
    global pass_length, special_length, integer_length, special_chars
    password = ""
    pair = []
    for i in range(0 , pass_length):
        pair = [chr(random.randint(65, 90)),chr(random.randint(97, 122))]
        password += random.choice(pair)
        
    if len(special_chars) != 0:
        for i in range(0, special_length):
            index = random.randint(0, pass_length)
            password = password[:index] + special_chars[random.randint(0,len(special_chars)-1)] + password[index + 1:]
        
    for i in range(0, integer_length):
        index = random.randint(0, pass_length)
        password = password[:index] + str(random.randint(2,9)) + password[index + 1:]
    return password

def pass_settings(root):
    settings = Toplevel(root)
    settings.title("Password Config")
    settings.geometry("430x175")

    checklist = {
        '!' : IntVar(),
        '@' : IntVar(),
        '#' : IntVar(),
        '$' : IntVar(),
        '%' : IntVar(),
        '^' : IntVar(),
        '&' : IntVar(),
        '*' : IntVar()
    }

    Label(settings, text="Length of Password:", font=("Ariel", 10)).place(x=30, y=30)
    Label(settings, text="Special Characters:", font=("Ariel", 10)).place(x=30, y=60)
    Label(settings, text="How many integers:", font=("Ariel", 10)).place(x=30, y=90)
    lt = Entry(settings,width=2)
    lt.place(x=180, y=28)
    lt.insert(0, pass_length)
    st = Entry(settings,width=2)
    st.place(x=180, y=58)
    st.insert(0,special_length)
    it = Entry(settings,width=2)
    it.place(x=180, y=88)
    it.insert(0,integer_length)
    s1 = Checkbutton(settings, text="!", variable=checklist['!'], onvalue=1, offvalue=0)
    s1.place(x=220, y=30)
    s2 = Checkbutton(settings, text="@", variable=checklist['@'], onvalue=1, offvalue=0)
    s2.place(x=270, y=30)
    s3 = Checkbutton(settings, text="#", variable=checklist['#'], onvalue=1, offvalue=0)
    s3.place(x=320, y=30)
    s4 = Checkbutton(settings, text="$", variable=checklist['$'], onvalue=1, offvalue=0)
    s4.place(x=370, y=30)
    s5 = Checkbutton(settings, text="%", variable=checklist['%'], onvalue=1, offvalue=0)
    s5.place(x=220, y=60)
    s6 = Checkbutton(settings, text="^", variable=checklist['^'], onvalue=1, offvalue=0)
    s6.place(x=270, y=60)
    s7 = Checkbutton(settings, text="&", variable=checklist['&'], onvalue=1, offvalue=0)
    s7.place(x=320, y=60)
    s8 = Checkbutton(settings, text="*", variable=checklist['*'], onvalue=1, offvalue=0)
    s8.place(x=370, y=60)

    
    def evt_submit(settings):
        global pass_length, special_length, integer_length, special_chars
        pass_length = 8 if lt.get() == '' else int(lt.get())
        special_length = 0 if st.get() == '' else int(st.get())
        integer_length = 0 if it.get() == '' else int(it.get())
        special_chars = ""
        for k,v in checklist.items():
            if v.get():
                special_chars += k
                
        settings.destroy()
    
    
    b1 = Button(settings, width=15, height=2,text="Submit", font=("Ariel",10), command=lambda: evt_submit(settings)).place(x=245, y=105)

