from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Hi")
root.iconbitmap(r'C:\Users\aadan\Desktop\2.ico')

top = Toplevel()
label = Label(top, text="Hello World!").pack()




mainloop()
