import connection as c

host = 'localhost'
port = 3306
user = 'root'
password = 'contra456'
database = 'control_stock_libreria'

conexionMarcas = c.Connection(host,user,password,database)
conexionMarcas.connect()
tabla = "GZZ_MARCAS"
print(conexionMarcas.recuperarDatosTabla(tabla))
data = {
        "MarCod":3,
        "MarNom": "Nuevo Registros",
        "MarEstReg": "A"
        }
conexionMarcas.insert_record(tabla,data)
#acutalizamos
codigo ={
        "MarCod":3
        }
data = {
        "MarNom": "Dato cambiado ",
        "MarEstReg": "A"
        }
conexionMarcas.update_record(tabla,"MarCod",codigo["MarCod"],data)
print(conexionMarcas.recuperarDatosTabla(tabla))
conexionMarcas.close()
