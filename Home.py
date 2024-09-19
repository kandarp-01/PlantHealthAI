from tkinter import *
from PIL import Image
from PIL import ImageTk

import os
import matplotlib

root=Tk()
root.title("PlantHealthAI")
root.geometry("1910x1070")
root.config(bg="#37B7C3")
frame=Frame(root,width=1200, height=550, bg="#E7F0DC")
frame.place(relx=0.5,rely=0.5, anchor="center")

image=Image.open("software\p.jpg")
image=image.resize((500,300))

img=ImageTk.PhotoImage(image)
Label(root,image=img,border=10,bg="#37B7C3").place(relx=0.5,rely=0.5,anchor="center")

Label(text="Welcome to PlantHealth AI ......",font=('arial',40,'bold')).place(x=377, y=170)

Label(text="Diagnose your Plant", font=('arial',20),bg="#37B7C3").place(x=570,y=650)
Label(text="➥", font=('arial',20), bg="#E7F0DC").place(x=830,y=650)
def open():
    root.destroy()
    os.system("browse.py")

login=Image.open("image.png")
login=login.resize((70,50))
log=ImageTk.PhotoImage(login)
b1=Button(image=log,bg="#c7defa", borderwidth=0,command=open).place(x=880,y=642)

root.mainloop()

