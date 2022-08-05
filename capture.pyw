from tkinter import *
# from tkinter import messagebox
from PIL import Image, ImageTk
import cv2

root=Tk()
root.title('Kinesics')
root.state("zoomed")
root.configure(bg="#ebebeb")
label =Label(root,borderwidth=5,relief=SUNKEN)
label.grid(row=15, column=15,padx=450,pady=60)
cap= cv2.VideoCapture(0)
def show_frames():
   # Get the latest frame and convert into Image
   cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
   img = Image.fromarray(cv2image)
   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)
   # Repeat after an interval to capture continiously
   label.after(20, show_frames)
show_frames()
root.mainloop()

