import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('backend.db')

# Crear una tabla si no existe para almacenar usuarios y contraseñas
conn.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        nombre_usuario TEXT PRIMARY KEY,
        contraseña TEXT
    )
''')

def registrar_usuario():
    print("Programa para registrarse")
    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    # Insertar los datos en la base de datos
    conn.execute("INSERT INTO usuarios (nombre_usuario, contraseña) VALUES (?, ?)", (nombre_usuario, contraseña))
    conn.commit()

    print("Usuario registrado con éxito.")

def validar_credenciales():
    print("Iniciar sesión")
    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    # Consultar la base de datos para verificar las credenciales
    cursor = conn.execute("SELECT nombre_usuario FROM usuarios WHERE nombre_usuario = ? AND contraseña = ?", (nombre_usuario, contraseña))
    resultado = cursor.fetchone()

    if resultado:
        print("Bienvenido!!!")
    else:
        print("Credenciales incorrectas. Inténtalo nuevamente.")

while True:
    print("\n1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        validar_credenciales()
    elif opcion == '3':
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
