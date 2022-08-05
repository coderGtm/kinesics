from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()

# opening the GUI in minimzed mode

root.geometry("%dx%d" % (root.winfo_screenwidth(),root.winfo_screenheight()))
root.iconify()

root.title("KINESICS")
# root.iconbitmap("vsCode.ico")


# defining all METHODS
def myfunc():
    pass


def feedback_form():
    pass


# creating MENU BAR
mainMenu = Menu(root, tearoff=0)

file_menu = Menu(mainMenu, tearoff=0)
command_menu = Menu(mainMenu, tearoff=0)
help_menu = Menu(mainMenu, tearoff=0)


command_menu.add_command(label="Status Bar")

help_menu.add_command(label="Send Feeback",command=feedback_form)
help_menu.add_separator()
help_menu.add_command(label="About Us")

mainMenu.add_cascade(label="File", menu=file_menu)
mainMenu.add_cascade(label="Commands", menu=command_menu)
mainMenu.add_cascade(label="Help", menu=help_menu)

root.config(menu=mainMenu)


# BUTTONS


f1 = Frame(root)

start_btn = Button(f1, text="START", font="comicsansms")
start_btn.pack(side="left", padx="65", pady="20")


f1.pack()

root.mainloop()
