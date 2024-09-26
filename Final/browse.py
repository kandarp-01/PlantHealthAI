import os
image_detail=None
from tkinter import *
from PIL import Image
from PIL import ImageTk
from datetime import datetime
from tkinter import filedialog, Label, Entry, Button
root=Tk()
#Functon for opening home page
def goback():
    root.destroy()
    os.system("Home.py")

#Function for opening result page
def view_result():
    root.destroy()
    os.system("result.py")

#function for browsing image
def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", ".jpg;.jpeg;.png;.bmp")]) 
    global image_detail
    image_detail=file_path
    if(len(image_detail)):
        b2.config(state=NORMAL)

#function for previewing image
def preview_image():
    def change():
        global image_detail
        image_detail=None # Making image path none to removing the  selected image
        b2.config(state=DISABLED)
        frame1.destroy()
    #Frame for showing selected image
    frame1=Frame(bg="#f0eeb7",width=800,height=400)
    frame1.place(x=360,y=200)
    img1=Image.open(image_detail)
    img1=img1.resize((600,300))
    im=ImageTk.PhotoImage(img1)
    l2=Label(frame1)
    l2.config(image=im)
    l2.image=im
    l2.place(x=100,y=40)
    b7=Button(frame1,text="Submit",width=10,height=2,command=view_result)
    b8=Button(frame1,text="Change",width=10,height=2,command=change)
    b7.place(x=460,y=360)
    b8.place(x=580,y=360)


root.title("PlantHealth")
root.geometry("1910x1070")

frame=Frame(root,width=1200, height=550, bg="#E7F0DC")
frame.place(relx=0.5,rely=0.5, anchor="center")

Label(text="Provide Details",bg="grey",font=('arial',40,'bold')).place(x=550,y=105)
b=Button(text="⇦ Back",border=8, width=8, height=2, command=goback).place(x=5,y=5)

#Selecting Browse Icon
search=Image.open("images\\image-search.png")
search=search.resize((205,200))
sr=ImageTk.PhotoImage(search)
#Selecting Preview Icon
preview=Image.open("images\\preview1.png")
preview=preview.resize((205,200))
pr=ImageTk.PhotoImage(preview)
#Submit Button
b1=Button(image=sr,bg="#73c991",border=2,command=open_image)
Label(text="Browse Image",width=29).place(x=500,y=437)
#Preview Button 
b2=Button(image=pr,bg="#73c991",border=2,command=preview_image)
b2.config(state=DISABLED)
Label(text="Preview Image",width=29).place(x=900,y=437)
b1.place(x=500,y=250)
b2.place(x=900,y=250)
root.config(bg="#37B7C3")
root.mainloop()

