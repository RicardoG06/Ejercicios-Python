import re

lista_nombres=['Ana Gomez',
                'Maria Martin',
                'Sandra Lopez',
                'Sandra Martin']

lista_nombres2=['hombres',
                'mujeres',
                'camión',
                'camion',
                'niños',
                'niñas']

lista_dominios=['http://www.ricardoG.es',
                'ftp://www.ricardogG.es',
                'http://www.ricardoG.com',
                'ftp://www.ricardoG.com']

lista_dominios2=['http://www.ricardoñG.es',
                'ftp://www.ricardogG.es',
                'http://www.ricardoG.com',
                'ftp://www.ricardoG.com']

for elemento in lista_nombres:
    if re.findall('^Sandra', elemento):
        print(elemento)

print("----------------------------")

for elemento in lista_nombres:
    if re.findall('Martin$', elemento):
        print(elemento)

print("----------------------------")

for elemento in lista_dominios:
    if re.findall('es$', elemento):
        print(elemento)

print("----------------------------")

for elemento in lista_dominios:
    if re.findall('^ftp', elemento):
        print(elemento)

print("----------------------------")

for elemento in lista_dominios2:
    if re.findall('[ñ]', elemento):
        print(elemento)

print("----------------------------")

for elemento in lista_nombres2:
    if re.findall('niñ[oa]s', elemento):
        print(elemento)

print("----------------------------")


cont=0
for elemento in lista_nombres2:
    if re.findall('cami[oó]n', elemento):
        print(elemento)
        cont=cont+1
print(cont)
