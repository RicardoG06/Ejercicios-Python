import tkinter as tk
from tkinter import *

raiz=tk.Tk()

miFrame=tk.Frame(raiz,width=1200,height=600)
miFrame.pack()

cuadrotexto=tk.Entry(miFrame)
cuadrotexto=grid(row=0, column=1)

nombrelabel=tk.Label(miFrame, text="Nombre:")
nombrelabel=grid(row=0, column=0)

raiz.mainloop()