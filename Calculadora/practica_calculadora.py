from tkinter import *


raiz=Tk()

miFrame=Frame()

miFrame.pack()

operacion=""

cont_resta=0

cont_mult=0

cont_div=0

resultado=0

reset = 0 

cont_coma = 1

#----------Pantalla------------

numeroPantalla=StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=5,pady=5, columnspan=4)
pantalla.config(background="black", fg="#03f943",justify="right")

#----------------Pulsaciones teclado--------------------

def numeroPulsado(num):
    global operacion
    global reset 
    global cont_coma

    if reset!=0:
        numeroPantalla.set(num)
        reset=0

    else:
        if num != "." :
            numeroPantalla.set(numeroPantalla.get() + num)
                                     
        else:
            if cont_coma == 1: 
                numeroPantalla.set(numeroPantalla.get() + num)
            cont_coma = 0
        
#----------------funcion suma--------------------

def suma(num):

    global operacion
    global resultado
    global reset
    global cont_coma
    
    resultado+=float(num)
    operacion="suma"
    reset = 1
    cont_coma = 1
    numeroPantalla.set(resultado)
   

#----------------funcion resta--------------------

def resta(num):

    global operacion
    global resultado
    global cont_resta
    global reset
    global cont_coma
    
    if cont_resta == 0:  
        resultado = float(num)
    else:
        if cont_resta == 1:
            resultado -= float(num)

    cont_resta = 1
    operacion="resta"
    reset = 1
    cont_coma = 1
    numeroPantalla.set(resultado)

#----------------funcion multiplicacion--------------------
def multiplicacion(num): 

    global operacion
    global resultado
    global reset
    global cont_mult
    global cont_coma
    
    if cont_mult == 0:  
        resultado = float(num)
    else:
        if cont_mult == 1:
            resultado *= float(num)

    cont_mult = 1
    operacion="multiplicacion"
    reset = 1
    cont_coma = 1
    numeroPantalla.set(resultado)

#----------------funcion division--------------------
    
def division(num):

    global operacion
    global resultado
    global reset
    global cont_div
    global cont_coma
    
    if cont_div == 0:  
        resultado = float(num)
    else:
        if cont_div == 1:
            resultado /= float(num)

    cont_div = 1
    operacion ="division"
    reset = 1
    cont_coma = 1
    numeroPantalla.set(resultado)
   

#--------------funcion el_resultado----------------

def el_resultado():
    global resultado
    global operacion
    global cont_resta
    global cont_mult
    global cont_coma

    if operacion == "suma":
        numeroPantalla.set(resultado + float(numeroPantalla.get()))
        resultado=0
        cont_coma = 1
    elif operacion == "resta":
        numeroPantalla.set(resultado - float(numeroPantalla.get()))
        resultado=0
        cont_resta=0
        cont_coma = 1
    
    elif operacion == "multiplicacion":
        numeroPantalla.set(resultado * float(numeroPantalla.get()))
        resultado=0
        cont_mult=0
        cont_coma = 1

    elif operacion == "division":
        numeroPantalla.set(resultado / float(numeroPantalla.get()))
        resultado=0
        cont_div=0
        cont_coma = 1
        
    
   


#---------Fila 1---------------

Button7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
Button7.grid(row=2, column=1)
Button8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
Button8.grid(row=2, column=2)
Button9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
Button9.grid(row=2, column=3)
ButtonDiv=Button(miFrame, text="/", width=3, command=lambda:division(numeroPantalla.get()))
ButtonDiv.grid(row=2, column=4)

#---------Fila 2-----------------

Button4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
Button4.grid(row=3, column=1)
Button5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
Button5.grid(row=3, column=2)
Button6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
Button6.grid(row=3, column=3)
ButtonMult=Button(miFrame, text="X", width=3, command=lambda:multiplicacion(numeroPantalla.get()))
ButtonMult.grid(row=3, column=4)

#---------Fila 3-----------------

Button1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
Button1.grid(row=4, column=1)
Button2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
Button2.grid(row=4, column=2)
Button3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
Button3.grid(row=4, column=3)
ButtonResta=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
ButtonResta.grid(row=4, column=4)

#---------Fila 4-----------------

Button0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
Button0.grid(row=5, column=1)
ButtonComa=Button(miFrame, text=".", width=3, command=lambda:numeroPulsado("."))
ButtonComa.grid(row=5, column=2)
ButtonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
ButtonIgual.grid(row=5, column=3)
ButtonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
ButtonSuma.grid(row=5, column=4)











raiz.mainloop()