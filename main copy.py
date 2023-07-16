import tkinter as tk
import mysql.connector
import frames_ref as fr
import frames_pro_cli as fp
import frames_cab as fc
import frames_art as fa
import frames_det as fd

flag = False
user = None
password = None

def login():
    global user, password, flag
    user = username_entry.get()
    password = password_entry.get()

    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            user=user,
            password=password,
            database='control_stock_libreria'
        )
        window.destroy()

        # Cerrar la conexión a la base de datos
        connection.close()
        flag = True

    except mysql.connector.Error as e:
        connection = None
        error_label.config(text="Usuario y/o contraseña incorrectos", fg="red")

def seleccionar_tabla():
    tabla_seleccionada = tabla_listbox.get(tk.ACTIVE)
    if tabla_seleccionada:
        ventana_seleccion.destroy()
        abrir_tabla(tabla_seleccionada)

def abrir_tabla(tabla):
    host = 'localhost'
    port = 3306
    database = 'control_stock_libreria'
    titulo = tabla.upper()
    window = tk.Tk()
    datosConexion = (host, port, user, password, database)

    if tabla == 'GZZ_MARCA':
        tablaMantenimiento = fr.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("MarCod", "MarNom", "MarEstReg")
    elif tabla == 'GZZ_ZONA':
        tablaMantenimiento = fr.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("ZonCod", "ZonDes", "ZonEstReg")

    elif tabla == 'GZZ_UNIDAD_MEDIDA':
        tablaMantenimiento = fr.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("UniMedCod", "UniMedNom", "EstRegCod")
    
    elif tabla == 'GZZ_EMPLEADO':
        tablaMantenimiento = fr.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("EmpCod", "EmpNom", "EstRegCod")

    elif tabla == 'GZZ_ESTADO_REGISTRO':
        tablaMantenimiento = fr.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("EstTegCod", "EstRegDes", "EstRegEstReg")

    elif tabla == 'L1M_PROVEEDOR':
        tablaMantenimiento = fp.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("ProCod", "ProNom", "ProFecInsProAño", "ProFecInsProMes", "ProFecInsProDia", "ProDir", "ProZon", "ProEstReg")

    elif tabla == 'L1M_CLIENTE':
        tablaMantenimiento = fp.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("CliCod", "CliNom", "CliFecInsProAño", "CliFecInsProMes", "CliFecInsProDia", "CliDir", "CliZon", "CliEstReg")

    elif tabla == 'L1T_STOCK_ENTRADA_CAB':
        tablaMantenimiento = fc.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("StoEntCabCod","StoEntCabFecInsAño","StoEntCabFecInsMes","StoEntCabFecInsDia", "StoEntCabPro", "StoEntCanEstReg", "EmpCod")

    elif tabla == 'L1T_STOCK_SALIDA_CAB':
        tablaMantenimiento = fc.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("StoSalCabCod","StoSalCabFecInsAño","StoSalCabFecInsMes","StoSalCabFecInsDia", "StoSalCabCli", "StoSalCanEstReg", "EmpCod")

    elif tabla == 'L1M_ARTICULO':
        tablaMantenimiento = fa.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("ArtCod","ArtNom","ArtCan","ArtDes", "ArtEstReg", "ArtMar", "UniMedCod")

    elif tabla == 'L1T_STOCK_ENTRADA_DET':
        tablaMantenimiento = fd.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("StoEntCabSec","StoEntDetCan","StoEntCabCod","StoEntDetArt", "StoEntCabEstReg")

    elif tabla == 'L1T_STOCK_SALIDA_DET':
        tablaMantenimiento = fd.FrameTabla(
            master=window,
            text=titulo,
            nombreFrame1="Inputs",
            nombreFrame2="Registros",
            datosConexion=datosConexion
        )
        tablaMantenimiento.cargarNomCampos("StoSalCabSec","StoSalDetCan","StoSalCabCod","StoSalDetArt", "StoSalCabEstReg")

    # Poner título al padre
    tablaMantenimiento.master.title(f"Mantenimiento tabla {tabla.capitalize()}")
    tablaMantenimiento.grid(row=1, column=0, sticky="nswe")

    window.mainloop()

window = tk.Tk()
window.title("Login")

username_label = tk.Label(text="Username")
username_entry = tk.Entry()

password_label = tk.Label(text="Password")
password_entry = tk.Entry(show="*")

login_button = tk.Button(text="Login", command=login)
error_label = tk.Label(window, text="", fg="red")

username_label.grid(row=0, column=0, pady=10)
username_entry.grid(row=0, column=1, pady=10)

password_label.grid(row=1, column=0, pady=10)
password_entry.grid(row=1, column=1, pady=10)

login_button.grid(row=2, column=0, columnspan=2, pady=10)

error_label.grid(row=3, column=0, columnspan=2, pady=(0, 10))

window.mainloop()

if flag:
    host = 'localhost'
    port = 3306
    database = 'control_stock_libreria'
    window = tk.Tk()
    datosConexion = (host, port, user, password, database)

    ventana_seleccion = tk.Toplevel(window)
    ventana_seleccion.title("Seleccionar tabla")

    tabla_label = tk.Label(ventana_seleccion, text="Seleccione una tabla:")
    tabla_listbox = tk.Listbox(ventana_seleccion)
    tabla_listbox.pack()

    # Agrega aquí las tablas que deseas mostrar en el listbox
    tablas = ["GZZ_ESTADO_REGISTRO","GZZ_ZONA","GZZ_MARCA", "GZZ_UNIDAD_MEDIDA", "GZZ_EMPLEADO" , "L1M_ARTICULO","L1M_PROVEEDOR","L1M_CLIENTE", "L1T_STOCK_ENTRADA_CAB", "L1T_STOCK_SALIDA_CAB", "L1T_STOCK_ENTRADA_DET", "L1T_STOCK_SALIDA_DET"]

    for tabla in tablas:
        tabla_listbox.insert(tk.END, tabla)

    seleccion_button = tk.Button(ventana_seleccion, text="Seleccionar", command=seleccionar_tabla)
    seleccion_button.pack()

    ventana_seleccion.mainloop()