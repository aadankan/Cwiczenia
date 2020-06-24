from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()
root.title("Hi")
root.iconbitmap(r'C:\Users\aadan\Desktop\2.ico')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="gui/images", title="select File", filetypes=(("Png Files", "*.png"), ("All Files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()


mainloop()
