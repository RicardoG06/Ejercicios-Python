import tkinter as tk

root = tk.Tk()

root.title("Ventana de pruebas")

#root.geometry("650x350")

root.config(bg="blue")

miFrame=tk.Frame()

#miFrame.pack(fill="both",expand="True")

miFrame.pack()

miFrame.config(bg="red")

miFrame.config(width="650",height="350")

miFrame.config(bd=35)

miFrame.config(relief="groove")

miFrame.config(cursor="pirate")


root.mainloop() 