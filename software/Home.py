from tkinter import *
import os
from PIL import *
image=open("p.jpg")
root=Tk()
root.title("PlantHealthAI")
root.geometry("1910x1070")
root.config(bg="#37B7C3")
img=PhotoImage(image)
frame=Frame(root, width=1200, height=550, bg="#E7F0DC",image=img)
frame.place(relx=0.5,rely=0.5, anchor="center")

Label(text="Welcome to PlantHealth AI ......",font=('arial',40,'bold')).place(x=377, y=170)

def open():
    root.destroy()
    os.system("software\\2nd_page.py")
Button(text='Start',command=open).place(x=100,y=300)

root.mainloop()
