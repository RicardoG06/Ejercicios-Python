import re

lista_nombres=['Ana',
                'Pedro',
                'Maria',
                'Rosa',
                'Sandra',
                'Celia']

lista_pedidos=['Ma.1',
                'Se1',
                'Ma2',
                'Ba1',
                'Ma:3',
                'Va1',
                'Va2',
                'Ma4',
                'MaA',
                'Ma.5',
                'MaB',
                'Ma:C']

#Te la los elementos el cual se componen de letras entre 
#la 'o' y la 't'
for elemento in lista_nombres:
    if re.findall('[o-t]', elemento):
        print(elemento)

print("----------------------------------")

#Te la los elementos el cual comienzan entre 
#la 'o' y la 't'
for elemento in lista_nombres:
    if re.findall('^[O-T]', elemento):
        print(elemento)

print("----------------------------------")

#Te la los elementos el cual terminan entre 
#la 'o' y la 't'
for elemento in lista_nombres:
    if re.findall('[o-t]$', elemento):
        print(elemento) 

print("----------------------------------")

for elemento in lista_pedidos:
    if re.findall('Ma[0-3]', elemento):
        print(elemento) 

print("----------------------------------")
#Negando lo de arriba (lo contrario)
for elemento in lista_pedidos:
    if re.findall('Ma[^0-3]', elemento):
        print(elemento) 

print("----------------------------------")

for elemento in lista_pedidos:
    if re.findall('Ma[0-3A-B]', elemento):
        print(elemento) 

print("----------------------------------")

for elemento in lista_pedidos:
    if re.findall('Ma[.:]', elemento):
        print(elemento) 

