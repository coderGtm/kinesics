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

# label.grid(row=15, column=15,padx=450,pady=60)
# cap= cv2.VideoCapture(0)

# # Define function to show frame
# def show_frames():
#    # Get the latest frame and convert into Image
#    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
#    img = Image.fromarray(cv2image)
#    # Convert image to PhotoImage
#    imgtk = ImageTk.PhotoImage(image = img)
#    label.imgtk = imgtk
#    label.configure(image=imgtk)
#    # Repeat after an interval to capture continiously
#    label.after(20, show_frames)

# # f1 = Frame(root)
# start_btn = Button(root, text="PREVIEW", font="comicsansms",command=show_frames)
# start_btn.pack(side="left", padx="65", pady="20")


# # f1.pack()


# def about():
#     messagebox.showinfo('Kinesics Gesture Recognition', 'Click to download the file')

# menubar = Menu(root, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
# file = Menu(menubar, tearoff=1, background='#ffcc99', foreground='black')
# file.add_command(label="New")
# file.add_command(label="Open")
# file.add_command(label="Save")
# file.add_command(label="Save as")
# file.add_separator()
# file.add_command(label="Exit", command=root.quit)
# menubar.add_cascade(label="File", menu=file)

# edit = Menu(menubar, tearoff=0)
# edit.add_command(label="Undo")
# edit.add_separator()
# edit.add_command(label="Cut")
# edit.add_command(label="Copy")
# edit.add_command(label="Paste")
# menubar.add_cascade(label="Edit", menu=edit)

# help = Menu(menubar, tearoff=0)
# help.add_command(label="About", command=about)
# menubar.add_cascade(label="Help", menu=help)

# root.config(menu=menubar)
