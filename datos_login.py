import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('backend.db')

# Crear una tabla si no existe
conn.execute('''
    CREATE TABLE IF NOT EXISTS datos_login (
        nombre TEXT,
        cedula INTEGER,
        ubicacion TEXT,
        salario INT
    )
''')

print("Datos del usuario")
nombre = input("Nombre de usuario: ")
cedula = int(input("CEDULA: "))
ubicacion = input("Donde vives?: ")
salario = int(input("cuanto es su salario:"))

# Insertar los datos en la base de datos
conn.execute("INSERT INTO datos_login (nombre, cedula, ubicacion, salario) VALUES (?, ?, ?, ?)", (nombre, cedula, ubicacion, salario))

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión con la base de datos
conn.close()

print(f'''
    Nombre: {nombre}
    Cedula: {cedula}
    ubicacion: {ubicacion}
    salario: {salario}
''')
