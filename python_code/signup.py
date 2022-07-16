#==================imports===================#
from ast import Or
import sqlite3
import re
import os
import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
#============================================#


root = Tk()

root.geometry("1340x699+5+0")
root.title("Sign Up Page")

user = StringVar()
mail = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()
new_user = StringVar()
new_passwd = StringVar()


with sqlite3.connect("C:/Users/ASUS/Desktop/PFA/Database/accounts.db") as db:
    cur = db.cursor()



def valid_phone(phn):
    if re.match(r"[[:<:]](06|07|05)\d{8}$", phn):
        return True
    return False

def valid_mail(mailo):
    if re.match(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|fr|ma|org)", mailo):
        return True
    return False

def signup(Event=None):
    global username
    username = user.get()
    email = mail.get()
    password = passwd.get()
    with sqlite3.connect("C:/Users/ASUS/Desktop/PFA/database/accounts.db") as db:
        cur = db.cursor()
    find_user = "SELECT * FROM accounts WHERE username = ?"
    cur.execute(find_user, [username])
    sameUser = cur.fetchall()
    find_user = "SELECT * FROM accounts WHERE email = ?"
    cur.execute(find_user, [email])
    sameMail = cur.fetchall()
    if username == "" and email == "" and password == "":
        messagebox.showerror("Oops!", "Please complet all the field.")
    elif username == "" and email == "":
        messagebox.showerror("Oops!", "Please complet all the field.")
    elif username == "" and email == "":
        messagebox.showerror("Oops!", "Please complet all the field.")
    elif username == "" and password == "":
        messagebox.showerror("Oops!", "Please complet all the field.")
    elif(username == ""):
        messagebox.showerror("Oops!", "Please enter a username.")
    elif(email == ""):
        messagebox.showerror("Oops!", "Please enter a Email.")
    elif (password == ""):
        messagebox.showerror("Oops!", "Please enter a password.")

    else:
        if valid_mail(email)==False:
            messagebox.showerror("Oops!", "Please enter a valid email.")

        elif sameUser:
            messagebox.showerror("Oops!", "This username is already taken. Try an other one")
            page1.entry1.delete(0, END)
            page1.entry3.delete(0, END)
        elif sameMail:
            messagebox.showerror("Oops!", "This email is taken by another account. Try an other one")
            page1.entry2.delete(0, END)
            page1.entry3.delete(0, END)
        else:
            with sqlite3.connect("C:/Users/ASUS/Desktop/PFA/database/accounts.db") as db:
                cur = db.cursor()
            insert = ("INSERT INTO accounts(username, email, password) VALUES(?,?,?)"
            )
            cur.execute(insert, [username, email, password])
            db.commit()
            messagebox.showinfo("Sign Up", "you have successfully signed up")
            os.system("python C:/Users/ASUS/Desktop/PFA/python_code/login.py")
            
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)
            page1.entry3.delete(0, END)
            root.destroy()
            os.system("python C:/Users/ASUS/Desktop/PFA/python_code/login.py")



class signup_page:
    def __init__(self, top=None):
        top.geometry("1340x699+5+0")
        top.resizable(0, 0)
        top.title("Sign Up Page")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1340, height=699)
        self.img = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/signup.png")
        self.label1.configure(image=self.img)

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.584, rely=0.274, width=184, height=24)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        #self.entry1.configure(background="#DEff05")
        self.entry1.configure(textvariable=user)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.584, rely=0.394, width=184, height=24)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        #self.entry2.configure(background="#DEff05")
        self.entry2.configure(textvariable=mail)

        self.entry3 = Entry(root)
        self.entry3.place(relx=0.584, rely=0.514, width=184, height=24)
        self.entry3.configure(font="-family {Poppins} -size 10")
        self.entry3.configure(relief="flat")
        #self.entry3.configure(background="#DEff05")
        self.entry3.configure(show="*")
        self.entry3.configure(textvariable=passwd)

        self.button1 = Button(root)
        self.button1.place(relx=0.584, rely=0.640, width=230, height=37)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#ffffff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#ffffff")
        self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="0")
        self.img5 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/img5.png")
        self.button1.configure(image=self.img5)
        self.button1.configure(command=signup)


page1 = signup_page(root)
root.bind("<Return>", signup)
root.mainloop()

