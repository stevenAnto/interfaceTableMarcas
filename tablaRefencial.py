import tkinter
from tkinter import ttk
#Instancio una ventana


window = tkinter.Tk()
window.title("Mantenimiento tabla Zonas")

#Agregando funcionalidad a los botones
codigoInput= descripcionInput= estadoRegistroInput=""
def enviarBD():
    codigoInput = codigoEntrada.get()
    descripcionInput=descripcionEntrada.get()
    estadoRegistroInput=estadoRegistroEntrada.get()
    if codigoInput!="":
        print(codigoInput,descripcionInput,estadoRegistroInput)
    else:
        print("Error")

def habilitar():
    codigoEntrada["state"]="normal"
    descripcionEntrada["state"]="normal"
    estadoRegistroEntrada["state"]="normal"


#Instancio un objeto Frame, que sera parte de windon
frame = tkinter.LabelFrame(window, text="GZZ_MARCAS")
#por buena practica este Fram contendra todos los widgets
frame.grid(row=0,column=0,sticky="nswe")

registro = tkinter.LabelFrame(frame,text="Registro de Marcas")
tabla = tkinter.LabelFrame(frame,text="Tabla_Marcas")
botones = tkinter.LabelFrame(frame)
#ubicamos los tres frames, situamos a la izquierda y agregamos padding
registro.grid(row=0,column=0, sticky="nswe")
tabla.grid(row=1,column=0)
#expande a lo horizontal
botones.grid(row=3,column=0, sticky="nswe")

#agregamos widgets el primer frame Registro
codigo = tkinter.Label(registro, text="Codigo", anchor="w")
descripcion = tkinter.Label(registro, text="Descripcion", anchor="w")
estadoRegistro = tkinter.Label(registro, text="Estado Registro")


codigoEntrada =tkinter.Entry(registro,width=10,state="disabled")
descripcionEntrada =tkinter.Entry(registro,width=60,state="disabled")
estadoRegistroEntrada =tkinter.Entry(registro,width=2,state="disabled")

codigo.grid(row=0,column=0, sticky="new")
descripcion.grid(row=1,column=0, sticky="nswe")
estadoRegistro.grid(row=2,column=0)


codigoEntrada.grid(row=0,column=1, sticky="w")
descripcionEntrada.grid(row=1,column=1, sticky="we")
estadoRegistroEntrada.grid(row=2,column=1,sticky="w")

#agregamos un treeview al segundo frame tabla
grilla = ttk.Treeview(tabla, columns=("descripcion","estado"))

#por defecto crea la primera columa
grilla.heading("#0", text="Codigo")
#pongo nombre  a las otras dos columnas
grilla.heading("descripcion", text="Descripcion")
grilla.heading("estado", text="Estado")

grilla.grid(row=0,column=0)

#agregamos widgets al tercer Frame botones

btnAdicionar = tkinter.Button(botones, text="Adicionar", command=habilitar)
btnModificar = tkinter.Button(botones, text="Modificar")
btnEliminar = tkinter.Button(botones, text="Eliminar")
btnCancelar = tkinter.Button(botones, text="Cancelar")
btnInactivar = tkinter.Button(botones, text="Inactivar")
btnReactivar = tkinter.Button(botones, text="Reactivar")
btnActualizar = tkinter.Button(botones, text="Actualizar", command=enviarBD)
btnSalir = tkinter.Button(botones, text="Salir")

#posicionamos los widgets
botones.columnconfigure((0, 1, 2,3), weight=1)

btnAdicionar.grid(row=0,column=0,sticky="we")
btnModificar.grid(row=0,column=1,sticky="we")
btnEliminar.grid(row=0,column=2,sticky="we")
btnCancelar.grid(row=0,column=3,sticky="we")
btnInactivar.grid(row=1,column=0,sticky="we")
btnReactivar.grid(row=1,column=1,sticky="we")
btnActualizar.grid(row=1,column=2,sticky="we")
btnSalir.grid(row=1,column=3,sticky="we")




#Agrego a los 3 padding
for widget in frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
for widget in registro.winfo_children():
    widget.grid_configure(padx=5, pady=5)
for widget in botones.winfo_children():
    widget.grid_configure(padx=10, pady=10)
for widget in tabla.winfo_children():
    widget.grid_configure(padx=20, pady=15)



window.mainloop()
