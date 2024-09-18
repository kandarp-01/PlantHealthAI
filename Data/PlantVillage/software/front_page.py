from tkinter import *
import os
root=Tk()
root.title("PlantHealth")
root.geometry('1400x750')
Label(text="Welcome to PlantHealth AI ......",font=('arial',40,'bold'),bg="green").place(x=100,y=100)
root.config(bg="#EABFB9")
def open():
    root.destroy()
    os.system("software\\browse.py")
Button(text='Start',command=open).place(x=100,y=300)
root.mainloop()
