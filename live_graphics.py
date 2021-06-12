#  Made by @Saksham Solanki, Date: 26/05/2021 (DD/MM/YYYY) Time: 23:44 (24-hour-format)
import tkinter as tk
import random

x = 0.0
y = 0.0
x2 = 0.0
y2 = 0.0
apls = ['A','B','C','D','E','F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
choice = 1
def display():
    global x
    global x2
    global choice
    global apls
    global y
    global y2
    x += 0.05
    y += 0.1
    if x > 0.95:
        x = -0.99
    frame.place(relx=0.1,rely=x)
    if choice == 1:
        tk.Label(frame, text=str(random.choice(apls)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)
        choice = 2
    elif choice == 2:
        tk.Label(frame, text=str(random.randint(0,9)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)     
        choice = 1

    x2 -= 0.05
    y2 += 0.1
    if x2 < -0.99:
        x2 = 0.99
    frame2.place(relx=0.2,rely=x2)
    if choice == 1:
        tk.Label(frame2, text=str(random.choice(apls)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y2)
        choice = 2
    elif choice == 2:
        tk.Label(frame2, text=str(random.randint(0,9)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y2)     
        choice = 1

    frame3.place(relx=0.3,rely=x)
    if choice == 1:
        tk.Label(frame3, text=str(random.choice(apls)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)
        choice = 2
    elif choice == 2:
        tk.Label(frame3, text=str(random.randint(0,9)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)     
        choice = 1

    frame4.place(relx=0.4,rely=x2)
    if choice == 1:
        tk.Label(frame4, text=str(random.choice(apls)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y2)
        choice = 2
    elif choice == 2:
        tk.Label(frame4, text=str(random.randint(0,9)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y2)     
        choice = 1

    frame5.place(relx=0.5,rely=x)
    if choice == 1:
        tk.Label(frame5, text=str(random.choice(apls)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)
        choice = 2
    elif choice == 2:
        tk.Label(frame5, text=str(random.randint(0,9)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)     
        choice = 1

    frame6.place(relx=0.6,rely=x2)
    if choice == 1:
        tk.Label(frame6, text=str(random.choice(apls)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y2)
        choice = 2
    elif choice == 2:
        tk.Label(frame6, text=str(random.randint(0,9)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y2)     
        choice = 1

    frame7.place(relx=0.7,rely=x)
    if choice == 1:
        tk.Label(frame7, text=str(random.choice(apls)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)
        choice = 2
    elif choice == 2:
        tk.Label(frame7, text=str(random.randint(0,9)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)     
        choice = 1

    frame8.place(relx=0.8,rely=x2)
    if choice == 1:
        tk.Label(frame8, text=str(random.choice(apls)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y2)
        choice = 2
    elif choice == 2:
        tk.Label(frame8, text=str(random.randint(0,9)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y2)     
        choice = 1

    frame9.place(relx=0.9,rely=x)
    if choice == 1:
        tk.Label(frame9, text=str(random.choice(apls)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)
        choice = 2
    elif choice == 2:
        tk.Label(frame9, text=str(random.randint(0,9)), bg="black", fg="SpringGreen3").place(relx=0.0,rely=y)     
        choice = 1
    window.after(20,display)
window = tk.Tk()
window.geometry("500x300")
window.config(bg="black")
frame = tk.Frame(window, height=300, width=15, bg="black")
frame.place(relx=0.1, rely=0.0)
frame2 = tk.Frame(window, height=300, width=15, bg="black")
frame2.place(relx=0.2, rely=0.999)

frame3 = tk.Frame(window, height=300, width=15, bg="black")
frame3.place(relx=0.3, rely=0.0)
frame4 = tk.Frame(window, height=300, width=15, bg="black")
frame4.place(relx=0.4, rely=0.999)

frame5 = tk.Frame(window, height=300, width=15, bg="black")
frame5.place(relx=0.5, rely=0.0)
frame6 = tk.Frame(window, height=300, width=15, bg="black")
frame6.place(relx=0.6, rely=0.999)

frame7 = tk.Frame(window, height=300, width=15, bg="black")
frame7.place(relx=0.7, rely=0.0)
frame8 = tk.Frame(window, height=300, width=15, bg="black")
frame8.place(relx=0.8, rely=0.999)
frame9 = tk.Frame(window, height=300, width=15, bg="black")
frame9.place(relx=0.9, rely=0.0)
window.after(20, display)
window.mainloop()
