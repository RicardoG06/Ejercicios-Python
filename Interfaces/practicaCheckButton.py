from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
TurismoRural=IntVar()

def opcionesViaje():
    opcionEscogida=""
    if(playa.get()==1):
        opcionEscogida+=" playa"
    if(montagna.get()==1):
        opcionEscogida+=" montaña"
    if(TurismoRural.get()==1):
        opcionEscogida+=" turismoRural"
    
    textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file='C:/Users/ricar/ProyectosPython/Curso Python Ejercicios/baile.gif')
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos:", width=50).pack()

Checkbutton(frame, text="Playa",variable=playa,onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña",variable=montagna,onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo Rural",variable=TurismoRural,onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()