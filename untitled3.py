#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter
from tkinter import *
from PIL import Image, ImageTk

from untitled2 import crearImg

test = crearImg()

ventana = Tk()

ventana.geometry("640x320")

label1 = tkinter.Label(ventana, image=test)
label1.image = test

# Position image
label1.place(x=100, y=100)

ventana.mainloop()