import re

nombre1="Sandra Lopez"

nombre2="Antonio Gomez"

nombre3="sandra Lopez"

nombre4="Jara Lopez"

nombre5="Lara Lopez"

nombre6="123123123"

nombre7="a21381236"

codigo1="adsadadhakhdakhd71"

codigo2="asdsadhksahd71bnzxc"

codigo3="sadsadsadbjsajdbas"

#Funcion Match = Busca al inicio de cada cadena de texto

#ignora el mayuscula o minuscula
if re.match("Sandra", nombre1, re.IGNORECASE):
    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado")

#Encuentra todos lo que lleven esa cadena junta
if re.match(".ara", nombre5, re.IGNORECASE):
    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado")

#Encuentra todos lo que comienzan en numero
if re.match("\d", nombre6):
    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado")

#Funcion search : Busca en toda la cadena de texto 

if re.search("lopez", nombre1, re.IGNORECASE):
    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado")


if re.search("71", codigo1):
    print("Hemos encontrado el nombre")

else:
    print("No lo hemos encontrado")


