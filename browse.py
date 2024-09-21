import os
from tkinter import *
from PIL import Image
from PIL import ImageTk

root=Tk()
def goback():
    root.destroy()
    os.system("Home.py")

def view_result():
    pass
def download_result():
    pass
def add_image():
    os.system("pick.py")
root.title("PlantHealth")
root.geometry("1910x1070")

frame=Frame(root,width=1200, height=550, bg="#E7F0DC")
frame.place(relx=0.5,rely=0.5, anchor="center")

Label(text="Provide Details",bg="grey",font=('arial',40,'bold')).place(x=550,y=105)
b=Button(text="⇦ Back",border=8, width=8, height=2, command=goback).place(x=5,y=5)


search=Image.open("image-search.png")
search=search.resize((205,200))
sr=ImageTk.PhotoImage(search)

b1=Button(image=sr,bg="#E7F0DC",border=2,command=add_image)
Label(text="Browse Image",width=29).place(x=500,y=437)

b2=Button(text="Preview",width=15,height=4)
b3=Button(text="Submit",width=15,height=4)
b1.place(x=500,y=250)
b2.place(x=900,y=300)
b3.place(x=730,y=600)
root.config(bg="#37B7C3")
root.mainloop()

