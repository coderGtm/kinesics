from tkinter import *
from PIL import Image, ImageTk
import cv2
import os

root = Tk()
root.title('Kinesics')
root.state("zoomed")
root.configure(bg="#ebebeb")


def capture():
    os.startfile('capture.pyw')


btn = Button(root, text="PREVIEW", command=capture)
btn.pack(pady=10)

root.mainloop()
