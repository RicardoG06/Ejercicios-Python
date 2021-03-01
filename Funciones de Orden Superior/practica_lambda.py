"""def area_triangulo(base,altura):
    return (base * altura)/2

print(area_triangulo(5,7))"""

area_triangulo=lambda base,altura: (base * altura)/2
al_cubo=lambda numero: numero**3
print(area_triangulo(5,7))
print(al_cubo(4))

destacar_valor=lambda comision: "¡{}! euros".format(comision)
comision_Ana=15343
print(destacar_valor(comision_Ana))