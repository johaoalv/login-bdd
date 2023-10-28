import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('libros.db')

# Crear una tabla si no existe
conn.execute('''
    CREATE TABLE IF NOT EXISTS libros (
        nombre TEXT,
        id INTEGER,
        precio REAL,
        envio_gratuito BOOLEAN
    )
''')

print("Datos del libro")
nombre = input("Nombre del libro: ")
id = int(input("ID del libro: "))
precio = float(input("Precio del libro: "))
envioGratuito = input("¿Es gratis el envío? (true/false): ").lower() == "true"

# Insertar los datos en la base de datos
conn.execute("INSERT INTO libros (nombre, id, precio, envio_gratuito) VALUES (?, ?, ?, ?)", (nombre, id, precio, envioGratuito))

# Guardar los cambios en la base de datos
conn.commit()

# Cerrar la conexión con la base de datos
conn.close()

print(f'''
    Nombre: {nombre}
    ID: {id}
    Precio: {precio}
    Envío gratuito: {envioGratuito}
''')
