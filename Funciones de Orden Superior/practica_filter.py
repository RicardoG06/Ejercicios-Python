"""def numero_par(num):

    if num % 2 == 0:
        return True"""

numeros=[17,24,7,39,8,51,92]

#Recorre la lista en la funcion y devuelve los 
#resultados que cumplen la funcion

#print(list(filter(numero_par,numeros)))

print(list(filter(lambda numero_par: numero_par%2==0, numeros)))

#Filtrado de salario superior a 

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} euros".format(self.nombre,self.cargo,self.salario)

listaEmpleados=[
    Empleado("Juan", "Director", 750000),
    Empleado("Ricardo", "Presindente", 850000),
    Empleado("Antonio", "Administrador", 250000),
    Empleado("Sara", "Secretaria", 27000),
    Empleado("Mario", "Botones", 21000),
]

salario_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleados )

for empleado_salario in salario_altos:
    print(empleado_salario)