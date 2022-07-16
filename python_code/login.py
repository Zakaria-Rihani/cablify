# ==================imports===================
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from time import strftime
from datetime import date
from tkinter import scrolledtext as tkst
from PIL import Image, ImageTk
from setuptools import Command
from tkvalidate import *
from math import *
import pandas as pd
import os
# ============================================

path = "C:/Users/ASUS/Desktop/pfa/"
facteur_f3_df = pd.read_excel(path + 'tableaux/facteur_f3.xlsx')
facteur_f4_df = pd.read_excel(path + 'tableaux/facteur_f4.xlsx')
facteur_f5_df = pd.read_excel(path + 'tableaux/facteur_f5.xlsx')
facteur_f6_df = pd.read_excel(path + 'tableaux/facteur_f6.xlsx')
facteur_f7_df = pd.read_excel(path + 'tableaux/facteur_f7.xlsx')
facteur_f8_df = pd.read_excel(path + 'tableaux/facteur_f8.xlsx')
facteur_f9_df = pd.read_excel(path + 'tableaux/facteur_f9.xlsx')
facteur_f10_df = pd.read_excel(path + 'tableaux/facteur_f10.xlsx')
section_cuivre_df = pd.read_excel(path + 'tableaux/section_cuivre_enterree.xlsx')
section_aluminium_df = pd.read_excel(path + 'tableaux/section_aluminium_enterree.xlsx')
section_cuivre_libre_df = pd.read_excel(path + 'tableaux/section_cuivre_libre.xlsx')
section_aluminium_libre_df = pd.read_excel(path + 'tableaux/section_aluminium_libre.xlsx')


root = Tk()
root.geometry("1341x699+5+0")
root.title("Log In Page")
root.iconphoto(False, PhotoImage(file='C:/Users/ASUS/Desktop/PFA/images/cable1.ico'))

user = StringVar()
passwd = StringVar()
fname = StringVar()
lname = StringVar()
on = 1   

with sqlite3.connect("C:/Users/ASUS/Desktop/PFA/Database/accounts.db") as db:
    cur = db.cursor()




class login_page:
    def __init__(self, top=None):
        top.geometry("1341x699")
        top.resizable(0, 0)
        top.title("Log In Page")

        self.label1 = Label(root)
        self.label1.place(relx=0, rely=0, width=1341, height=699)
        self.img = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/login.png")
        self.label1.configure(image=self.img)
        

        self.entry1 = Entry(root)
        self.entry1.place(relx=0.580, rely=0.356, width=184, height=24)
        self.entry1.configure(font="-family {Poppins} -size 10")
        self.entry1.configure(relief="flat")
        #self.entry1.configure(background="#DEff05")
        self.entry1.configure(textvariable=user)

        self.entry2 = Entry(root)
        self.entry2.place(relx=0.580, rely=0.476, width=184, height=24)
        self.entry2.configure(font="-family {Poppins} -size 10")
        self.entry2.configure(relief="flat")
        self.entry2.configure(show="*")
        # self.entry2.configure(background="#DEff05")
        self.entry2.configure(textvariable=passwd)

        self.button1 = Button(root)
        self.button1.place(relx=0.585, rely=0.598, width=229, height=42)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#ffffff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#ffffff")
        #self.button1.configure(font="-family {Poppins SemiBold} -size 20")
        self.button1.configure(borderwidth="0")
        self.img4 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/img4.png")
        self.button1.configure(image=self.img4)
        #self.button1.configure(text="""LOGIN""")
        self.button1.configure(command=self.login)

    def login(self, Event=None):
        global username
        username = user.get()
        password = passwd.get()

        with sqlite3.connect("C:/Users/ASUS/Desktop/PFA/database/accounts.db") as db:
            cur = db.cursor()
        find_user = "SELECT * FROM accounts WHERE username = ? and password = ?"
        cur.execute(find_user, [username, password])
        results = cur.fetchall() 
        if results:
            messagebox.showinfo("Login Page", "The login is successful.")
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)
            root.withdraw()
            global adm
            global page2
            adm = Toplevel()
            adm.iconphoto(False, PhotoImage(file='C:/Users/ASUS/Desktop/PFA/images/cable.ico'))
            page2 = Outils(adm)
            page2.time()
            adm.protocol("WM_DELETE_WINDOW", exitt)
            adm.mainloop()

        else:
            print("")
            messagebox.showerror("Error", "Incorrect username or password.")
            page1.entry2.delete(0, END)

    
def exitt():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
    if sure == True:
        adm.destroy()
        root.destroy()

def calcul_section():
    adm.withdraw()
    global inv
    global page3
    inv = Toplevel()
    page3 = CaracteristiqueElectrique(inv)
    page3.time()
    inv.mainloop()



def Suivant():
    adm.withdraw()
    global invoice
    global page7
    invoice = Toplevel()
    page7 = modePose(invoice)
    page7.time()
    #invoice.protocol("WM_DELETE_WINDOW", exitt)
    inv.destroy()
    invoice.mainloop()

def Suivant2():
    adm.withdraw()
    global result
    global page8
    invoice.destroy()
    result = Toplevel()
    page8 = InitialResult(result)
    page8.time()
    #invoice.protocol("WM_DELETE_WINDOW", exitt)
    result.mainloop()

def Suivant3():
    adm.withdraw()
    global drop
    global page9
    result.destroy()
    drop = Toplevel()
    page9 = DropVoltage(drop)
    page9.time()
    #invoice.protocol("WM_DELETE_WINDOW", exitt)
    drop.mainloop()

def Retour1():
    adm.withdraw()
    global inv
    global page3
    invoice.destroy()
    inv = Toplevel()
    inv.iconphoto(False, PhotoImage(file='C:/Users/ASUS/Desktop/PFA/images/cable.ico'))
    page3 = CaracteristiqueElectrique(inv)
    page3.time()
    inv.protocol("WM_DELETE_WINDOW", exitt)
    inv.mainloop()

def Retour2():
    adm.withdraw()
    global invoice
    global page7
    result.destroy()
    invoice = Toplevel()
    page7 = modePose(invoice)
    page7.time()
    #invoice.protocol("WM_DELETE_WINDOW", exitt)
    invoice.mainloop()

def Retour3():
    adm.withdraw()
    global result
    global page8
    drop.destroy()
    result = Toplevel()
    page8 = InitialResult(result)
    page8.time()
    #invoice.protocol("WM_DELETE_WINDOW", exitt)
    result.mainloop()

def about():
    pass 



class Outils:
    def __init__(self, top=None):
        top.geometry("1340x699+5+0")
        top.resizable(0, 0)
        top.title("Home Page")

        self.label1 = Label(adm)
        self.label1.place(relx=0, rely=0, width=1340, height=699)
        self.img = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/home.png")
        self.label1.configure(image=self.img)

        self.message = Label(adm)
        self.message.place(relx=0.267, rely=0.090, width=90, height=30)
        self.message.configure(font="-family {Poppins ExtraBold} -size 16")
        self.message.configure(foreground="#757198")
        self.message.configure(background="#ffffff")
        self.message.configure(text=username)
        self.message.configure(anchor="w")

        self.clock1 = Label(adm)
        self.clock1.place(relx=0.846, rely=0.027, width=102, height=36)
        self.clock1.configure(font="-family {Poppins} -size 12")
        self.clock1.configure(foreground="#ffffff")
        self.clock1.configure(background="#7f74d0")

        self.button1 = Button(adm)
        self.button1.place(relx=0.625, rely=0.826, width=117, height=30)
        self.button1.configure(relief="flat")
        self.button1.configure(overrelief="flat")
        self.button1.configure(activebackground="#ffffff")
        self.button1.configure(cursor="hand2")
        self.button1.configure(foreground="#ffffff")
        self.button1.configure(background="#ffffff")
        self.button1.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon2 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/logout.png")
        self.button1.configure(image=self.icon2) 
        self.button1.configure(borderwidth="0")
        self.button1.configure(text="""Logout""")
        self.button1.configure(command=self.Logout)

        self.button2 = Button(adm)
        self.button2.place(relx=0.538, rely=0.348, width=154, height=69)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#ffffff")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#333333")
        self.button2.configure(background="#ffffff")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon3 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/icon1.png")
        self.button2.configure(image=self.icon3)
        self.button2.configure(borderwidth="0")
        self.button2.configure(command=calcul_section)

        self.button3 = Button(adm)
        self.button3.place(relx=0.684, rely=0.348, width=154, height=69)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#ffffff")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="#333333")
        self.button3.configure(background="#ffffff")
        self.button3.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon4 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/icon2.png")
        self.button3.configure(image=self.icon4)
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="")
        self.button3.configure(command=about)


        self.button4 = Button(adm)
        self.button4.place(relx=0.538, rely=0.513, width=154, height=69)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#ffffff")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="#333333")
        self.button4.configure(background="#ffffff")
        self.button4.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon5 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/icon2.png")
        self.button4.configure(image=self.icon5)
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="")
        self.button4.configure(command=about)


        self.button5 = Button(adm)
        self.button5.place(relx=0.684, rely=0.513, width=154, height=69)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#ffffff")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="#333333")
        self.button5.configure(background="#ffffff")
        self.button5.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon6 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/icon2.png")
        self.button5.configure(image=self.icon6)
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="")
        self.button5.configure(command=about)

    def time(self):
        string1 = strftime("%H:%M:%S %p")
        self.clock1.config(text=string1)
        self.clock1.after(1000, self.time)

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?", parent=adm)
        if sure == True:
            adm.destroy()
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

class CaracteristiqueElectrique:
    def __init__(self, top=None):
        top.geometry("1340x699+5+0")
        top.resizable(0, 0)
        top.title("Section Calculation")

        self.label1 = Label(inv)
        self.label1.place(relx=0, rely=0, width=1340, height=699)
        self.img = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/page1.png")
        self.label1.configure(image=self.img)

        self.message = Label(inv)
        self.message.place(relx=0.267, rely=0.09, width=90, height=30)
        self.message.configure(font="-family {Poppins} -size 16")
        self.message.configure(foreground="#757198")
        self.message.configure(background="#ffffff")
        self.message.configure(text=username)
        self.message.configure(anchor="w")

        self.clock = Label(inv)
        self.clock.place(relx=0.92, rely=0.009, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#ffffff")
        self.clock.configure(background="#7c6dcd")


        self.button2 = Button(inv)
        self.button2.place(relx=0.712, rely=0.864, width=117, height=30)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#757198")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#7c6dcd")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon2 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/logout.png")
        self.button2.configure(image=self.icon2)
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)


        self.button6 = Button(inv)
        self.button6.place(relx=0.54, rely=0.861, width=113, height=33)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#757198")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#7c6dcd")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.retour = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/retour.png")
        self.button6.configure(image=self.retour)
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=self.Exit)

        self.labelframe = LabelFrame(inv, text="calcul", fg="#ffffff")
        self.labelframe.place(relx=0.52, rely=0.18, width=410, height=450)
        self.labelframe.configure(background="#716cac")
        self.labelframe.configure(foreground="#ffffff")
        self.labelframe.configure(font="-family {Poppins SemiBold} -size 18")

        self.type_alim = Label(self.labelframe, text="Type D'alimentation   :")
        self.type_alim.place(relx=0.01, rely=0.01, width=154, height=50)
        self.type_alim.configure(background="#716cac")
        self.type_alim.configure(foreground="#ffffff")
        self.type_alim.configure(font="-family {Poppins SemiBold} -size 12")

        global v0
        v0=StringVar(self.labelframe, "1")
        v0.set(1)
        self.r1=ttk.Radiobutton(self.labelframe, text="Alternatif (ca)", variable=v0, value=1, style = "BW.TRadiobutton", command= lambda: self.r4.configure(state=NORMAL))
        self.r2=ttk.Radiobutton(self.labelframe, text="Continu (cc)", variable=v0,value=2, style = "BW.TRadiobutton", command= self.Disable_r4)
        self.style = ttk.Style()
        self.style.configure("BW.TRadiobutton", foreground="#ffffff", background="#716cac",font="-family {Poppins SemiBold} -size 12")
        self.r1.place(relx=0.42, rely=0.02, width=114, height=50)
        self.r2.place(relx=0.73, rely=0.02, width=109, height=50)
        self.r1.invoke()

        self.type_res = Label(self.labelframe, text="Type De Réseaux       :")
        self.type_res.place(relx=0.01, rely=0.11, width=154, height=50)
        self.type_res.configure(background="#716cac")
        self.type_res.configure(foreground="#ffffff")
        self.type_res.configure(font="-family {Poppins SemiBold} -size 12")

        global v1
        v1=StringVar(self.labelframe, "1")
        v1.set(3)
        self.r3=ttk.Radiobutton(self.labelframe, text="Monophasé", variable=v1,value=3, style = "BW.TRadiobutton")
        self.r4=ttk.Radiobutton(self.labelframe, text="Triphasé", variable=v1,value=4, style = "BW.TRadiobutton")
        self.style = ttk.Style() 
        self.style.configure("BW.TRadiobutton", foreground="#ffffff", background="#716cac",font="-family {Poppins SemiBold} -size 12")
        self.style.map(
        "BW.TRadiobutton",
        foreground=[("disabled", "#c8bfe7")]
        )
        self.r3.place(relx=0.42, rely=0.11, width=115, height=50)
        self.r4.place(relx=0.73, rely=0.11, width=109, height=50)
        self.r4.invoke()

        self.type_res = Label(self.labelframe, text="Tension du réseaux U :")
        self.type_res.place(relx=0.01, rely=0.21, width=157, height=50)
        self.type_res.configure(background="#716cac")
        self.type_res.configure(foreground="#ffffff")
        self.type_res.configure(font="-family {Poppins SemiBold} -size 12")
        global selected_tension
        selected_tension = StringVar()
        self.reseau_tension = ttk.Combobox(self.labelframe, textvariable=selected_tension)
        self.reseau_tension['values'] = (
                          '12', 
                          '24',
                          '50',
                          '127',
                          '230',
                          '400',
                          '500',
                          '1000',
                          '1500')
        self.reseau_tension.place(relx=0.43, rely=0.244, width=220, height=22)
        self.reseau_tension['state'] = 'readonly'  # normal
        self.reseau_tension.set("Sélectionner la tension du réseau")

        self.lab_perso = Label(self.labelframe, text="Personnalisé")
        self.lab_perso.place(relx=0.46, rely=0.31, width=100, height=30)
        self.lab_perso.configure(background="#716cac", disabledforeground="#c8bfe7", state=DISABLED)
        self.lab_perso.configure(foreground="#ffffff")
        self.lab_perso.configure(font="-family {Poppins } -size 10")

        self.lab_v = Label(self.labelframe, text="V")
        self.lab_v.place(relx=0.81, rely=0.32, width=15, height=22)
        self.lab_v.configure(background="#716cac", disabledforeground="#c8bfe7", state=DISABLED)
        self.lab_v.configure(foreground="#ffffff")
        self.lab_v.configure(font="-family {Poppins } -size 10")
        
        global tension_perso
        tension_perso = StringVar()
        self.entry_per = Entry(self.labelframe)
        self.entry_per.place(relx=0.7, rely=0.325, width=40, height=18)
        self.entry_per.configure(font="-family {Poppins} -size 10", state=DISABLED)
        self.entry_per.configure(relief="flat", disabledbackground="#c8bfe7")
        #self.entry1.configure(background="#DEff05")
        self.entry_per.configure(textvariable=tension_perso)
        float_validate(self.entry_per, from_=0, to=1000000000000)

        global CheckVar1
        CheckVar1 = BooleanVar()
        self.tension_perso = ttk.Checkbutton(self.labelframe, text="", variable = CheckVar1, onvalue = 1, offvalue = 0,style = "BW.TCheckbutton", command= self.disable_perso)
        self.tension_perso.place(relx=0.43, rely=0.32)
        self.style.configure("BW.TCheckbutton", foreground="#ffffff", background="#716cac",font="-family {Poppins SemiBold} -size 12")        
        
        self.dipo_protection = Label(self.labelframe, text="Dispositif de potection :")
        self.dipo_protection.place(relx=0.01, rely=0.385, width=170, height=22)
        self.dipo_protection.configure(background="#716cac")
        self.dipo_protection.configure(foreground="#ffffff")
        self.dipo_protection.configure(font="-family {Poppins SemiBold} -size 12")

        global selected_dispo
        selected_dispo = StringVar()
        self.dispo_protection = ttk.Combobox(self.labelframe, textvariable=selected_dispo)
        self.dispo_protection['values'] = (
                          'Disjoncteur', 
                          'Fusible < 10 A',
                          '10 A < Fusible < 25 A',
                          'Fusible > 25 A'
                         )
        self.dispo_protection.place(relx=0.43, rely=0.39, width=220, height=22)
        self.dispo_protection['state'] = 'readonly'  # normal
        self.dispo_protection.set("Disjoncteur")

        self.courant = Label(self.labelframe, text="Courant en Ampéres  :")
        self.courant.place(relx=0.01, rely=0.435, width=154, height=50)
        self.courant.configure(background="#716cac")
        self.courant.configure(foreground="#ffffff")
        self.courant.configure(font="-family {Poppins SemiBold} -size 12")

        global courant
        courant = StringVar()
        self.entry_courant = Entry(self.labelframe)
        self.entry_courant.place(relx=0.43, rely=0.475, width=50, height=18)
        self.entry_courant.configure(font="-family {Poppins} -size 10")
        self.entry_courant.configure(relief="flat", disabledbackground="#c8bfe7")
        self.entry_courant.configure(textvariable=courant)
        float_validate(self.entry_courant, from_=0, to=1000000000000)

        self.lab_A = Label(self.labelframe, text="A")
        self.lab_A.place(relx=0.57, rely=0.47, width=15, height=22)
        self.lab_A.configure(background="#716cac")
        self.lab_A.configure(foreground="#ffffff")
        self.lab_A.configure(font="-family {Poppins SemiBold} -size 12")

        global CheckVar2
        CheckVar2 = BooleanVar()
        self.calc_courant = ttk.Checkbutton(self.labelframe, text="Calculer l'intensité (A)", variable = CheckVar2, onvalue = 1, offvalue = 0,style = "BW.TCheckbutton", command= self.disableSousFrame)
        self.calc_courant.place(relx=0.03, rely=0.54)
        self.style.configure("BW.TCheckbutton", foreground="#ffffff", background="#716cac",font="-family {Poppins SemiBold} -size 11")         
        
        self.sousFrame = LabelFrame(self.labelframe, text="Sélectionnez la puissance", fg="#ffffff")
        self.sousFrame.place_forget()
        self.sousFrame.configure(background="#716cac")
        self.sousFrame.configure(foreground="#ffffff")
        self.sousFrame.configure(font="-family {Poppins SemiBold} -size 11")

        global v2
        v2=StringVar(self.sousFrame, "1")
        v2.set(1)
        self.r5=ttk.Radiobutton(self.sousFrame, text="Apparente :", variable=v2,value=5, style = "BW.TRadiobutton", command=self.disable_calc_courant)
        self.r6=ttk.Radiobutton(self.sousFrame, text="Active :", variable=v2,value=6, style = "BW.TRadiobutton", command=self.disable_calc_courant)
        self.style = ttk.Style() 
        self.style.configure("BW.TRadiobutton", foreground="#ffffff", background="#716cac",font="-family {Poppins SemiBold} -size 10")
        self.style.map(
        "BW.TRadiobutton",
        foreground=[("disabled", "#c8bfe7")]
        )
        self.r5.place(relx=0.01, rely=0.03, width=115, height=30)
        self.r6.place(relx=0.01, rely=0.3, width=109, height=30)
        self.r5.invoke()

        global puissance_app
        puissance_app = StringVar()
        self.entryPuisanceApp = Entry(self.sousFrame, textvariable=puissance_app)
        self.entryPuisanceApp.place(relx=0.26, rely=0.08, width=50, height=18)
        self.entryPuisanceApp.configure(font="-family {Poppins} -size 10")
        self.entryPuisanceApp.configure(relief="flat", disabledbackground="#c8bfe7")
        float_validate(self.entryPuisanceApp, from_=0, to=1000000000000)

        self.lab_KVA = Label(self.sousFrame, text="kVA")
        self.lab_KVA.place(relx=0.41, rely=0.07, width=30, height=22)
        self.lab_KVA.configure(background="#716cac")
        self.lab_KVA.configure(foreground="#ffffff", disabledforeground="#c8bfe7")
        self.lab_KVA.configure(font="-family {Poppins SemiBold} -size 10")

        global puissance_act
        puissance_act = StringVar()
        self.entry_puissance_act = Entry(self.sousFrame, textvariable=puissance_act)
        self.entry_puissance_act.place(relx=0.26, rely=0.37, width=50, height=18)
        self.entry_puissance_act.configure(font="-family {Poppins} -size 10")
        self.entry_puissance_act.configure(relief="flat", disabledbackground="#c8bfe7", state=DISABLED)
        float_validate(self.entry_puissance_act, from_=0, to=1000000000000)

        self.lab_KW = Label(self.sousFrame, text="kW")
        self.lab_KW.place(relx=0.41, rely=0.35, width=25, height=22)
        self.lab_KW.configure(background="#716cac", state=DISABLED)
        self.lab_KW.configure(foreground="#ffffff", disabledforeground="#c8bfe7")
        self.lab_KW.configure(font="-family {Poppins SemiBold} -size 10")

        global cosPhi
        cosPhi = StringVar()
        self.entry_puissance_act_cos = Entry(self.sousFrame, textvariable=cosPhi)
        self.entry_puissance_act_cos.place(relx=0.7, rely=0.37, width=50, height=18)
        self.entry_puissance_act_cos.configure(font="-family {Poppins} -size 10")
        self.entry_puissance_act_cos.configure(relief="flat", disabledbackground="#c8bfe7", state=DISABLED)
        float_validate(self.entry_puissance_act_cos, from_=0, to=1)

        self.lab_cos = Label(self.sousFrame, text="Cos(φ):")
        self.lab_cos.place(relx=0.55, rely=0.35, width=50, height=22)
        self.lab_cos.configure(background="#716cac", state=DISABLED)
        self.lab_cos.configure(foreground="#ffffff", disabledforeground="#c8bfe7")
        self.lab_cos.configure(font="-family {Poppins SemiBold} -size 10")

        self.button_appliquer = Button(self.sousFrame)
        self.button_appliquer.place(relx=0.4, rely=0.78, width=76, height=23)
        self.button_appliquer.configure(relief="flat")
        self.button_appliquer.configure(overrelief="flat")
        self.button_appliquer.configure(activebackground="#757198")
        self.button_appliquer.configure(activeforeground="#ffffff")
        self.button_appliquer.configure(cursor="hand2")
        self.button_appliquer.configure(foreground="#716cac")
        self.button_appliquer.configure(background="#ffffff")
        self.button_appliquer.configure(font="-family {Poppins ExtraBold} -size 11")
        self.button_appliquer.configure(borderwidth="0")
        self.button_appliquer.configure(text="""Appliquer""")
        self.button_appliquer.configure(command=self.calcCourant)

        self.button_suivant = Button(self.labelframe)
        self.button_suivant.place(relx=0.808, rely=0.94, width=76, height=23)
        self.button_suivant.configure(relief="flat")
        self.button_suivant.configure(overrelief="flat")
        self.button_suivant.configure(activebackground="#757198")
        self.button_suivant.configure(activeforeground="#ffffff")
        self.button_suivant.configure(cursor="hand2")
        self.button_suivant.configure(foreground="#716cac")
        self.button_suivant.configure(background="#ffffff")
        self.button_suivant.configure(font="-family {Poppins ExtraBold} -size 12")
        self.button_suivant.configure(borderwidth="0")
        self.button_suivant.configure(text="""Suivant""")
        self.button_suivant.configure(command=self.next)
        
     


    def disable_calc_courant(self):
        if v2.get() == "5":
            self.entryPuisanceApp.config(state=NORMAL)
            self.lab_KVA.configure(state=NORMAL)
            self.entry_puissance_act.configure(state=DISABLED)
            self.lab_KW.configure(state=DISABLED)
            self.entry_puissance_act_cos.configure(state=DISABLED)
            self.lab_cos.configure(state=DISABLED)
        if v2.get() == "6":
            self.entry_puissance_act.configure(state=NORMAL)
            self.lab_KW.configure(state=NORMAL) 
            self.entry_puissance_act_cos.configure(state=NORMAL)
            self.lab_cos.configure(state=NORMAL)
            #self.entry_puissance_act.configure(textvariable=puissance_act)

            self.entryPuisanceApp.configure(state=DISABLED)
            self.lab_KVA.configure(state=DISABLED)

    

    def calcCourant(self):
        global test
        print(v0.get())
        if selected_tension.get() == "Sélectionner la tension du réseau" and CheckVar1.get() == 0:
            messagebox.showerror("Oops!!", "Pealse Sélectionner la tension du réseau .", parent=inv) 
            test = 0
        elif CheckVar1.get() == 1 and tension_perso.get() =="":
            messagebox.showerror("Oops!!", "Pealse Enter la tension du réseau .", parent=inv)
            test = 0
        elif CheckVar2.get() == 1 and v2.get() == "5" and puissance_app.get() == "":
            messagebox.showerror("Oops!!", "Pealse Entrer la puissance apparente .", parent=inv)
            test = 0
        elif CheckVar2.get() == 1 and v2.get() == "6" and puissance_act.get() == "" and cosPhi.get() =="":
            messagebox.showerror("Oops!!", "Pealse Entrer la puissance active & le Cos(φ) .", parent=inv)
            test = 0
        elif CheckVar2.get() == 1 and v2.get() == "6" and puissance_act.get() == "" and cosPhi.get() !="":
            messagebox.showerror("Oops!!", "Pealse Entrer la puissance active .", parent=inv)
            print(puissance_act.get())
            test = 0
        elif CheckVar2.get() == 1 and v2.get() == "6" and puissance_act.get() !="" and cosPhi.get() =="":
            messagebox.showerror("Oops!!", "Pealse Entrer le Cos(φ) .", parent=inv)
            test = 0
        elif v0.get() == "1":
            print("alternative")
            #alternative
            global Iz
            if selected_dispo.get() == "Disjoncteur":
                f_dispo = 1
            if selected_dispo.get() == "Fusible < 10 A":
                f_dispo = 1.31
            if selected_dispo.get() == "10 A < Fusible < 25 A":
                f_dispo = 1.21
            if selected_dispo.get() == "Fusible > 25 A":
                f_dispo = 1.10
            if CheckVar2.get() == 1:
                if v1.get() == "3":
                #monophasé
                    global courantCalculer
                    global tension
                    print("monophasé")
                    if CheckVar1.get() == 0:
                        print("tension")
                        tension = float(selected_tension.get())
                        if v2.get() == "5":
                            puissanceApp = float(puissance_app.get())
                            courantCalculer = (1000*puissanceApp)/tension
                        elif v2.get() == "6":
                            puissanceAct = float(puissance_act.get())
                            cosphi = float(cosPhi.get())
                            courantCalculer = (1000*puissanceAct)/(tension*cosphi)
                        self.entry_courant.delete(0,END)
                        self.entry_courant.insert(0, f"{courantCalculer:.2f}")
                        test = 1
                        
                    elif CheckVar1.get() == 1:
                        tension =float( tension_perso.get())
                        if v2.get() == "5":
                            puissanceApp = float(puissance_app.get())
                            courantCalculer = (1000*puissanceApp)/tension
                        elif v2.get() == "6":
                            puissanceAct = float(puissance_act.get())
                            cosphi = float(cosPhi.get())
                            courantCalculer = (1000*puissanceAct)/(tension*cosphi)
                        self.entry_courant.delete(0,END)
                        self.entry_courant.insert(0, f"{courantCalculer:.2f}")
                        print(f"{courantCalculer:.2f}")
                        test = 1
                    
                elif v1.get() == "4":
                #triphasé
                    if CheckVar1.get() == 0:
                        tension = float(selected_tension.get())
                        if v2.get() == "5":
                            puissanceApp = float(puissance_app.get())
                            courantCalculer = (1000*puissanceApp)/(sqrt(3)*tension)
                        elif v2.get() == "6":
                            puissanceAct = float(puissance_act.get())
                            cosphi = float(cosPhi.get())
                            courantCalculer = (1000*puissanceAct)/(sqrt(3)*tension*cosphi)
                        self.entry_courant.delete(0,END)
                        self.entry_courant.insert(0, f"{courantCalculer:.2f}")
                        print(f"{courantCalculer:.2f}")
                        test = 1
                        
                    elif CheckVar1.get() == 1:
                        tension = float(tension_perso.get())
                        if v2.get() == "5":
                            puissanceApp = float(puissance_app.get())
                            courantCalculer = (1000*puissanceApp)/(sqrt(3)*tension)
                        elif v2.get() == "6":
                            puissanceAct = float(puissance_act.get())
                            cosphi = float(cosPhi.get())
                            courantCalculer = (1000*puissanceAct)/(sqrt(3)*tension*cosphi)
                        self.entry_courant.delete(0,END)
                        self.entry_courant.insert(0, f"{courantCalculer:.2f}")
                        print(f"{courantCalculer:.2f}")    
                        test = 1        
            if CheckVar2.get() == 0:
                courantCalculer = float(courant.get())
                test = 1
            Iz = courantCalculer*f_dispo
            print("Iz = {}".format(Iz))
            
        #Continue
        elif v0.get() == "2":
            print("Continue")
            if CheckVar1.get() == 0:
                tension = float(selected_tension.get())
            elif CheckVar1.get() == 1:
                tensionPerso = tension_perso.get()
        
    def next(self):
        self.calcCourant()
        if test == 1:
            print("uygffffffffff")
            Suivant()
        else:
            print("bbbbbbb")
               
    
    def disable_perso(self):
        if CheckVar1.get() == 1:
           self.reseau_tension['state'] = 'disabled' 
           self.lab_perso.configure(state=NORMAL ) 
           self.lab_v.configure(state=NORMAL) 
           self.entry_per.configure(state=NORMAL, background="#ffffff") 
        if CheckVar1.get() == 0:
            self.reseau_tension['state'] = 'readonly' 
            self.entry_per.configure(disabledbackground="#c8bfe7")  
            self.entry_per.configure(state=DISABLED)  
            self.lab_perso.configure(state=DISABLED) 
            self.lab_v.configure(state=DISABLED) 

    def disableSousFrame(self):
        if CheckVar2.get() == 1:
            self.sousFrame.place(relx=0.03, rely=0.60, width=380, height=140)
            self.sousFrame.configure(background="#716cac")
            self.sousFrame.configure(foreground="#ffffff") 
            self.sousFrame.configure(font="-family {Poppins SemiBold} -size 11")
        if CheckVar2.get() == 0:
            self.sousFrame.place_forget()  
      
    
    def Disable_r4(self):
        self.r4.configure(state=DISABLED)
        self.r3.invoke()

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=inv)
        if sure == True:
            inv.destroy()
            adm.deiconify()

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

class modePose:
    def __init__(self, top=None):
        top.geometry("1340x699+5+0")
        top.resizable(0, 0)
        top.title("Section Calculation")

        self.label1 = Label(invoice)
        self.label1.place(relx=0, rely=0, width=1340, height=699)
        self.img = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/page2.png")
        self.label1.configure(image=self.img)

        self.message = Label(invoice)
        self.message.place(relx=0.267, rely=0.09, width=90, height=30)
        self.message.configure(font="-family {Poppins} -size 16")
        self.message.configure(foreground="#757198")
        self.message.configure(background="#ffffff")
        self.message.configure(text=username)
        self.message.configure(anchor="w")


        self.clock = Label(invoice)
        self.clock.place(relx=0.92, rely=0.009, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#ffffff")
        self.clock.configure(background="#7c6dcd")


        self.button2 = Button(invoice)
        self.button2.place(relx=0.712, rely=0.864, width=117, height=30)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#757198")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#7c6dcd")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon2 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/logout.png")
        self.button2.configure(image=self.icon2)
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)


        self.button6 = Button(invoice)
        self.button6.place(relx=0.54, rely=0.861, width=113, height=31)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#757198")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#7c6dcd")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon3 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/retour.png")
        self.button6.configure(image=self.icon3)
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=Retour1)

        self.labelframe = LabelFrame(invoice, text="Mode De Pose", fg="#ffffff")
        self.labelframe.place(relx=0.52, rely=0.18, width=410, height=450)
        self.labelframe.configure(background="#716cac")
        self.labelframe.configure(foreground="#ffffff")
        self.labelframe.configure(font="-family {Poppins SemiBold} -size 18")

        self.type_alim = Label(self.labelframe, text="Pose :")
        self.type_alim.place(relx=0.01, rely=0.01, width=60, height=50)
        self.type_alim.configure(background="#716cac")
        self.type_alim.configure(foreground="#ffffff")
        self.type_alim.configure(font="-family {Poppins SemiBold} -size 12")  


        global p0
        p0=StringVar(self.labelframe, "1")
        p0.set(1)
        self.r1=ttk.Radiobutton(self.labelframe, text="Pose à l’air libre", variable=p0, value=1, style = "BW.TRadiobutton", command= self.disable_enterre)
        self.r2=ttk.Radiobutton(self.labelframe, text="Pose enterrée", variable=p0,value=2, style = "BW.TRadiobutton", command= self.disable_non_enterre)
        self.style = ttk.Style()
        self.style.configure("BW.TRadiobutton", foreground="#ffffff", background="#716cac",font="-family {Poppins SemiBold} -size 10")
        self.r1.place(relx=0.22, rely=0.015, width=124, height=50)
        self.r2.place(relx=0.63, rely=0.015, width=109, height=50)
        self.r1.invoke()   
        
        self.souslabelframe = LabelFrame(self.labelframe, text="", fg="#ffffff")
        self.souslabelframe.place(relx=0.01, rely=0.12, width=400, height=365)
        self.souslabelframe.configure(background="#716cac", borderwidth = 0, highlightthickness = 0)
        self.souslabelframe.configure(foreground="#ffffff")
        self.souslabelframe.configure(font="-family {Poppins SemiBold} -size 11")

        self.temperature = Label(self.souslabelframe, text="Température ambiante :")
        self.temperature.place(relx=0.01, rely=0.01, width=170, height=50)
        self.temperature.configure(background="#716cac")
        self.temperature.configure(foreground="#ffffff")
        self.temperature.configure(font="-family {Poppins SemiBold} -size 12")
        
        global selected_temperature
        selected_temperature = StringVar()
        self.temperature_ambiant = ttk.Combobox(self.souslabelframe, textvariable=selected_temperature)
        self.temperature_ambiant['values'] = (
                        '  10', 
                        '  15',
                        '  20',
                        '  25',
                        '  35',
                        '  40',
                        '  45',
                        '  50',
                        '  55',
                        '  60',
                        '  65',
                        '  70',
                        '  75',
                        '  80' )
        self.temperature_ambiant.place(relx=0.48, rely=0.048, width=160, height=22)
        self.temperature_ambiant['state'] = 'readonly'  # normal
        self.temperature_ambiant.set('  20')  

        self.lab_v = Label(self.souslabelframe, text="°C")
        self.lab_v.place(relx=0.88, rely=0.048, width=15, height=22)
        self.lab_v.configure(background="#716cac", disabledforeground="#c8bfe7")
        self.lab_v.configure(foreground="#ffffff")
        self.lab_v.configure(font="-family {Poppins } -size 10")

        self.lab_isolation = Label(self.souslabelframe, text="Type d'Isolation :")
        self.lab_isolation.place(relx=0.01, rely=0.13, width=120, height=50)
        self.lab_isolation.configure(background="#716cac")
        self.lab_isolation.configure(foreground="#ffffff")
        self.lab_isolation.configure(font="-family {Poppins SemiBold} -size 12")
        
        global type_isolation
        type_isolation = StringVar()
        self.isolation = ttk.Combobox(self.souslabelframe, textvariable=type_isolation)
        self.isolation['values'] = (
                        'Elastromères (caoutchouc)', 
                        '  PVC ',
                        '  PR OU EPR ')
        self.isolation.place(relx=0.48, rely=0.164, width=160, height=22)
        self.isolation['state'] = 'readonly'  # normal
        self.isolation.set('  Selectionner un type')

        self.lab_chemin = Label(self.souslabelframe, text="Type de pose de câbles :")
        self.lab_chemin.place(relx=0.01, rely=0.25, width=182, height=50)
        self.lab_chemin.configure(background="#716cac")
        self.lab_chemin.configure(foreground="#ffffff")
        self.lab_chemin.configure(font="-family {Poppins SemiBold} -size 12")
        
        global type_chemin
        type_chemin = StringVar()
        self.chemin = ttk.Combobox(self.souslabelframe, textvariable=type_chemin)
        self.chemin['values'] = (
                        'Fixés sur un mur', 
                        'Fixés à un plafond ',
                        'Sur des chemins de cables',
                        'Sur des corbeaux', 
                        'Sur des échelles a cables',
                        'Dans des vides de construction',
                        'Dans des conduits',
                        'Dans des conduits profilés noyés',
                        'Dans des faux-plafonds',
                        'Dans des plafonds suspendus',
                        'Dans des goulottes fixées aux parois',
                        'Dans des caniveaux fermés',
                        'Dans des caniveaux ouverts ou ventilés')
        self.chemin.place(relx=0.48, rely=0.284, width=200, height=22)
        self.chemin['state'] = 'readonly'  # normal
        self.chemin.set('  Selectionner un type')
        self.chemin.bind("<<ComboboxSelected>>", self.Disable_horiz_verti)

        self.lab_joitif = Label(self.souslabelframe, text="Nombre de cables jointifs :")
        self.lab_joitif.place(relx=0.01, rely=0.38, width=187, height=50)
        self.lab_joitif.configure(background="#716cac")
        self.lab_joitif.configure(foreground="#ffffff")
        self.lab_joitif.configure(font="-family {Poppins SemiBold} -size 12")
        
        global NB_jointif
        NB_jointif = StringVar()
        self.jointif = ttk.Combobox(self.souslabelframe, textvariable=NB_jointif)
        self.jointif['values'] = (
                        '  1', 
                        '  2',
                        '  3',
                        '  4', 
                        '  5',
                        '  6',
                        '  7',
                        '  8',
                        '  9',
                        '  12',
                        '  16',
                        '  20')
        self.jointif.place(relx=0.48, rely=0.414, width=200, height=22)
        self.jointif['state'] = 'readonly'  # normal
        self.jointif.set('  Selectionner une valeur')

        self.lab_couche = Label(self.souslabelframe, text="Nombre de couches :")
        self.lab_couche.place(relx=0.01, rely=0.5, width=154, height=50)
        self.lab_couche.configure(background="#716cac")
        self.lab_couche.configure(foreground="#ffffff")
        self.lab_couche.configure(font="-family {Poppins SemiBold} -size 12")
        
        global NB_couche
        NB_couche = StringVar()
        self.couche = ttk.Combobox(self.souslabelframe, textvariable=NB_couche)
        self.couche['values'] = (
                        '--1--',
                        '--2--', 
                        '--3--',
                        '--4 ou 5--',
                        '--6 a 8--', 
                        '--9 et plus--')
        self.couche.place(relx=0.48, rely=0.534, width=200, height=22)
        self.couche['state'] = 'readonly'  # normal
        self.couche.set('  Selectionner une valeur')

        self.lab_horizontal = Label(self.souslabelframe, text="Nombre de conduits \n disposés horizontalement :")
        self.lab_horizontal.place(relx=0.01, rely=0.62, width=185, height=50)
        self.lab_horizontal.configure(background="#716cac")
        self.lab_horizontal.configure(foreground="#ffffff")
        self.lab_horizontal.configure(font="-family {Poppins SemiBold} -size 12")
        
        global NB_horizontal
        NB_horizontal = StringVar()
        self.horizontal = ttk.Combobox(self.souslabelframe, textvariable=NB_horizontal)
        self.horizontal['values'] = (
                        '  1', 
                        '  2',
                        '  3',
                        '  4', 
                        '  5',
                        '  6')
        self.horizontal.place(relx=0.48, rely=0.68, width=200, height=22)
        self.horizontal['state'] = 'disabled'  # normal
        self.horizontal.set('  Selectionner une valeur')

        self.lab_vertical = Label(self.souslabelframe, text="Nombre de conduits \n disposés verticalement     :")
        self.lab_vertical.place(relx=0.01, rely=0.77, width=184, height=50)
        self.lab_vertical.configure(background="#716cac")
        self.lab_vertical.configure(foreground="#ffffff")
        self.lab_vertical.configure(font="-family {Poppins SemiBold} -size 12")
        
        global NB_vertical
        NB_vertical = StringVar()
        self.vertical = ttk.Combobox(self.souslabelframe, textvariable=NB_vertical)
        self.vertical['values'] = (
                        '  1', 
                        '  2',
                        '  3',
                        '  4', 
                        '  5',
                        '  6')
        self.vertical.place(relx=0.48, rely=0.83, width=200, height=22)
        self.vertical['state'] = 'disabled'  # normal
        self.vertical.set('  Selectionner une valeur')
######################################################################################################

        self.souslabelframe2 = LabelFrame(self.labelframe, text="", fg="#ffffff")
        self.souslabelframe2.place_forget()

        self.lab_chemin_enterre = Label(self.souslabelframe2, text="Type de pose Enterrée :")
        self.lab_chemin_enterre.place(relx=0.01, rely=0, width=182, height=50)
        self.lab_chemin_enterre.configure(background="#716cac")
        self.lab_chemin_enterre.configure(foreground="#ffffff")
        self.lab_chemin_enterre.configure(font="-family {Poppins SemiBold} -size 12")
        
        global type_chemin2
        type_chemin2 = StringVar()
        self.chemin_enterre = ttk.Combobox(self.souslabelframe2, textvariable=type_chemin2)
        self.chemin_enterre['values'] = (
                        'Directement enterré dans le sol', 
                        'Enterrés en conduites')
        self.chemin_enterre.place(relx=0.48, rely=0.038, width=200, height=22)
        self.chemin_enterre['state'] = 'readonly'  # normal
        self.chemin_enterre.set('  Sélectionner un type')
        self.chemin_enterre.bind("<<ComboboxSelected>>", self.update_sections)

        self.temperature_sol = Label(self.souslabelframe2, text="Température du Sol :")
        self.temperature_sol.place(relx=0.01, rely=0.1, width=160, height=50)
        self.temperature_sol.configure(background="#716cac")
        self.temperature_sol.configure(foreground="#ffffff")
        self.temperature_sol.configure(font="-family {Poppins SemiBold} -size 12")

        global selected_temperature_enterre
        selected_temperature_enterre = StringVar()
        self.temperature_ambiant_enterre = ttk.Combobox(self.souslabelframe2, textvariable=selected_temperature_enterre)
        self.temperature_ambiant_enterre['values'] = (
                        '  10', 
                        '  15',
                        '  25',
                        '  30',
                        '  35',
                        '  40',
                        '  45',
                        '  50',
                        '  55',
                        '  60'
                            )
        self.temperature_ambiant_enterre.place(relx=0.48, rely=0.14, width=160, height=22)
        self.temperature_ambiant_enterre['state'] = 'readonly'  # normal
        self.temperature_ambiant_enterre.set('  25')  

        self.lab_C = Label(self.souslabelframe2, text="°C")
        self.lab_C.place(relx=0.88, rely=0.14, width=15, height=22)
        self.lab_C.configure(background="#716cac", disabledforeground="#c8bfe7")
        self.lab_C.configure(foreground="#ffffff")
        self.lab_C.configure(font="-family {Poppins } -size 10")

        self.lab2_isolation = Label(self.souslabelframe2, text="Type d'Isolation :")
        self.lab2_isolation.place(relx=0.01, rely=0.2, width=120, height=50)
        self.lab2_isolation.configure(background="#716cac")
        self.lab2_isolation.configure(foreground="#ffffff")
        self.lab2_isolation.configure(font="-family {Poppins SemiBold} -size 12")
        global type_isolation2
        type_isolation2 = StringVar()
        self.isolation2 = ttk.Combobox(self.souslabelframe2, textvariable=type_isolation2)
        self.isolation2['values'] = (
                        '  PVC ',
                        '  PR OU EPR ')
        self.isolation2.place(relx=0.48, rely=0.24, width=160, height=22)
        self.isolation2['state'] = 'readonly'  # normal
        self.isolation2.set('  PVC ')
        self.isolation2.bind("<<ComboboxSelected>>", self.update_values)

        self.resistance_sol = Label(self.souslabelframe2, text="Résistivité thermique\n du Sol :")
        self.resistance_sol.place(relx=0.01, rely=0.3, width=160, height=50)
        self.resistance_sol.configure(background="#716cac")
        self.resistance_sol.configure(foreground="#ffffff")
        self.resistance_sol.configure(font="-family {Poppins SemiBold} -size 12")

        global selected_resistance_sol
        selected_resistance_sol = StringVar()
        self.resistance_sol_box = ttk.Combobox(self.souslabelframe2, textvariable=selected_resistance_sol)
        self.resistance_sol_box['values'] = (
                        '  0.40', 
                        '  0.50',
                        '  0.70',
                        '  0.85',
                        '  1.00',
                        '  1.20',
                        '  1.50',
                        '  2.00',
                        '  2.50',
                        '  3.00'
                         )
        self.resistance_sol_box.place(relx=0.48, rely=0.36, width=160, height=22)
        self.resistance_sol_box['state'] = 'readonly'  # normal
        self.resistance_sol_box.set('  1.50')

        self.resistance_sol_unit = Label(self.souslabelframe2, text="K.m/W")
        self.resistance_sol_unit.place(relx=0.89, rely=0.36, width=45, height=22)
        self.resistance_sol_unit.configure(background="#716cac", disabledforeground="#c8bfe7")
        self.resistance_sol_unit.configure(foreground="#ffffff")
        self.resistance_sol_unit.configure(font="-family {Poppins } -size 10")

        self.nbr_conduits = Label(self.souslabelframe2, text="Nombre de Conduits :")
        self.nbr_conduits.place(relx=0.01, rely=0.43, width=160, height=50)
        self.nbr_conduits.configure(background="#716cac")
        self.nbr_conduits.configure(foreground="#ffffff")
        self.nbr_conduits.configure(font="-family {Poppins SemiBold} -size 12")

        global nbr_conduits
        nbr_conduits = StringVar()
        self.nbr_conduits_box = ttk.Combobox(self.souslabelframe2, textvariable=nbr_conduits)
        self.nbr_conduits_box['values'] = (
                        '  2', 
                        '  3',
                        '  4',
                        '  5',
                        '  6'
                         )
        self.nbr_conduits_box.place(relx=0.48, rely=0.48, width=160, height=22)
        self.nbr_conduits_box['state'] = 'readonly'  # normal
        self.nbr_conduits_box.set('  2')

################################################################################################################

        self.nbr_cable = Label(self.souslabelframe2, text="Nombre de Cable :")

        global nbr_cable
        nbr_cable = StringVar()
        self.nbr_cable_box = ttk.Combobox(self.souslabelframe2, textvariable=nbr_cable)
        self.nbr_cable_box['values'] = (
                        '  2', 
                        '  3',
                        '  4',
                        '  5',
                        '  6'
                         )
        self.nbr_cable_box['state'] = 'readonly'  # normal
        self.nbr_cable_box.set('  2')

        self.distance_cables = Label(self.souslabelframe2, text="Distance entre\n Cables :")

        global distance_cables
        distance_cables = StringVar()
        self.distance_cables_box = ttk.Combobox(self.souslabelframe2, textvariable=distance_cables)
        self.distance_cables_box['values'] = (
                        'En contact',
                        'Un diametre de cable',  
                        '0.25', 
                        '0.50',
                        '1.00'
                         )
        self.distance_cables_box['state'] = 'readonly'  # normal
        self.distance_cables_box.set('En contact')

########################################################################################################

        self.distance_conduits = Label(self.souslabelframe2, text="Distance entre\n Conduits :")
        self.distance_conduits.place(relx=0.01, rely=0.56, width=160, height=50)
        self.distance_conduits.configure(background="#716cac")
        self.distance_conduits.configure(foreground="#ffffff")
        self.distance_conduits.configure(font="-family {Poppins SemiBold} -size 12")

        global distance_conduits
        distance_conduits = StringVar()
        self.distance_conduits_box = ttk.Combobox(self.souslabelframe2, textvariable=distance_conduits)
        self.distance_conduits_box['values'] = (
                        '0.25', 
                        '0.50',
                        '1.00'
                         )
        self.distance_conduits_box.place(relx=0.48, rely=0.62, width=160, height=22)
        self.distance_conduits_box['state'] = 'readonly'  # normal
        self.distance_conduits_box.set('0.50')

        self.distance_conduits_unit = Label(self.souslabelframe2, text="m")
        self.distance_conduits_unit.place(relx=0.89, rely=0.62, width=15, height=22)
        self.distance_conduits_unit.configure(background="#716cac", disabledforeground="#c8bfe7")
        self.distance_conduits_unit.configure(foreground="#ffffff")
        self.distance_conduits_unit.configure(font="-family {Poppins } -size 10")

        self.nbr_circuit = Label(self.souslabelframe2, text="Nombre de cable \ndans un meme conduit :")
        self.nbr_circuit.place(relx=0.01, rely=0.71, width=170, height=50)
        self.nbr_circuit.configure(background="#716cac")
        self.nbr_circuit.configure(foreground="#ffffff")
        self.nbr_circuit.configure(font="-family {Poppins SemiBold} -size 12")

        global nbr_circuit
        nbr_circuit = StringVar()
        self.nbr_circuit_box = ttk.Combobox(self.souslabelframe2, textvariable=nbr_circuit)
        self.nbr_circuit_box['values'] = (
                        '  1', 
                        '  2',
                        '  3',
                        '  4', 
                        '  5',
                        '  6',
                        '  7', 
                        '  8',
                        '  9',
                        '  12', 
                        '  16',
                        '  20'
                         )
        self.nbr_circuit_box.place(relx=0.48, rely=0.77, width=160, height=22)
        self.nbr_circuit_box['state'] = 'readonly'  # normal
        self.nbr_circuit_box.set('  2')

        self.button_suivant = Button(invoice)
        self.button_suivant.place(relx=0.768, rely=0.788, width=76, height=23)
        self.button_suivant.configure(relief="flat")
        self.button_suivant.configure(overrelief="flat")
        self.button_suivant.configure(activebackground="#757198")
        self.button_suivant.configure(activeforeground="#ffffff")
        self.button_suivant.configure(cursor="hand2")
        self.button_suivant.configure(foreground="#716cac")
        self.button_suivant.configure(background="#ffffff")
        self.button_suivant.configure(font="-family {Poppins ExtraBold} -size 12")
        self.button_suivant.configure(borderwidth="0")
        self.button_suivant.configure(text="""Suivant""")
        self.button_suivant.configure(command=self.facteur_correction)

    def facteur_correction(self):
        if p0.get() == "1":
            if type_isolation.get() =="  Selectionner un type" or type_chemin.get() =="  Selectionner un type"              or NB_jointif.get() =="  Selectionner une valeur" or NB_couche.get() =="  Selectionner une valeur":
                messagebox.showerror("Oops!!", "Pealse Remplir toutes les champs .", parent=invoice)
            elif (type_chemin.get() == "Dans des conduits profilés noyés" or type_chemin.get() =="Dans des conduits")         and (NB_horizontal.get() =="  Selectionner une valeur" or NB_vertical.get() =="  Selectionner une valeur"):
                messagebox.showerror("Oops!!", "Pealse Remplir toutes les champs .", parent=invoice)
            else:
                global f, f1, f4, f5, f6, f7
                nb_de_couche  = facteur_f5_df['Nombre de couches'] == str(NB_couche.get())
                f5 = facteur_f5_df.loc[nb_de_couche,'F5'].tolist()

                if type_isolation.get() == "  PVC ":
                    f1 = sqrt((70 - float(selected_temperature.get()))/(70 - 30))
                elif type_isolation.get() == "Elastromères (caoutchouc)":
                    f1 = sqrt((60 - float(selected_temperature.get()))/(60 - 30))
                else:
                    f1 = sqrt((90 - int(selected_temperature.get()))/(90 - 30))
                if type_chemin.get() == "Dans des vides de construction"                         or type_chemin.get() == "Dans des conduits" or  type_chemin.get() == "Dans des conduits profilés noyés" or type_chemin.get() == "Dans des plafonds suspendus" or type_chemin.get() == "Dans des goulottes fixées aux parois" or type_chemin.get() == "Dans des caniveaux fermés" or type_chemin.get() == "Dans des caniveaux ouverts ou ventilés":
                    mode_pose = facteur_f4_df['Mode de pose'] == 'mode1'
                    f4 = facteur_f4_df.loc[mode_pose,int(NB_jointif.get())].tolist()
                    if type_chemin.get() == "Dans des vides de construction"                    or type_chemin.get() == "Dans des caniveaux fermés" or type_chemin.get() == "Dans des plafonds suspendus":
                        f = 0.95*f1*f4[0]*f5[0]
                    elif type_chemin.get() == "Dans des goulottes fixées aux parois" :
                        f = 0.9*f1*f4[0]*f5[0]
                    elif type_chemin.get() == "Dans des caniveaux ouverts ou ventilés" :
                        f = 1*f1*f4[0]*f5[0]
                    elif type_chemin.get() == "Dans des conduits" :
                        nbr_vertical = facteur_f6_df['Nombre de conduits vertical'] == int(NB_vertical.get())
                        f6 = facteur_f6_df.loc[nbr_vertical,int(NB_horizontal.get())].tolist()
                        f = 0.865*f1*f4[0]*f5[0]*f6[0]
                    elif type_chemin.get() == "Dans des conduits profilés noyés" :
                        nbr_vertical = facteur_f7_df['Nombre de conduits vertical'] == int(NB_vertical.get())
                        f7 = facteur_f7_df.loc[nbr_vertical,int(NB_horizontal.get())].tolist()
                        f = 0.865*f1*f4[0]*f5[0]*f7[0]
                elif type_chemin.get() == "Fixés sur un mur" or type_chemin.get() == "Sur des chemins de cables":
                    mode_pose = facteur_f4_df['Mode de pose'] == 'mode2'
                    f4 = facteur_f4_df.loc[mode_pose,int(NB_jointif.get())].tolist()
                    f = 1*f1*f4[0]*f5[0]
                elif type_chemin.get() == "Fixés à un plafond ":
                    mode_pose = facteur_f4_df['Mode de pose'] == 'mode3'
                    f4 = facteur_f4_df.loc[mode_pose,int(NB_jointif.get())].tolist()
                    f = 0.95*f1*f4[0]*f5[0]
                elif type_chemin.get() == "Sur des chemins de cables":
                    mode_pose = facteur_f4_df['Mode de pose'] == 'mode4'
                    f4 = facteur_f4_df.loc[mode_pose,int(NB_jointif.get())].tolist()
                    f = 1*f1*f4[0]*f5[0]
                elif type_chemin.get() == "Sur des corbeaux" or type_chemin.get() == "Sur des échelles a cables":
                    mode_pose = facteur_f4_df['Mode de pose'] == 'mode3'
                    f4 = facteur_f4_df.loc[mode_pose,int(NB_jointif.get())].tolist()
                    f = 1*f1*f4[0]*f5[0]
                print("f = {}".format(f))
                print(selected_temperature.get())
                print(type_isolation.get())
                print(type_chemin.get())
                print(NB_jointif.get())
                print(NB_couche.get()) 
                Suivant2()
        elif p0.get() == "2":
            if type_chemin2.get() =="  Sélectionner un type":
                messagebox.showerror("Oops!!", "Pealse Remplir toutes les champs .", parent=invoice)
            else:
                global f2
                global f3
                global f8
                global f9
                global f10
                
                resistance  = facteur_f3_df['Résistivité thermique du sol'] == float(selected_resistance_sol.get())
                f3 = facteur_f3_df.loc[resistance,'F3'].tolist()

                if type_isolation2.get() == "  PVC ":
                    f2 = sqrt((70 - float(selected_temperature_enterre.get()))/(70 - 20))
                else:
                    f2 = sqrt((90 - int(selected_temperature_enterre.get()))/(90 - 20))
                if type_chemin2.get() =="Directement enterré dans le sol":
                    nb_cable  = facteur_f10_df['Nombre de cables '] == int(nbr_cable.get())
                    f10 = facteur_f10_df.loc[nb_cable, distance_cables.get()].tolist()
                    f = f2*float(f3[0])*float(f10[0])
                elif type_chemin2.get() =="Enterrés en conduites":
                    nb_conduit  = facteur_f8_df['Nombre de conduits'] == int(nbr_conduits.get())
                    f8 = facteur_f8_df.loc[nb_conduit, distance_conduits.get()].tolist()
                    nb_cable_conduit  = facteur_f9_df['Nombre de cables'] == int(nbr_circuit.get())
                    f9 = facteur_f9_df.loc[nb_cable_conduit, 'F9'].tolist()
                    f = 0.8*f2*float(f3[0])*float(f8[0])*float(f9[0])
                print("f = {}".format(f))
                print(selected_temperature_enterre.get())
                print(selected_resistance_sol.get())
                Suivant2()
    
    def Disable_horiz_verti(self, arg):
        if type_chemin.get() != "Dans des conduits" and type_chemin.get() != "Dans des conduits profilés noyés":
            self.vertical['state'] = 'disabled' 
            self.horizontal['state'] = 'disabled'
        if type_chemin.get() == "Dans des conduits" or type_chemin.get() == "Dans des conduits profilés noyés":
            self.vertical['state'] = 'readonly'
            self.horizontal['state'] = 'readonly'
    
    def update_values(self, arg):
        if type_isolation2.get() == "  PVC ":
            self.temperature_ambiant_enterre['values'] = (
                        '  10', 
                        '  15',
                        '  25',
                        '  30',
                        '  35',
                        '  40',
                        '  45',
                        '  50',
                        '  55',
                        '  60'
                                )
        else:
            self.temperature_ambiant_enterre['values'] = (
                        '  10', 
                        '  15',
                        '  25',
                        '  30',
                        '  35',
                        '  40',
                        '  45',
                        '  50',
                        '  55',
                        '  60',
                        '  65',
                        '  70',
                        '  75',
                        '  80' )


    def disable_non_enterre(self):
        self.souslabelframe.place_forget() 
        self.souslabelframe2.place(relx=0.01, rely=0.12, width=400, height=365)
        self.souslabelframe2.configure(background="#716cac", borderwidth = 0, highlightthickness = 0)
        self.souslabelframe2.configure(foreground="#ffffff")
        self.souslabelframe2.configure(font="-family {Poppins SemiBold} -size 11")
    def disable_enterre(self):
        self.souslabelframe2.place_forget() 
        self.souslabelframe.place(relx=0.01, rely=0.12, width=400, height=365)
        self.souslabelframe.configure(background="#716cac", borderwidth = 0, highlightthickness = 0)
        self.souslabelframe.configure(foreground="#ffffff")
        self.souslabelframe.configure(font="-family {Poppins SemiBold} -size 11") 

    def update_sections(self, arg):
        if type_chemin2.get() == 'Directement enterré dans le sol':
            self.nbr_cable.place(relx=0.01, rely=0.43, width=160, height=50)
            self.nbr_cable.configure(background="#716cac")
            self.nbr_cable.configure(foreground="#ffffff")
            self.nbr_cable.configure(font="-family {Poppins SemiBold} -size 12")
            self.nbr_cable_box.place(relx=0.48, rely=0.47, width=160, height=22)
            self.distance_cables.place(relx=0.01, rely=0.53, width=160, height=50)
            self.distance_cables.configure(background="#716cac")
            self.distance_cables.configure(foreground="#ffffff")
            self.distance_cables.configure(font="-family {Poppins SemiBold} -size 12")
            self.distance_cables_box.place(relx=0.48, rely=0.59, width=160, height=22)
            self.distance_conduits_unit.place(relx=0.89, rely=0.59, width=15, height=22)
            self.distance_conduits.place_forget()
            self.distance_conduits_box.place_forget()
            self.nbr_conduits.place_forget()
            self.nbr_conduits_box.place_forget()
            self.nbr_circuit.place_forget()
            self.nbr_circuit_box.place_forget()
        else:
            self.nbr_conduits.place(relx=0.01, rely=0.43, width=160, height=50)
            self.nbr_conduits.configure(background="#716cac")
            self.nbr_conduits.configure(foreground="#ffffff")
            self.nbr_conduits.configure(font="-family {Poppins SemiBold} -size 12")
            self.nbr_conduits_box.place(relx=0.48, rely=0.48, width=160, height=22)
            self.distance_conduits.place(relx=0.01, rely=0.56, width=160, height=50)
            self.distance_conduits.configure(background="#716cac")
            self.distance_conduits.configure(foreground="#ffffff")
            self.distance_conduits.configure(font="-family {Poppins SemiBold} -size 12")
            self.distance_conduits_box.place(relx=0.48, rely=0.62, width=160, height=22)
            self.nbr_circuit.place(relx=0.01, rely=0.71, width=170, height=50)
            self.nbr_circuit.configure(background="#716cac")
            self.nbr_circuit.configure(foreground="#ffffff")
            self.nbr_circuit.configure(font="-family {Poppins SemiBold} -size 12")
            self.nbr_circuit_box.place(relx=0.48, rely=0.77, width=160, height=22)
            self.distance_conduits_unit.place(relx=0.89, rely=0.62, width=15, height=22)
            self.distance_cables.place_forget()
            self.distance_cables_box.place_forget()
            self.nbr_cable.place_forget()
            self.nbr_cable_box.place_forget()


    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=invoice)
        if sure == True:
            invoice.destroy()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            invoice.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)

class InitialResult:
    def __init__(self, top=None):
        top.geometry("1340x699+5+0")
        top.resizable(0, 0)
        top.title("Section Calculation")

        self.label1 = Label(result)
        self.label1.place(relx=0, rely=0, width=1340, height=699)
        self.img = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/page3.png")
        self.label1.configure(image=self.img)

        self.message = Label(result)
        self.message.place(relx=0.267, rely=0.09, width=90, height=30)
        self.message.configure(font="-family {Poppins} -size 16")
        self.message.configure(foreground="#757198")
        self.message.configure(background="#ffffff")
        self.message.configure(text=username)
        self.message.configure(anchor="w")


        self.clock = Label(result)
        self.clock.place(relx=0.92, rely=0.009, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#ffffff")
        self.clock.configure(background="#7c6dcd")


        self.button2 = Button(result)
        self.button2.place(relx=0.712, rely=0.864, width=117, height=30)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#757198")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#7c6dcd")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon2 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/logout.png")
        self.button2.configure(image=self.icon2)
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)


        self.button6 = Button(result)
        self.button6.place(relx=0.54, rely=0.861, width=113, height=31)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#757198")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#7c6dcd")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon3 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/retour.png")
        self.button6.configure(image=self.icon3)
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=Retour2)

        self.labelframe = LabelFrame(result, text="Caractéristiques électriques :", fg="#ffffff")
        self.labelframe.place(relx=0.52, rely=0.16, width=410, height=150)
        self.labelframe.configure(background="#716cac")
        self.labelframe.configure(foreground="#ffffff")
        self.labelframe.configure(font="-family {Poppins SemiBold} -size 16")
        if v0.get() == '1':
            type1 = "Alternatif (AC)"
        else:
            type1 = "Continu (CC)"
        self.type_alim = Label(self.labelframe, text="Type d'alimentation: ")
        self.type_alim.place(relx=0.01, rely=0.00, width=160, height=38)
        self.type_alim.configure(background="#716cac")
        self.type_alim.configure(foreground="#ffffff")
        self.type_alim.configure(font="-family {Poppins ExtraBold} -size 13")

        self.type_alim1 = Label(self.labelframe, text= type1)
        self.type_alim1.place(relx=0.385, rely=0.00, width=130, height=38)
        self.type_alim1.configure(background="#716cac")
        self.type_alim1.configure(foreground="#c0c0c0")
        self.type_alim1.configure(font="-family {Poppins ExtraBold} -size 13")

        self.type_reseau = Label(self.labelframe, text="Type de réseau     : ")
        self.type_reseau.place(relx=0.01, rely=0.23, width=160, height=38)
        self.type_reseau.configure(background="#716cac")
        self.type_reseau.configure(foreground="#ffffff")
        self.type_reseau.configure(font="-family {Poppins ExtraBold} -size 13")
        if v1.get() == '3':
            type1 = "Monophasé"
        else:
            type1 = "Triphasé"
        self.type_reseau1 = Label(self.labelframe, text= type1)
        self.type_reseau1.place(relx=0.385, rely=0.25, width=110, height=38)
        self.type_reseau1.configure(background="#716cac")
        self.type_reseau1.configure(foreground="#c0c0c0")
        self.type_reseau1.configure(font="-family {Poppins ExtraBold} -size 13")

        self.tension_reseau = Label(self.labelframe, text="Tension du réseau : ")
        self.tension_reseau.place(relx=0.01, rely=0.475, width=160, height=34)
        self.tension_reseau.configure(background="#716cac")
        self.tension_reseau.configure(foreground="#ffffff")
        self.tension_reseau.configure(font="-family {Poppins ExtraBold} -size 13")
        if CheckVar1.get() == 1:
            type1 = tension_perso.get() + " V"
        else:
            type1 = selected_tension.get() + " V"
        self.tension_reseau1 = Label(self.labelframe, text= type1)
        self.tension_reseau1.place(relx=0.385, rely=0.475, width=110, height=34)
        self.tension_reseau1.configure(background="#716cac")
        self.tension_reseau1.configure(foreground="#c0c0c0")
        self.tension_reseau1.configure(font="-family {Poppins ExtraBold} -size 13")

        self.courant = Label(self.labelframe, text="Courant en Ampére: ")
        self.courant.place(relx=0.01, rely=0.69, width=160, height=38)
        self.courant.configure(background="#716cac")
        self.courant.configure(foreground="#ffffff")
        self.courant.configure(font="-family {Poppins ExtraBold} -size 13")
        type1 = f"{courantCalculer:.2f}" + " A"
        self.courant = Label(self.labelframe, text= type1)
        self.courant.place(relx=0.385, rely=0.69, width=110, height=38)
        self.courant.configure(background="#716cac")
        self.courant.configure(foreground="#c0c0c0")
        self.courant.configure(font="-family {Poppins ExtraBold} -size 13")

        self.labelframe1 = LabelFrame(result, text="Pose :", fg="#ffffff")
        self.labelframe1.place(relx=0.52, rely=0.3755, width=410, height=230)
        self.labelframe1.configure(background="#716cac")
        self.labelframe1.configure(foreground="#ffffff")
        self.labelframe1.configure(font="-family {Poppins SemiBold} -size 16")
        if p0.get() == "1":
            type = "Pose à l’air libre"
            self.type_pose = Label(self.labelframe1, text="Type de pose              : ")
            self.type_pose.place(relx=0.01, rely=0.00, width=190, height=38)
            self.type_pose.configure(background="#716cac")
            self.type_pose.configure(foreground="#ffffff")
            self.type_pose.configure(font="-family {Poppins ExtraBold} -size 13")

            self.type_pose1 = Label(self.labelframe1, text= type)
            self.type_pose1.place(relx=0.45, rely=0.00, width=130, height=38)
            self.type_pose1.configure(background="#716cac")
            self.type_pose1.configure(foreground="#c0c0c0")
            self.type_pose1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.temperature = Label(self.labelframe1, text="Temperature ambiante : ")
            self.temperature.place(relx=0.01, rely=0.13, width=190, height=38)
            self.temperature.configure(background="#716cac")
            self.temperature.configure(foreground="#ffffff")
            self.temperature.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = selected_temperature.get() + " °C"
            self.temperature1 = Label(self.labelframe1, text= type1)
            self.temperature1.place(relx=0.45, rely=0.13, width=110, height=38)
            self.temperature1.configure(background="#716cac")
            self.temperature1.configure(foreground="#c0c0c0")
            self.temperature1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.type_chemin = Label(self.labelframe1, text="Type de chemin          : ")
            self.type_chemin.place(relx=0.01, rely=0.26, width=190, height=34)
            self.type_chemin.configure(background="#716cac")
            self.type_chemin.configure(foreground="#ffffff")
            self.type_chemin.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = type_chemin.get()
            self.type_chemin1 = Label(self.labelframe1, text= type1)
            self.type_chemin1.place(relx=0.45, rely=0.26, width=210, height=34)
            self.type_chemin1.configure(background="#716cac")
            self.type_chemin1.configure(foreground="#c0c0c0")
            self.type_chemin1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.type_isolation = Label(self.labelframe1, text="Type d'Isolation           : ")
            self.type_isolation.place(relx=0.01, rely=0.38, width=190, height=38)
            self.type_isolation.configure(background="#716cac")
            self.type_isolation.configure(foreground="#ffffff")
            self.type_isolation.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = type_isolation.get()
            self.type_isolation1 = Label(self.labelframe1, text= type1)
            self.type_isolation1.place(relx=0.45, rely=0.38, width=110, height=38)
            self.type_isolation1.configure(background="#716cac")
            self.type_isolation1.configure(foreground="#c0c0c0")
            self.type_isolation1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.nb_jointif = Label(self.labelframe1, text="Nombre de cable jointif : ")
            self.nb_jointif.place(relx=0.01, rely=0.51, width=190, height=38)
            self.nb_jointif.configure(background="#716cac")
            self.nb_jointif.configure(foreground="#ffffff")
            self.nb_jointif.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = NB_jointif.get()
            self.nb_jointif1 = Label(self.labelframe1, text= type1)
            self.nb_jointif1.place(relx=0.45, rely=0.51, width=110, height=38)
            self.nb_jointif1.configure(background="#716cac")
            self.nb_jointif1.configure(foreground="#c0c0c0")
            self.nb_jointif1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.nb_couche = Label(self.labelframe1, text="Nombre de Couche      : ")
            self.nb_couche.place(relx=0.01, rely=0.64, width=190, height=38)
            self.nb_couche.configure(background="#716cac")
            self.nb_couche.configure(foreground="#ffffff")
            self.nb_couche.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = NB_couche.get()
            self.nb_couche1 = Label(self.labelframe1, text= type1)
            self.nb_couche1.place(relx=0.45, rely=0.64, width=110, height=38)
            self.nb_couche1.configure(background="#716cac")
            self.nb_couche1.configure(foreground="#c0c0c0")
            self.nb_couche1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.facteur = Label(self.labelframe1, text="Facteur de correction total:")
            self.facteur.place(relx=0.01, rely=0.77, width=205, height=38)
            self.facteur.configure(background="#716cac")
            self.facteur.configure(foreground="#ffffff")
            self.facteur.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = f"{f:.2f}"
            self.facteur1 = Label(self.labelframe1, text= type1)
            self.facteur1.place(relx=0.5, rely=0.77, width=60, height=38)
            self.facteur1.configure(background="#716cac")
            self.facteur1.configure(foreground="#c0c0c0")
            self.facteur1.configure(font="-family {Poppins ExtraBold} -size 13")

            if type_chemin.get() == "Dans des vides de construction" or type_chemin.get() == "Dans des conduits" or type_chemin.get() == "Dans des conduits profilés noyés" or type_chemin.get() == "Dans des faux-plafonds" or type_chemin.get() == "Dans des plafonds suspendus" or type_chemin.get() == "Dans des goulottes fixées aux parois"  or type_chemin.get() == "Dans des caniveaux fermés" or type_chemin.get() == "Dans des caniveaux ouverts ou ventilés":
                if type_isolation.get() == "  PR OU EPR ":
                    if v1.get() =="3":
                        isolant = "isolant6"
                    else:
                        isolant = "isolant4"
                else:
                    if v1.get() =="3":
                        isolant = "isolant2"
                    else:
                        isolant = "isolant1"

            elif type_chemin.get() == "Fixés sur un mur" or type_chemin.get() == "Fixés à un plafond " or type_chemin.get() == "Sur des chemins de cables":
                if type_isolation.get() == "  PR OU EPR ":
                    if v1.get() =="3":
                        isolant = "isolant7"
                    else:
                        isolant = "isolant5"
                else:
                    if v1.get() =="3":
                        isolant = "isolant4"
                    else:
                        isolant = "isolant2"
            else:
                if type_isolation.get() == "  PR OU EPR ":
                    if v1.get() =="3":
                        isolant = "isolant8"
                    else:
                        isolant = "isolant6"
                else:
                    if v1.get() =="3":
                        isolant = "isolant5"
                    else:
                        isolant = "isolant3"

            Izz = Iz/f
            print(Izz)
            global section_cuivre
            global section_aluminium
            choix1  = section_aluminium_libre_df[isolant] >= Izz
            print(choix1)
            section_aluminium = section_aluminium_libre_df.loc[choix1,'Section de aluminium'].tolist()
            print(section_aluminium)
            choix2  = section_cuivre_libre_df[isolant] >= Izz
            print(choix2)
            section_cuivre = section_cuivre_libre_df.loc[choix2,'Section de cuivre'].tolist()
            print(section_cuivre)

        else: 
            type = "Pose enterrée"
            self.type_pose = Label(self.labelframe1, text="Type de pose              : ")
            self.type_pose.place(relx=0.01, rely=0.00, width=190, height=38)
            self.type_pose.configure(background="#716cac")
            self.type_pose.configure(foreground="#ffffff")
            self.type_pose.configure(font="-family {Poppins ExtraBold} -size 13")

            self.type_pose1 = Label(self.labelframe1, text= type)
            self.type_pose1.place(relx=0.45, rely=0.00, width=130, height=38)
            self.type_pose1.configure(background="#716cac")
            self.type_pose1.configure(foreground="#c0c0c0")
            self.type_pose1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.temperature = Label(self.labelframe1, text="Temperature du Sol     : ")
            self.temperature.place(relx=0.01, rely=0.13, width=190, height=38)
            self.temperature.configure(background="#716cac")
            self.temperature.configure(foreground="#ffffff")
            self.temperature.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = selected_temperature_enterre.get() + " °C"
            self.temperature1 = Label(self.labelframe1, text= type1)
            self.temperature1.place(relx=0.45, rely=0.13, width=110, height=38)
            self.temperature1.configure(background="#716cac")
            self.temperature1.configure(foreground="#c0c0c0")
            self.temperature1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.type_chemin = Label(self.labelframe1, text="Type de pose enterrée : ")
            self.type_chemin.place(relx=0.01, rely=0.26, width=190, height=34)
            self.type_chemin.configure(background="#716cac")
            self.type_chemin.configure(foreground="#ffffff")
            self.type_chemin.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = type_chemin2.get()
            self.type_chemin1 = Label(self.labelframe1, text= type1)
            self.type_chemin1.place(relx=0.45, rely=0.26, width=170, height=34)
            self.type_chemin1.configure(background="#716cac")
            self.type_chemin1.configure(foreground="#c0c0c0")
            self.type_chemin1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.resistance_sol = Label(self.labelframe1, text="Résistivité du Sol         : ")
            self.resistance_sol.place(relx=0.01, rely=0.38, width=190, height=38)
            self.resistance_sol.configure(background="#716cac")
            self.resistance_sol.configure(foreground="#ffffff")
            self.resistance_sol.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = selected_resistance_sol.get() + " K.m/W"
            self.resistance_sol1 = Label(self.labelframe1, text= type1)
            self.resistance_sol1.place(relx=0.45, rely=0.38, width=110, height=38)
            self.resistance_sol1.configure(background="#716cac")
            self.resistance_sol1.configure(foreground="#c0c0c0")
            self.resistance_sol1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.type_isolation = Label(self.labelframe1, text="Type d'Isolation           : ")
            self.type_isolation.place(relx=0.01, rely=0.51, width=190, height=38)
            self.type_isolation.configure(background="#716cac")
            self.type_isolation.configure(foreground="#ffffff")
            self.type_isolation.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = type_isolation2.get()
            self.type_isolation1 = Label(self.labelframe1, text= type1)
            self.type_isolation1.place(relx=0.45, rely=0.51, width=110, height=38)
            self.type_isolation1.configure(background="#716cac")
            self.type_isolation1.configure(foreground="#c0c0c0")
            self.type_isolation1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.nb_conduit = Label(self.labelframe1, text="Nombre de Conduit     : ")
            self.nb_conduit.place(relx=0.01, rely=0.51, width=190, height=38)
            self.nb_conduit.configure(background="#716cac")
            self.nb_conduit.configure(foreground="#ffffff")
            self.nb_conduit.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = nbr_conduits.get()
            self.nb_conduit1 = Label(self.labelframe1, text= type1)
            self.nb_conduit1.place(relx=0.45, rely=0.51, width=110, height=38)
            self.nb_conduit1.configure(background="#716cac")
            self.nb_conduit1.configure(foreground="#c0c0c0")
            self.nb_conduit1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.distance = Label(self.labelframe1, text="Distance entre Conduit: ")
            self.distance.place(relx=0.01, rely=0.64, width=190, height=38)
            self.distance.configure(background="#716cac")
            self.distance.configure(foreground="#ffffff")
            self.distance.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = distance_conduits.get()
            self.distance1 = Label(self.labelframe1, text= type1)
            self.distance1.place(relx=0.45, rely=0.64, width=110, height=38)
            self.distance1.configure(background="#716cac")
            self.distance1.configure(foreground="#c0c0c0")
            self.distance1.configure(font="-family {Poppins ExtraBold} -size 13")

            self.facteur = Label(self.labelframe1, text="Facteur de correction total:")
            self.facteur.place(relx=0.01, rely=0.77, width=205, height=38)
            self.facteur.configure(background="#716cac")
            self.facteur.configure(foreground="#ffffff")
            self.facteur.configure(font="-family {Poppins ExtraBold} -size 13")
            type1 = f"{f:.2f}"
            self.facteur1 = Label(self.labelframe1, text= type1)
            self.facteur1.place(relx=0.5, rely=0.77, width=110, height=38)
            self.facteur1.configure(background="#716cac")
            self.facteur1.configure(foreground="#c0c0c0")
            self.facteur1.configure(font="-family {Poppins ExtraBold} -size 13")

            if type_isolation2.get() == "  PVC ":
                if v1.get() =="3":
                    isolant = "PVC2"
                else:
                    isolant = "PVC3"
            else:
                if v1.get() =="3":
                    isolant = "PR2"
                else:
                    isolant = "PR3"
            Izz = Iz/f
            choix1  = section_aluminium_df[isolant] >= Izz
            section_aluminium = section_aluminium_df.loc[choix1,'Section de aluminium'].tolist()
            print(section_aluminium)
            choix2  = section_cuivre_df[isolant] >= Izz
            section_cuivre = section_cuivre_df.loc[choix2,'Section de cuivre'].tolist()
            print(section_cuivre)

        self.section_cuivre = Label(result, text= "La section recommandée pour le cuivre est :")
        self.section_cuivre.place(relx=0.52, rely=0.705, width=330, height=32)
        self.section_cuivre.configure(background="#716cac")
        self.section_cuivre.configure(foreground="#FBA4E6")
        self.section_cuivre.configure(font="-family {Poppins ExtraBold} -size 13")

        self.section_cuivre1 = Label(result, text= str(section_cuivre[0]) + " mm")
        self.section_cuivre1.place(relx=0.765, rely=0.705, width=82, height=32)
        self.section_cuivre1.configure(background="#716cac")
        self.section_cuivre1.configure(foreground="#FBA4E6")
        self.section_cuivre1.configure(font="-family {Poppins ExtraBold} -size 13")

        self.section_aluminium = Label(result, text= "La section recommandée pour l'aluminium est :")
        self.section_aluminium.place(relx=0.52, rely=0.74, width=350, height=32)
        self.section_aluminium.configure(background="#716cac")
        self.section_aluminium.configure(foreground="#FBA4E6")
        self.section_aluminium.configure(font="-family {Poppins ExtraBold} -size 13")

        self.section_aluminium1 = Label(result, text= str(section_aluminium[0]) + " mm")
        self.section_aluminium1.place(relx=0.78, rely=0.74, width=62, height=32)
        self.section_aluminium1.configure(background="#716cac")
        self.section_aluminium1.configure(foreground="#FBA4E6")
        self.section_aluminium1.configure(font="-family {Poppins ExtraBold} -size 13")

        self.button_suivant = Button(result,  )
        self.button_suivant.place(relx=0.6, rely=0.79, width=190, height=27)
        self.button_suivant.configure(relief="raised")
        self.button_suivant.configure(overrelief="raised")
        self.button_suivant.configure(activebackground="#757198")
        self.button_suivant.configure(activeforeground="#ffffff")
        self.button_suivant.configure(cursor="hand2")
        self.button_suivant.configure(foreground="#716cac")
        self.button_suivant.configure(background="#ffffff")
        self.button_suivant.configure(font="-family {Poppins ExtraBold} -size 12")
        self.button_suivant.configure(borderwidth="2")
        self.button_suivant.configure(text="""Vérifier la chute de tension""")
        self.button_suivant.configure(command=Suivant3)

        
    
    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=result)
        if sure == True:
            result.destroy()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            result.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)
    
class DropVoltage:
    def __init__(self, top=None):
        top.geometry("1340x699+5+0")
        top.resizable(0, 0)
        top.title("Section Calculation")

        self.label1 = Label(drop)
        self.label1.place(relx=0, rely=0, width=1340, height=699)
        self.img = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/page4.png")
        self.label1.configure(image=self.img)

        self.message = Label(drop)
        self.message.place(relx=0.267, rely=0.09, width=90, height=30)
        self.message.configure(font="-family {Poppins} -size 16")
        self.message.configure(foreground="#757198")
        self.message.configure(background="#ffffff")
        self.message.configure(text=username)
        self.message.configure(anchor="w")


        self.clock = Label(drop)
        self.clock.place(relx=0.92, rely=0.009, width=102, height=36)
        self.clock.configure(font="-family {Poppins Light} -size 12")
        self.clock.configure(foreground="#ffffff")
        self.clock.configure(background="#7c6dcd")


        self.button2 = Button(drop)
        self.button2.place(relx=0.704, rely=0.864, width=117, height=30)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#757198")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="#ffffff")
        self.button2.configure(background="#7c6dcd")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon2 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/logout.png")
        self.button2.configure(image=self.icon2)
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Logout""")
        self.button2.configure(command=self.Logout)


        self.button6 = Button(drop)
        self.button6.place(relx=0.54, rely=0.861, width=113, height=31)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#757198")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#ffffff")
        self.button6.configure(background="#7c6dcd")
        self.button6.configure(font="-family {Poppins SemiBold} -size 12")
        self.icon3 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/retour.png")
        self.button6.configure(image=self.icon3)
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""EXIT""")
        self.button6.configure(command=Retour3)

        self.principal_frame = LabelFrame(drop, text="", fg="#ffffff")
        self.principal_frame.place(relx=0.52, rely=0.18, width=410, height=380)
        self.principal_frame.configure(background="#716cac", borderwidth = 0, highlightthickness = 0)
        self.principal_frame.configure(foreground="#ffffff")
        self.principal_frame.configure(font="-family {Poppins SemiBold} -size 14")

        self.lenght = Label(self.principal_frame, text="Longeur du circuit         :")
        self.lenght.place(relx=0.01, rely=0.02, width=180, height=50)
        self.lenght.configure(background="#716cac")
        self.lenght.configure(foreground="#ffffff")
        self.lenght.configure(font="-family {Poppins SemiBold} -size 12")

        global lenght
        lenght = StringVar()
        self.entry_lenght = Entry(self.principal_frame)
        self.entry_lenght.place(relx=0.45, rely=0.07, width=110, height=18)
        self.entry_lenght.configure(font="-family {Poppins} -size 10")
        self.entry_lenght.configure(relief="flat", disabledbackground="#c8bfe7")
        self.entry_lenght.configure(textvariable=lenght)
        float_validate(self.entry_lenght, from_=0, to=1000000000000)

        self.lenght_unit = Label(self.principal_frame, text="m")
        self.lenght_unit.place(relx=0.73, rely=0.06, width=15, height=22)
        self.lenght_unit.configure(background="#716cac")
        self.lenght_unit.configure(foreground="#ffffff")
        self.lenght_unit.configure(font="-family {Poppins SemiBold} -size 12")

        self.power_factor = Label(self.principal_frame, text="Facteur de Puissance  :")
        self.power_factor.place(relx=0.01, rely=0.14, width=180, height=50)
        self.power_factor.configure(background="#716cac")
        self.power_factor.configure(foreground="#ffffff")
        self.power_factor.configure(font="-family {Poppins SemiBold} -size 12")

        global cosPhi
        cosPhi = StringVar()
        self.entry_puissance_act_cos = Entry(self.principal_frame, textvariable=cosPhi)
        self.entry_puissance_act_cos.place(relx=0.45, rely=0.19, width=110, height=18)
        self.entry_puissance_act_cos.configure(font="-family {Poppins} -size 10")
        self.entry_puissance_act_cos.configure(relief="flat")
        float_validate(self.entry_puissance_act_cos, from_=0, to=1)

        self.lab_cos = Label(self.principal_frame, text="Cos(φ)")
        self.lab_cos.place(relx=0.73, rely=0.18, width=50, height=22)
        self.lab_cos.configure(background="#716cac")
        self.lab_cos.configure(foreground="#ffffff", disabledforeground="#c8bfe7")
        self.lab_cos.configure(font="-family {Poppins SemiBold} -size 10")

        self.labelframe = LabelFrame(self.principal_frame, text="Chute de tension maximale autorisée :", fg="#ffffff")
        self.labelframe.place(relx=0.0, rely=0.28, width=410, height=180)
        self.labelframe.configure(background="#716cac")
        self.labelframe.configure(foreground="#ffffff")
        self.labelframe.configure(font="-family {Poppins SemiBold} -size 13")

        global v0
        v0=StringVar(self.labelframe, "1")
        v0.set(1)
        self.choice1=ttk.Radiobutton(self.labelframe, text="Installation industrielle :", variable=v0, value=1, style = "BW.TRadiobutton", command= self.disable_others)
        self.choice2=ttk.Radiobutton(self.labelframe, text="Logement et similaire  :", variable=v0,value=2, style = "BW.TRadiobutton", command= self.disable_others)
        self.choice3=ttk.Radiobutton(self.labelframe, text="Personnalisé              :", variable=v0,value=3, style = "BW.TRadiobutton", command= self.disable_others)
        self.style = ttk.Style()
        self.style.configure("BW.TRadiobutton", foreground="#ffffff", background="#716cac",font="-family {Poppins SemiBold} -size 10")
        self.choice1.place(relx=0.05, rely=0.015, width=160, height=50)
        self.choice2.place(relx=0.05, rely=0.3, width=160, height=50)
        self.choice3.place(relx=0.05, rely=0.6, width=160, height=50)
        self.choice1.invoke() 

        global indus_drop
        indus_drop = StringVar()
        self.indus_drop_box = ttk.Combobox(self.labelframe, textvariable=indus_drop)
        self.indus_drop_box['values'] = (
                        '  4.5', 
                        '  6.5'
                         )
        self.indus_drop_box.place(relx=0.45, rely=0.1, width=160, height=22)
        self.indus_drop_box['state'] = 'readonly'  # normal
        self.indus_drop_box.set('  4.5')  

        self.percente = Label(self.labelframe, text= " %")
        self.percente.place(relx=0.85, rely=0.055, width=18, height=38)
        self.percente.configure(background="#716cac")
        self.percente.configure(foreground="#c0c0c0")
        self.percente.configure(font="-family {Poppins ExtraBold} -size 13")

        global log_drop
        log_drop = StringVar()
        self.log_drop_box = ttk.Combobox(self.labelframe, textvariable=log_drop)
        self.log_drop_box['values'] = (
                        '  3', 
                        '  5'
                        )
        self.log_drop_box.place(relx=0.45, rely=0.38, width=160, height=22)
        self.log_drop_box['state'] = 'disabled'  # normal
        self.log_drop_box.set('  3')  

        self.percente1 = Label(self.labelframe, text= " %")
        self.percente1.place(relx=0.85, rely=0.335, width=18, height=38)
        self.percente1.configure(background="#716cac")
        self.percente1.configure(foreground="#c0c0c0")
        self.percente1.configure(font="-family {Poppins ExtraBold} -size 13")

        global person
        person = StringVar()
        self.spin_box = ttk.Spinbox(
            self.labelframe,
            from_=0,
            to=99,
            textvariable=person,
            wrap=True)
        self.spin_box['state'] = 'disabled'  # normal
        self.spin_box.place(relx=0.45, rely=0.68, width=160, height=20)
        self.spin_box.set(1)

        self.percente2 = Label(self.labelframe, text= " %")
        self.percente2.place(relx=0.85, rely=0.628, width=18, height=38)
        self.percente2.configure(background="#716cac")
        self.percente2.configure(foreground="#c0c0c0")
        self.percente2.configure(font="-family {Poppins ExtraBold} -size 13")

        self.button_suivant = Button(drop)
        self.button_suivant.place(relx=0.768, rely=0.69, width=76, height=23)
        self.button_suivant.configure(relief="flat")
        self.button_suivant.configure(overrelief="flat")
        self.button_suivant.configure(activebackground="#757198")
        self.button_suivant.configure(activeforeground="#ffffff")
        self.button_suivant.configure(cursor="hand2")
        self.button_suivant.configure(foreground="#716cac")
        self.button_suivant.configure(background="#ffffff")
        self.button_suivant.configure(font="-family {Poppins ExtraBold} -size 12")
        self.button_suivant.configure(borderwidth="0")
        self.button_suivant.configure(text="""Calculer""")
        self.button_suivant.configure(command=self.calculate)
    
    def calculate(self):
        p1 = 0.0225
        y = 0.00008
        L = float(lenght.get())
        phi = acos(float(cosPhi.get()))
        S = section_cuivre[0]
        
        i = 0
        if v1.get() =="3":
            b = 2
        else:
            b = 3
        if CheckVar1.get() == 0:
            voltage = float(selected_tension.get())
        elif CheckVar1.get() == 1:
            voltage =float( tension_perso.get())

        delta_V = b*(p1*(L/S)*cos(phi) + y*L*sin(phi))*courantCalculer

        if v0.get() =="1":
            drop_enable = float(indus_drop.get())*voltage
            p_drop = delta_V/voltage
            self.lab_result = Label(self.principal_frame, text= "La chute de tension correspondante\n a la section de {} mm est {} %".format(section_cuivre[0],f"{p_drop:.2f}"))
            self.lab_result.place(relx=0.0, rely=0.78, width=400, height=38)
            self.lab_result.configure(background="#716cac")
            self.lab_result.configure(foreground="#ffffff")
            self.lab_result.configure(font="-family {Poppins ExtraBold} -size 12")
            
            if drop_enable > delta_V:
                self.lab_result = Label(self.principal_frame, text= "La section minimale est {} mm".format(section_cuivre[0]))
                self.lab_result.place(relx=0.0, rely=0.9, width=400, height=38)
                self.lab_result.configure(background="#716cac")
                self.lab_result.configure(foreground="#ffffff")
                self.lab_result.configure(font="-family {Poppins ExtraBold} -size 12")
            elif drop_enable < delta_V:
                while drop_enable < delta_V:
                    i = i + 1
                    S = section_cuivre[i]
                    delta_V = b*(p1*(L/S)*cos(phi) + y*L*sin(phi))*courantCalculer
                    p_drop = delta_V/voltage

                self.lab_result = Label(self.principal_frame, text= "La section minimale est {} mm \navec une chute de tension {} %".format(section_cuivre[i],f"{p_drop:.2f}"))
                self.lab_result.place(relx=0.0, rely=0.9, width=400, height=38)
                self.lab_result.configure(background="#716cac")
                self.lab_result.configure(foreground="#ffffff")
                self.lab_result.configure(font="-family {Poppins ExtraBold} -size 12")

        elif v0.get() =="2":
            drop_enable = float(log_drop.get())*voltage
            p_drop = delta_V/voltage
            self.lab_result = Label(self.principal_frame, text= "La chute de tension correspondante\n a la section de {} mm est {} %".format(section_cuivre[0],f"{p_drop:.2f}"))
            self.lab_result.place(relx=0.0, rely=0.78, width=400, height=38)
            self.lab_result.configure(background="#716cac")
            self.lab_result.configure(foreground="#ffffff")
            self.lab_result.configure(font="-family {Poppins ExtraBold} -size 12")
            if drop_enable > delta_V:
                self.lab_result = Label(self.principal_frame, text= "La section minimale est {} mm".format(section_cuivre[0]))
                self.lab_result.place(relx=0.0, rely=0.9, width=400, height=38)
                self.lab_result.configure(background="#716cac")
                self.lab_result.configure(foreground="#ffffff")
                self.lab_result.configure(font="-family {Poppins ExtraBold} -size 12")
            elif drop_enable < delta_V:
                while drop_enable < delta_V:
                    i = i + 1
                    S = section_cuivre[i]
                    delta_V = b*(p1*(L/S)*cos(phi) + y*L*sin(phi))*courantCalculer
                    p_drop = delta_V/voltage

                self.lab_result = Label(self.principal_frame, text= "La section minimale est {} mm \navec une chute de tension {} %".format(section_cuivre[i],f"{p_drop:.2f}"))
                self.lab_result.place(relx=0.0, rely=0.9, width=400, height=38)
                self.lab_result.configure(background="#716cac")
                self.lab_result.configure(foreground="#ffffff")
                self.lab_result.configure(font="-family {Poppins ExtraBold} -size 12")
             

        else:
            drop_enable = float(person.get())*voltage 
            p_drop = delta_V/voltage
            self.lab_result = Label(self.principal_frame, text= "La chute de tension correspondante\n a la section de {} mm est {} %".format(section_cuivre[0],f"{p_drop:.2f}"))
            self.lab_result.place(relx=0.0, rely=0.78, width=400, height=38)
            self.lab_result.configure(background="#716cac")
            self.lab_result.configure(foreground="#ffffff")
            self.lab_result.configure(font="-family {Poppins ExtraBold} -size 12")
            if drop_enable > delta_V:
                self.lab_result = Label(self.principal_frame, text= "La section minimale est {} mm".format(section_cuivre[0]))
                self.lab_result.place(relx=0.0, rely=0.9, width=400, height=38)
                self.lab_result.configure(background="#716cac")
                self.lab_result.configure(foreground="#ffffff")
                self.lab_result.configure(font="-family {Poppins ExtraBold} -size 12")
            elif drop_enable < delta_V:
                while drop_enable < delta_V:
                    i = i + 1
                    S = section_cuivre[i]
                    delta_V = b*(p1*(L/S)*cos(phi) + y*L*sin(phi))*courantCalculer
                    p_drop = delta_V/voltage

                self.lab_result = Label(self.principal_frame, text= "La section minimale est {} mm \navec une chute de tension {} %".format(section_cuivre[i],f"{p_drop:.2f}"))
                self.lab_result.place(relx=0.0, rely=0.9, width=400, height=38)
                self.lab_result.configure(background="#716cac")
                self.lab_result.configure(foreground="#ffffff")
                self.lab_result.configure(font="-family {Poppins ExtraBold} -size 12")
    def disable_others(self):
        if v0.get() =="1":
            self.spin_box['state'] = 'disabled'
            self.log_drop_box['state'] = 'disabled'  
            self.indus_drop_box['state'] = 'readonly' 
        elif v0.get() =="2":
            self.spin_box['state'] = 'disabled'  
            self.indus_drop_box['state'] = 'disabled'  
            self.log_drop_box['state'] = 'readonly' 
        else:
            self.log_drop_box['state'] = 'disabled'  
            self.indus_drop_box['state'] = 'disabled'  
            self.spin_box['state'] = 'readonly' 

    def time(self):
        string = strftime("%H:%M:%S %p")
        self.clock.config(text=string)
        self.clock.after(1000, self.time)

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=root)
        if sure == True:
            root.destroy()

    def Logout(self):
        sure = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if sure == True:
            root.deiconify()
            page1.entry1.delete(0, END)
            page1.entry2.delete(0, END)
    
    
page1 = login_page(root)
root.bind("<Return>", login_page.login)
root.mainloop()