
import tkinter as tk
from PIL import ImageTk, Image

# --- functions ---

text =  "nunca te rindas"
img = "Harry.jpeg"

def matus():

    matus = tk.Toplevel()

    image = Image.open("emma.jpeg")
    w, h = image.size
    
    imgrResized = image.resize((300,205), Image.ANTIALIAS)
    
    photo = ImageTk.PhotoImage(imgrResized)
    
    matus.photo = photo  # solution for bug in `PhotoImage`

    canvas = tk.Canvas(matus, width=w, height=h)
    canvas.pack()

    canvas.create_image(0, 0, anchor='nw', image=photo)

# --- main ---

root = tk.Tk()
root.geometry("640x320")
button = tk.Button(root, text='IMAGE', command=matus)
button.pack()

root.mainloop()