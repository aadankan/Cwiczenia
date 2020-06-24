from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('message')
root.iconbitmap(r'C:\Users\aadan\Desktop\2.ico')


def popup():
    messagebox.showinfo('Popup', 'Hello world!')


Button(root, text='Popup', command=popup).pack()


mainloop()
