from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("checkboxes")
root.iconbitmap(r'C:\Users\aadan\Desktop\2.ico')
root.geometry("400x400")



def show():
    mylabel = Label(root, text=clicked.get()).pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

my_button = Button(root, text="Show Selection", command=show).pack()


mainloop()
