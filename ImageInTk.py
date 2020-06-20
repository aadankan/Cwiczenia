from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hi')
root.iconbitmap(r'C:\Users\aadan\Desktop\2.ico')

my_img = ImageTk.PhotoImage(Image.open(r'C:\Users\aadan\Desktop\1.png'))
myLabel = Label(image=my_img)
myLabel.pack()

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()
