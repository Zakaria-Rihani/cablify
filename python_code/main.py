import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

main = Tk()
main.geometry("1340x699+5+0")
main.title("Cable Section")
main.resizable(0, 0)

def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()
        
main.protocol("WM_DELETE_WINDOW", Exit)

def login():
    main.withdraw()
    os.system("python C:/Users/ASUS/Desktop/PFA/python_code/login.py")
    main.deiconify()

def signup():
    main.withdraw()
    os.system("python C:/Users/ASUS/Desktop/PFA/python_code/signup.py")
    main.deiconify()

label1 = Label(main)
label1.place(relx=0, rely=0, width=1340, height=699)
img = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/main1.png")
label1.configure(image=img)

button1 = Button(main)
button1.place(relx=0.583, rely=0.425, width=230, height=37)
button1.configure(relief="flat")
button1.configure(overrelief="flat")
button1.configure(activebackground="#ffffff")
button1.configure(cursor="hand2")
button1.configure(foreground="#ffffff")
button1.configure(background="#ffffff")
button1.configure(borderwidth="0")
img2 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/img4.png")
button1.configure(image=img2)
button1.configure(command=login)

button2 = Button(main)
button2.place(relx=0.583, rely=0.539, width=230, height=37)
button2.configure(relief="flat")
button2.configure(overrelief="flat")
button2.configure(activebackground="#ffffff")
button2.configure(cursor="hand2")
button2.configure(foreground="#ffffff")
button2.configure(background="#ffffff")
button2.configure(borderwidth="0")
img3 = PhotoImage(file="C:/Users/ASUS/Desktop/PFA/images/img5.png")
button2.configure(image=img3)
button2.configure(command=signup)

main.mainloop()