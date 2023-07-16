import tkinter as tk
import mysql.connector
import frames_det as f

flag = False
user = None
password = None

def login():
    global user, password
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
        global flag 
        flag = True

    except mysql.connector.Error as e:
        connection = None
        error_label.config(text=f"Usuario y/o contraseña incorrectos", fg="red")

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
    user = user
    password = password
    database = 'control_stock_libreria'
    titulo = "L1T_STOCK_ENTRADA_DET"
    window = tk.Tk()
    datosConexion = (host, port, user, password, database)

    tablaMantenimiento = f.FrameTabla(
        master=window,
        text=titulo,
        nombreFrame1="GAaaaaaaaaaaaa",
        nombreFrame2="GAAax2",
        datosConexion=datosConexion
    )
    tablaMantenimiento.cargarNomCampos("StoEntCabSec","StoEntDetCan","StoEntCabCod","StoEntDetArt", "StoEntCabEstReg")

    # Poner título al padre
    tablaMantenimiento.master.title("Mantenimiento tabla Zonas")
    tablaMantenimiento.grid(row=1, column=0, sticky="nswe")

    window.mainloop()

   