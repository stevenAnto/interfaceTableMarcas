import mysql.connector

# Datos de conexión a la base de datos
host = 'localhost'
port = 3306
user = 'root'
password = 'PasP@wer123'
database = 'control_stock_libreria'

# Función para establecer la conexión a la base de datos
def establecer_conexion():
    try:
        conexion = mysql.connector.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=database
                )
        # La conexión se realizó con éxito
        print("Conexión exitosa a la base de datos.")
        return conexion
    except mysql.connector.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Función para cerrar la conexión a la base de datos
def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada.")
# Función para insertar registros en la tabla GZZ_MARCA
def insertar_marca(conexion, codigo, nombre, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO GZZ_MARCAS (MarCod, MarNom, MarEstReg) VALUES (%s, %s, %s)"
        valores = (codigo, nombre, estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro insertado correctamente en la tabla GZZ_MARCAS.")
        return ("Registro insertado correctamente en la GZZ_MARCAs")
    except mysql.connector.Error as error:
        print("Error al insertar registro en la tabla GZZ_MARCAS:", error)
        return error

# Función para seleccionar todos los registros de la tabla GZZ_MARCA
def seleccionar_MARCA(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM GZZ_MARCAS")
        registros = cursor.fetchall()
        print("Registros en la tabla GZZ_MARCAS:")
        print(registros)
        return registros
    except mysql.connector.Error as error:
        print("Error al seleccionar registros de la tabla GZZ_MARCAS:", error)

def actualizar_marcas(conexion, codigo, nombre , estado):
    try:
        cursor = conexion.cursor()
        sql = "UPDATE GZZ_MARCAS SET MarNom = %s, MarEstReg = %s WHERE MarCod = %s"
        valores = (nombre, estado, codigo)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla GZZ_MARCAS.")
        return "Registro actualizado correctamente en la tabla GZZ_MARCAS"
    except mysql.connector.Error as error:
        print("Error al actualizar registro en la tabla GZZ_MARCAS:", error)
        return error


#conexion = establecer_conexion()

#if conexion is not None:
#    actualizar_marcas(conexion,1,"nueva Mars","I")
#cerrar_conexion(conexion)
