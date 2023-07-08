import tkinter
import frames as f
"""Vamos a instanciar un objeto de la clase frames, la cual
tiene como atributos los valores para hacer la conextion a la base de datos"""
host = 'localhost'
port = 3306
user = 'root'
password = 'contra456'
database = 'control_stock_libreria'
titulo = "GZZ_MARCAS"
window = tkinter.Tk()
datosConexion = (host,port,user,password,database)


tablaMantenimiento = f.FrameTabla(master=window, text=titulo, nombreFrame1="GAaaaaaaaaaaaa",nombreFrame2="GAAax2",datosConexion=datosConexion)
tablaMantenimiento.cargarNomCampos("MarCod","MarEstReg","MarNom")
#poner titulo al padre
tablaMantenimiento.master.title("Mantenimiento tabla Zonas")
tablaMantenimiento.grid(row=1,column=0, sticky="nswe")

window.mainloop()
