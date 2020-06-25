from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("checkboxes")
root.iconbitmap(r'C:\Users\aadan\Desktop\2.ico')
root.geometry("400x400")

def show():
    mylabel = Label(root, text=var.get()).pack()


var = IntVar()

c = Checkbutton(root, text="You can check this box", variable=var)
c.pack()

mybutton = Button(root, text="Show Selection", command=show).pack()


mainloop()
