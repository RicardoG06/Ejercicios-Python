import sqlite3

miconexion=sqlite3.connect("PrimeraBase")

miCursor=miconexion.cursor()


#Crear tabla e insertar datos 

miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR (50), PRECIO INTEGER , SECCION VARCHAR (20))")
miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON','15','DEPORTES')")

variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarron", 90, "Ceramica"),
    ("Camion", 20, "Jugueteria")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)


#Leer de la Base de Datos
miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

for producto in variosProductos:
    print("Nombre Articulo: ",producto[0], " Seccion: ", producto[2])

print(variosProductos)



miconexion.commit()


miconexion.close()