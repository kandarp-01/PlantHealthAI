from tkinter import *
def choose():
    pass
root=Tk()
root.geometry(("1400x800"))
frame1=Frame(root,width=1200,height=600)
frame1.config(bg="white")
l1=Label(frame1,text="View Your Result",bg="white",font=("Arial",40),fg="black")
b1=Button(text="Show Result",command=choose,width=15,height=4)
frame1.place(relx=0.5,rely=0.5,anchor=CENTER)
b1.place(x=700,y=500)
l1.place(x=400,y=40)
root.config(bg="#16423C")
root.mainloop()