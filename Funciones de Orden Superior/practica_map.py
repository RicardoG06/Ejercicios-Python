class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene un salario de {} euros".format(self.nombre,self.cargo,self.salario)

listaEmpleados=[
    Empleado("Juan", "Director", 6700),
    Empleado("Ricardo", "Presindente", 7500),
    Empleado("Antonio", "Administrador", 2100),
    Empleado("Sara", "Secretaria", 2150),
    Empleado("Mario", "Botones", 2100),
]

def calculo_comision(empleado):
    if(empleado.salario >= 3000):
        empleado.salario=empleado.salario * 1.03
    return empleado

listaEmpleadosComision=map(calculo_comision,listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)

