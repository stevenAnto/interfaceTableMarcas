import cx_Oracle

dsn = 'localhost:1521/orcl'
user = 'Alvarez'
password = '12345'
encoding = 'UTF-8'

def establecer_conexion():
    try:
        conexion = cx_Oracle.connect(
            user=user,
            password=password,
            dsn=dsn,
            encoding=encoding
        )
        # La conexión se realizó con éxito
        print("Conexión exitosa a la base de datos.")
        return conexion
    except cx_Oracle.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Función para cerrar la conexión a la base de datos
def cerrar_conexion(conexion):
    try:
        conexion.close()
        print("Conexión cerrada.")
    except cx_Oracle.Error as error:
        print("Error al cerrar la conexión:", error)

# Función para insertar registros en la tabla GZZ_MARCA
def insertar(conexion, nomTable, atribTable, codigo, nombre, estado_registro):
    try:
        cursor = conexion.cursor()
        sql = f"INSERT INTO {nomTable} {atribTable} VALUES (:1, :2, :3)"
        valores = (codigo, nombre, estado_registro)
        cursor.execute(sql, valores)
        conexion.commit()
        print(f"Registro insertado correctamente en la tabla {nomTable}")
        return (f"Registro insertado correctamente en la {nomTable}")
    except cx_Oracle.Error as error:
        print(f"Error al insertar registro en la tabla {nomTable}", error)
        return error

# Función para seleccionar todos los registros de la tabla GZZ_MARCA
def seleccionar(conexion, nomTable):
    try:
        cursor = conexion.cursor()
        cursor.execute(f"SELECT * FROM {nomTable}")
        registros = cursor.fetchall()
        print(f"Registros en la tabla {nomTable}")
        print(registros)
        return registros
    except cx_Oracle.Error as error:
        print(f"Error al seleccionar registros de la tabla {nomTable}", error)

def actualizar(conexion, nomTable, colName, colER, colCod, codigo, nombre , estado):
    try:
        cursor = conexion.cursor()
        sql = f"UPDATE {nomTable} SET {colName} = :1 , {colER} = :2 WHERE {colCod} = :3"
        valores = (nombre, estado, codigo)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Registro actualizado correctamente en la tabla " + nomTable)
        return "Registro actualizado correctamente en la tabla " + nomTable
    except cx_Oracle.Error as error:
        print("Error al actualizar registro en la tabla "+ nomTable, error)
        return error


#conexion = establecer_conexion()

#if conexion is not None:
#    actualizar_marcas(conexion,1,"nueva Mars","I")
#cerrar_conexion(conexion)
