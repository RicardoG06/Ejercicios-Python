import tkinter as tk

root=tk.Tk()

miFrame=tk.Frame(root, width= 500 ,height= 400 )
miFrame.pack()

miImagen=tk.PhotoImage(file='C:/Users/ricar/ProyectosPython/Curso Python Ejercicios/baile.gif')

#miLabel=tk.Label(miFrame, text="Hola alumnos de Python", fg="red",
#font=("Comic Sans MS",18))

miLabel=tk.Label(miFrame, image=miImagen)

miLabel.place(x=100,y=200)

root.mainloop()
