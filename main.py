from tkinter import *
from tkinter import dialog
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tk()

# opening the GUI in maximized mode

root.state("zoomed")

root.title("Team : PYRAMID")
root.iconbitmap("gesture.jpg")


# defining all METHODS
def myfunc():
    pass


def open_image():
    global gesture_image
    global gesture_label

    filename = filedialog.askopenfilename(initialdir="vsCode.ico",
                                          title="Select a File :", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    gesture_photo = Image.open(filename)
    # tuple of width, height
    resized_gesture_photo = gesture_photo.resize((500, 500))
    gesture_image = ImageTk.PhotoImage(resized_gesture_photo)
    gesture_label = Label(open_frame, image=gesture_image)
    gesture_label.pack(pady="50")


def delete_img():
    gesture_label.pack_forget()


def modify_img():
    delete_img()
    open_image()


# creating MENU BAR
mainMenu = Menu(root, tearoff=0)

file_menu = Menu(mainMenu, tearoff=0)
edit_menu = Menu(mainMenu, tearoff=0)
format_menu = Menu(mainMenu, tearoff=0)
view_menu = Menu(mainMenu, tearoff=0)
help_menu = Menu(mainMenu, tearoff=0)

file_menu.add_command(label="New")
file_menu.add_command(label="New Window")
file_menu.add_command(label="Open...")
file_menu.add_command(label="Save")
file_menu.add_command(label="SaveAs...")
file_menu.add_separator()
file_menu.add_command(label="Page Setup...")
file_menu.add_command(label="Print...")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu.add_command(label="Undo")
edit_menu.add_separator()
edit_menu.add_command(label="Cut", state="disabled")
edit_menu.add_command(label="Copy", state="disabled")
edit_menu.add_command(label="Paste", state="disabled")
edit_menu.add_command(label="Delete", state="disabled")
edit_menu.add_separator()
edit_menu.add_command(label="Search with Bing...")
edit_menu.add_command(label="Find...")
edit_menu.add_command(label="Find Next")
edit_menu.add_command(label="Find Previous")
edit_menu.add_command(label="Replace...", state="disabled")
edit_menu.add_command(label="Go To...")
edit_menu.add_separator()
edit_menu.add_command(label="Select All")
edit_menu.add_command(label="Time/Date")

format_menu.add_command(label="Word Wrap")
format_menu.add_command(label="Font...")

Zoom_view_menu = Menu(view_menu, tearoff=0)
Zoom_view_menu.add_command(label="Zoom In")
Zoom_view_menu.add_command(label="Zoom Out")
Zoom_view_menu.add_command(label="Restore Default Zoom")

view_menu.add_cascade(label="Zoom", menu=Zoom_view_menu)
# view_menu.add_command("Zoom")
view_menu.add_command(label="Status Bar")

help_menu.add_command(label="View Help")
help_menu.add_command(label="Send Feeback")
help_menu.add_separator()
help_menu.add_command(label="About Us")

mainMenu.add_cascade(label="File", menu=file_menu)
mainMenu.add_cascade(label="View", menu=edit_menu)
mainMenu.add_cascade(label="Menu", menu=format_menu)
mainMenu.add_cascade(label="Command", menu=view_menu)
mainMenu.add_cascade(label="Help", menu=help_menu)

root.config(menu=mainMenu)


# PREVIEW FRAME

# TODO: resizer of the image dynamically


open_frame = Frame(root)

Button(open_frame, text="Open Image File", command=open_image).pack()

open_frame.pack()

# BUTTONS


f1 = Frame(root)

bt1_ADD = Button(f1, text="ADD", font="comicsansms", command=open_image)
bt1_ADD.pack(side="left", padx="65", pady="20")
bt2_DELETE = Button(f1, text="DELETE", font="comicsansms", command=delete_img)
bt2_DELETE.pack(padx="0", pady="20")

f1.pack()

f2 = Frame(root)

bt3_MODIFY = Button(f2, text="MODIFY", font="comicsansms",
                    command=modify_img)
bt3_MODIFY.pack(side="left", padx="30", pady="20")
bt4_EXIT = Button(f2, text="EXIT", font="comicsansms", command=root.quit)
bt4_EXIT.pack(side="left", padx="35", pady="20")

f2.pack()


# STATUS BAR
# TODO: status Bar showing the connected/disconnected status

# SCROLL BAR
# TODO: horizontal scroll bar

root.mainloop()
