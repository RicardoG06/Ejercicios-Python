import sqlite3

miconexion=sqlite3.connect("GestionProductos")

miCursor=miconexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[
    ("pelota",20,"juguetería"),
    ("pantalon",15,"confección"),
    ("destornillador",25,"ferretería"),
    ("jarron",45,"cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

#Actualizar un dato de una tabla 
miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 35 WHERE NOMBRE_ARTICULO = 'pelota'")

#Borrar un registro de una tabla
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 4")


miconexion.commit()


miconexion.close()