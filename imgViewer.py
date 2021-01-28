from tkinter import *
from PIL import ImageTk, Image

def openImg(image):
    root = Tk()
    img = ImageTk.PhotoImage(Image.open(image))
    panel = Label(root, image=img)
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()