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
conexionMarcas.close()
