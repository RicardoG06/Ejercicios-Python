from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import re
#lista
listanueva = []

#panel 
root=Tk()
#Funciones

class Analizador():
    def __init__(self):
        self.lista = []

    def abrirArchivo(self):
        archivo = filedialog.askopenfilename(title="Abrir Archivo")
        if archivo != '':
            archi1 = open(archivo, 'r')       
            contenido = archi1.read()
            self.lista = [linea.strip() for linea in contenido]
            archi1.close()
            insertarCuadroTexto(contenido)
    
    def analizadorS(self):
        self.lista.append('$')

        Qf = 100
        Qe = -1
        Qg = -2
        k=0
        p=0
        q=0
        contadorL=0
        linea=1
        con=0
        aim = 0
        aim1=0
        ent=0
        tex = 0
        texto=""
        
        #while(con < len(self.lista)):
        #    if(self.lista[con] == '$'):
        #        contadorL = contadorL + 1
        #    con = con + 1
        if self.lista[0] == '':
            p = p + 1 

        
        while ( q != Qf and q!= Qe):
            if q == 0:
                if ((self.lista[p] == 'i' or self.lista[p] == 'I')  and self.lista[p + 1] == 'n' and self.lista[p + 2] == 't')  or ((self.lista[p] == 'f' or self.lista[p] == 'F') and self.lista[p + 1] == 'l' and self.lista[p + 2] == 'o' and self.lista[p + 3] == 'a' and self.lista[p + 4] == 't'):
                    q = 1
                else:
                    q = Qe
                    texto = "\nError en la linea " + str(linea) + ". La asignacion deberia comenzar por int o float para continuar.  "
                    if tex == 0:
                        textocomentario2.delete("1.0",END)
                        textocomentario2.insert("1.0",texto)
                    else:
                        textocomentario2.insert("1.0",texto)
                    
            elif q == 1:
                
                if ((self.lista[p] == 'i' or self.lista[p] == 'I')  and self.lista[p + 1] == 'n' and self.lista[p + 2] == 't'):
                    if (self.lista[p + 3] == ''):
                        while (self.lista[p + 3] == ''):
                            p = p + 1
                        if (self.lista[p + 3] != '$'):
                            
                            if re.findall('[a-zA-Z]', self.lista[p + 3]):
                                p = p + 1
                                while(self.lista[p + 3] != '$' and aim == 0):
                                    if (self.lista[p + 3] == '' or self.lista[p + 3] == ';' or self.lista[p + 3] == ',' or self.lista[p + 3] == '=' ):
                                        q = 2 
                                        aim = 1
                                        ent=0
                                    elif (self.lista[p + 3] != '$'):
                                        p = p + 1
                            else:
                                texto = "\nError en la linea "+str(linea)+ ". Debe escribir un nombre de variable que no comience en numero o signo. "
                                if tex == 0:
                                    textocomentario2.delete("1.0",END)
                                    textocomentario2.insert("1.0",texto)
                                else:
                                    textocomentario2.insert("1.0",texto)
                                q = Qe
                        else:
                            texto = "\nError en la linea "+str(linea)+ ". No se ha asignado una variable al tipo de dato. "
                            if tex == 0:
                                textocomentario2.delete("1.0",END)
                                textocomentario2.insert("1.0",texto)
                            else:
                                textocomentario2.insert("1.0",texto)
                            q = Qe
                        
                    else:
                        texto = "\nError en la linea "+str(linea)+". Debe haber un espacio entre la asignacion de tipo con el nombre de la variable.  "
                        if tex == 0:
                            textocomentario2.delete("1.0",END)
                            textocomentario2.insert("1.0",texto)
                        else:
                            textocomentario2.insert("1.0",texto)
                        q = Qe

                elif ((self.lista[p] == 'f' or self.lista[p] == 'F') and self.lista[p + 1] == 'l' and self.lista[p + 2] == 'o' and self.lista[p + 3] == 'a' and self.lista[p + 4] == 't'):
                    if (self.lista[p + 5] == ''):
                        while (self.lista[p + 5] == ''):
                            p = p + 1
                        if (self.lista[p + 5] != '$'):
                            
                            if re.findall('[a-zA-Z]', self.lista[p + 5]):
                                p = p + 1
                                while(self.lista[p + 5] != '$' and aim1 == 0):
                                    if (self.lista[p + 5] == '' or self.lista[p + 5] == ';' or self.lista[p + 5] == ',' or self.lista[p + 5] == '=' ):
                                        q = 2 
                                        aim1 = 1
                                        ent=1
                                    elif (self.lista[p + 5] != '$'):
                                        p = p + 1
                            else:
                                texto = "\nError en la linea "+str(linea)+ ". Debe escribir un nombre de variable que no comience en numero o signo. "
                                q = Qe
                                if tex == 0:
                                    textocomentario2.delete("1.0",END)
                                    textocomentario2.insert("1.0",texto)
                                else:
                                    textocomentario2.insert("1.0",texto)
                        else:
                            texto = "\nError en la linea "+str(linea)+ ". No se ha asignado una variable al tipo de dato. "
                            q = Qe
                            if tex == 0:
                                textocomentario2.delete("1.0",END)
                                textocomentario2.insert("1.0",texto)
                            else:
                                textocomentario2.insert("1.0",texto)
                        
                    else:
                        texto = "\nError en la linea "+str(linea)+". Debe haber un espacio entre la asignacion de tipo con el nombre de la variable.  "
                        q = Qe
                        if tex == 0:
                            textocomentario2.delete("1.0",END)
                            textocomentario2.insert("1.0",texto)
                        else:
                            textocomentario2.insert("1.0",texto)


            elif q ==2:
                if ent==0:
                    while (self.lista[p + 3] == ''):
                        p = p + 1
                    if (self.lista[p + 3] == ';'):
                        q = 3
                    elif (self.lista[p + 3] == ','):
                        q = 1
                        p = p + 4
                    elif (self.lista[p + 3] == '='):
                        q = 4
                        p  = p + 1
                    else:
                        q = Qe
                        texto = "\nError en la linea "+ str(linea) +". No esta bien colocada la estructura . Luego de una variable pueden seguir los signos ';' , ',' o '=' para continuar. "
                        if tex == 0:
                            textocomentario2.delete("1.0",END)
                            textocomentario2.insert("1.0",texto)
                        else:
                            textocomentario2.insert("1.0",texto)
                if ent==1:
                    while (self.lista[p + 5] == ''):
                        p = p + 1
                    if (self.lista[p + 5] == ';'):
                        q = 3
                    elif (self.lista[p + 5] == ','):
                        q = 1
                        p = p + 6
                    elif (self.lista[p + 5] == '='):
                        q = 4
                        p  = p + 1
                    else:
                        q = Qe
                        texto = "\nError en la linea "+ str(linea) +". No esta bien colocada la estructura . Luego de una variable pueden seguir los signos ';' , ',' o '=' para continuar. "
                        if tex == 0:
                            textocomentario2.delete("1.0",END)
                            textocomentario2.insert("1.0",texto)
                        else:
                            textocomentario2.insert("1.0",texto)
                

            elif q == 3:
                if ent==0:
                    if self.lista[p + 3] == ";":
                        if self.lista[p + 5]!= "$" :
                            texto = "\nLinea " + str(linea) + " correcta."
                            if tex == 0:
                                textocomentario2.delete("1.0",END)
                                textocomentario2.insert("1.0",texto)
                            else:
                                textocomentario2.insert("1.0",texto)
                            tex = 1
                            linea = linea + 1
                            q = 0
                            p = p + 5
                            aim=0
                        elif self.lista[p + 5] == "$":
                            texto = "\nLinea " + str(linea) + " correcta."
                            q = Qe
                            if tex == 0:
                                textocomentario2.delete("1.0",END)
                                textocomentario2.insert("1.0",texto)
                            else:
                                textocomentario2.insert("1.0",texto)
                            tex = 1
                if ent==1:
                    if self.lista[p + 5] == ";":
                        if self.lista[p + 7]!= "$" :
                            texto = "\nLinea " + str(linea) + " correcta."
                            
                            if tex == 0:
                                textocomentario2.delete("1.0",END)
                                textocomentario2.insert("1.0",texto)
                            else:
                                textocomentario2.insert("1.0",texto)
                            tex = 1
                            linea = linea + 1
                            q = 0
                            p = p + 7
                            aim=0
                        elif self.lista[p + 7] == "$":
                            
                            texto = "\nLinea " + str(linea) + " correcta."
                            q = Qe
                            if tex == 0:
                                textocomentario2.delete("1.0",END)
                                textocomentario2.insert("1.0",texto)
                            else:
                                textocomentario2.insert("1.0",texto)
                            tex = 1
                
            
            elif q == 4:
                if ent == 0:
                    while (self.lista[p + 3] == ''):
                        p = p + 1
                    while re.findall('[0-9]', self.lista[p + 3]):
                        q = 5
                        p = p + 1
                    if q != 5:
                        texto = "\nError en la linea "+ str(linea)+ ". Deberia ser numero para continuar. "
                        if tex == 0:
                            textocomentario2.delete("1.0",END)
                            textocomentario2.insert("1.0",texto)
                        else:
                            textocomentario2.insert("1.0",texto)
                        q= Qe
                if ent == 1:
                    while (self.lista[p + 5] == ''):
                        p = p + 1
                    while re.findall('[0-9]', self.lista[p + 5]):
                        q = 5
                        p = p + 1
                    if q != 5:
                        texto = "\nError en la linea "+ str(linea)+ ". Deberia ser numero para continuar. "
                        q= Qe
                        if tex == 0:
                            textocomentario2.delete("1.0",END)
                            textocomentario2.insert("1.0",texto)
                        else:
                            textocomentario2.insert("1.0",texto)
                

            elif q == 5: 
                if ent == 0:
                    if self.lista[p + 3] == ",":
                        q = 1
                        p = p + 4
                        aim=0
                    elif self.lista[p + 3] == ";":
                        q = 3
                    else:
                        texto = "\nError en la linea "+ str(linea)+ ". Deberia ser ',' o ';' para continuar. "
                        q = Qe
                        
                        if tex == 0:
                            textocomentario2.delete("1.0",END)
                            textocomentario2.insert("1.0",texto)
                        else:
                            textocomentario2.insert("1.0",texto)
                if ent == 1:
                    if self.lista[p + 5] == ",":
                        q = 1
                        p = p + 6
                        aim=0
                    elif self.lista[p + 5] == ";":
                        q = 3
                    else:
                        texto = "\nError en la linea "+ str(linea)+ ". Deberia ser ',' o ';' para continuar. "
                        q = Qe
                        if tex == 0:
                            textocomentario2.delete("1.0",END)
                            textocomentario2.insert("1.0",texto)
                        else:
                            textocomentario2.insert("1.0",texto)
                

    def actualizar(self):
        contenido2 = textocomentario1.get("1.0", END)
        self.lista = [linea.strip() for linea in contenido2]

def insertarCuadroTexto(contenido):
    textocomentario1.delete("1.0",END)
    textocomentario1.insert("1.0",contenido)



analizador = Analizador()
miFrame=Frame(root)
miFrame.config(bg="lightblue")
miFrame.pack()

#Labels 
idLabel=Label(miFrame, text="Analizador Sintatico")
idLabel.config(fg="white",bg="black", font=("Verdana",18))
idLabel.grid(row=0,column=1,sticky="e",padx=10,pady=10)

#Botones
botonCrear=Button(miFrame,text="Abrir Archivo", command = analizador.abrirArchivo)
botonCrear.grid(row=1,column=0,sticky="e",padx=10,pady=10)

botonCrear=Button(miFrame,text="Analizar", command = analizador.analizadorS)
botonCrear.grid(row=1,column=5,sticky="e",padx=10,pady=10)

botonCrear=Button(miFrame,text="Actualizar", command = analizador.actualizar)
botonCrear.grid(row=1,column=6,sticky="e",padx=10,pady=10)

#Textos
miFrame2=Frame(root)
miFrame2.config(bg="lightblue")
miFrame2.pack()

textocomentario1=Text(miFrame2, width=40,height=15)
textocomentario1.grid(row=2,column=0,padx=10,pady=10)
scrollVert=Scrollbar(miFrame2, command=textocomentario1.yview)
scrollVert.grid(row=2,column=1,sticky="nsew")

textocomentario1.config(yscrollcommand=scrollVert.set)

textocomentario2=Text(miFrame2, width=40,height=15)
textocomentario2.grid(row=2,column=2,padx=10,pady=10)
scrollVert=Scrollbar(miFrame2, command=textocomentario2.yview)
scrollVert.grid(row=2,column=3,sticky="nsew")

textocomentario2.config(yscrollcommand=scrollVert.set)

root.mainloop()