from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

import os

root = Tk()

# opening the GUI in minimzed mode

root.geometry("700x310")
# root.iconify()

root.title("KINESICS")
# root.iconbitmap("vsCode.ico")


# defining all METHODS
def myfunc():
    pass


def feedback_form():
    pass


def capture():
    os.startfile('capture.pyw')


# BUTTONS


f1 = Frame(root)

start_btn = Button(f1, text="START", font="comicsansms", padx="30")
start_btn.pack(side="left", padx="65", pady="20")


preview_btn = Button(f1, text="PREVIEW", command=capture,
                     font="comicsansms", padx="20")
preview_btn.pack(side="left")


btn = Button(f1, text="EXIT", command=root.quit, font="comicsansms", padx="30")
btn.pack(side="left", padx="65", pady="20")

f1.pack(pady=(50, 30))

f2 = Frame(root)

Button(f2, text="COMMANDS", font="comicsansms").pack(side="left",
                                                     padx="35", pady="20")
Button(f2, text="HELP", font="comicsansms", padx="30").pack(side="left",
                                                            padx="55", pady="30")

f2.pack()


root.mainloop()
