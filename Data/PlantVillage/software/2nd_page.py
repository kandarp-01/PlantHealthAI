from tkinter import *
root=Tk()
root.title("PlantHealth")
root.geometry('1400x750')
Label(text="Provide Details",font=('arial',40,'bold'),bg="green").place(x=100,y=100)
root.config(bg="Black")
Button(text="Preview")
Button(text="View Result")
Button(text="Download")
def testing():
    l=e1.get()
    b1.destroy()
    Label(root,text=l).place(x=400,y=400)
e1=Entry(root)
e1.place(x=500,y=500)
b1=Button(text="Browse Image",command=testing)
b1.place(x=300,y=400)
root.mainloop()

