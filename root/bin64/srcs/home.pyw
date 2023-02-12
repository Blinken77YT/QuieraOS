from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from lib.libs import echo
import os

cwd = os.getcwd()

def runterm():
    os.startfile(f"{cwd}\\term.py")

root = Tk()
root.geometry("500x400")
root.attributes("-fullscreen")
root.title("QuieraOS homescreen")

frame = ttk.Frame(root)
frame.pack(fill="both", expand=True)

style = ttk.Style()
style.configure("TButton")

image = Image.open(f"{cwd}\\img\\background.jpg")
image.resize((500, 400), Image.Resampling.LANCZOS)
background_image = ImageTk.PhotoImage(image)
image2 = Image.open(f"{cwd}\\img\\term.png")
image2.resize((128, 128), Image.Resampling.LANCZOS)
icon = ImageTk.PhotoImage(image2)

label = ttk.Label(frame, image=background_image)
label.pack(fill="both", expand=True)

button = Button(label, image=icon, relief="flat", width=64, height=64, command=runterm)
button.pack(side="bottom", anchor="s")

root.mainloop()
