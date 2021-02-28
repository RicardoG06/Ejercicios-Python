from tkinter import *

#panel 
raiz=Tk()

#Frame
miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

#Cuadros de texto

minombre = StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)

cuadroapellido=Entry(miFrame)
cuadroapellido.grid(row=1,column=1,padx=10,pady=10)

cuadrodireccion=Entry(miFrame)
cuadrodireccion.grid(row=2,column=1,padx=10,pady=10)

cuadrocontraseña=Entry(miFrame)
cuadrocontraseña.grid(row=3,column=1,padx=10,pady=10)
cuadrocontraseña.config(show="*")

textocomentario=Text(miFrame, width=16,height=5)
textocomentario.grid(row=4,column=1,padx=10,pady=10)

#Barra de desplazamiento de un cuadro de texto
ScrollVert=Scrollbar(miFrame, command=textocomentario.yview)
ScrollVert.grid(row=4,column=2,sticky="nsew")
textocomentario.config(yscrollcommand=ScrollVert.set)

#Etiquetas
nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="w",padx=10,pady=10)

apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0,sticky="w",padx=10,pady=10)

direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2, column=0, sticky="w",padx=10,pady=10)

contraseñaLabel=Label(miFrame, text="Contraseña: ")
contraseñaLabel.grid(row=3, column=0, sticky="w",padx=10,pady=10)

comentarioLabel=Label(miFrame, text="Comentarios: ")
comentarioLabel.grid(row=4, column=0, sticky="w",padx=10,pady=10)

def codigoBoton():
    minombre.set("Ricardo")

#Boton
botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)
botonEnvio.pack()


raiz.mainloop()