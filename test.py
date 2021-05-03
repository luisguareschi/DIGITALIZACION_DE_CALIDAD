import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Cursor
from POINT import Point
from PART import Part
import tkinter as tk
from tkinter import ttk, font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Start TKinter
start_screen = tk.Tk()
# Create a style
# style = ttk.Style(start_screen)
# start_screen.tk.call('source', 'azure-dark.tcl')
# style.theme_use('azure-dark')

# Screen settings
windowWidth = 300
windowHeight = 200
screenWidth = start_screen.winfo_screenwidth()
screenHeight = start_screen.winfo_screenheight()
xCordinate = int((screenWidth / 2) - (windowWidth / 2))
yCordinate = int((screenHeight / 2) - (windowHeight / 2))
start_screen.geometry("{}x{}+{}+{}".format(windowWidth, windowHeight, xCordinate, yCordinate))
start_screen.config(bg='grey')

# Creating a Font object of "TkDefaultFont"
defaultFont = font.nametofont("TkDefaultFont")

# Overriding default-font with custom settings
# i.e changing font-family, size and weight
defaultFont.configure(family=None,
                           size=12,
                           weight=font.NORMAL)

# Main Menu Window
frame = tk.LabelFrame(start_screen, text='Tipo de avion', bg='grey')
frame.pack(fill='both', expand=True, padx=15, pady=15)
for i in range(0, 2):
    frame.columnconfigure(i, weight=1)
for i in range(0, 2):
    frame.rowconfigure(i, weight=1)
img = tk.PhotoImage(file='azure-dark/button-hover.png')
label1 = tk.Label(frame, text='\nSelecciona el tipo de avion:', bg='grey')
label1.grid(row=0, column=0, columnspan=2, padx=10)
button1 = tk.Button(frame, text='v900', image=img, compound='center', bg='grey', border=0)
button1.grid(row=1, column=0)
button2 = tk.Button(frame, text='v1000')
button2.grid(row=1, column=1, ipady=0, padx=0)

start_screen.mainloop()