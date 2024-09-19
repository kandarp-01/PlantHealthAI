import os
from tkinter import *
root=Tk()
def view_result():
    pass
def download_result():
    pass
def add_image():
    os.system("software\\pick.py")
root.title("PlantHealth")
root.geometry('1400x750')
Label(text="Provide Details",font=('arial',40,'bold'),bg="green").place(x=550,y=100)
b1=Button(text="Browse Image",width=15,height=4,command=add_image)
b2=Button(text="Preview",width=15,height=4)
b3=Button(text="Submit",width=15,height=4)
b1.place(x=400,y=300)
b2.place(x=900,y=300)
b3.place(x=650,y=500)
root.config(bg="Black")
root.mainloop()

