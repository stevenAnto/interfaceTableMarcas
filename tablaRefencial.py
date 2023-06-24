import tkinter
from tkinter import ttk
import backend as back
#Instancio una ventana


window = tkinter.Tk()
window.title("Mantenimiento tabla Zonas")

#Agregando funcionalidad a los botones
codigoInput= descripcionInput= estadoRegistroInput=""
contador=0
marFlaAct= False
def adicionarF():
    habilitar()


def verificarFlag():
    global marFlaAct
    if codigoEntrada.get()!="":
        marFlaAct=True

def enviarBD():
    global marFlaAct
    verificarFlag()
    print("masFlaAct",marFlaAct)
    global contador
    contador +=1
    codigoInput = codigoEntrada.get()
    descripcionInput=descripcionEntrada.get()
    estadoRegistroInput=estadoRegistroEntrada.get()
    verificarFlag()
    print("masFlaAct",marFlaAct)
    if marFlaAct:
        print("Estado de masFlaAct",marFlaAct)
        print(codigoInput,descripcionInput,estadoRegistroInput)
        enviarGrilla(contador,codigoInput,descripcionInput,estadoRegistroInput)
    else:
        print("Error")
    blanqueoInputs()
    deshabilitar()
    marFlaAct=False
    print("Termino de atualizar, y regreso al bandera",marFlaAct)
    #blanqueo de inputs
def cancelarBoton():
    global marFlaAct
    blanqueoInputs()
    grilla.selection_remove(grilla.selection())
    deshabilitar()
    marFlaAct=False;

def blanqueoInputs():
    codigoEntrada.delete(0,tkinter.END)
    descripcionEntrada.delete(0,tkinter.END)
    estadoRegistroEntrada.delete(0,tkinter.END)

def habilitar():
    codigoEntrada["state"]="normal"
    descripcionEntrada["state"]="normal"
    estadoRegistroEntrada["state"]="disabled"

def deshabilitar():
    codigoEntrada["state"]="disabled"
    descripcionEntrada["state"]="disabled"
    estadoRegistroEntrada["state"]="disabled"

def modificar():
    seleccion = grilla.selection()
    if seleccion:
        #codigo
        item1=seleccion[0]
        valores = grilla.item(item1,"values")
        print("el primero",item1)
        print("Valores seleccionados",valores)
        print(valores[0])
        habilitar()
        codigoEntrada.insert(0,valores[0])
        descripcionEntrada.insert(0,valores[1])
        estadoRegistroEntrada.insert(0,valores[2])
    else:
        print("no hay seleccion")
    print(seleccion)

def enviarGrilla(indice,codigoInput,descripcionInput,estadoRegistroInput):
    grilla.insert("",tkinter.END,text=str(indice),values=(codigoInput,descripcionInput,estadoRegistroInput))

def llenarGrilla():
    conexion = back.establecer_conexion()
    registrosTodos = back.seleccionar_MARCA(conexion)
    contadorGrilla=1
    for registro in registrosTodos:
        enviarGrilla(contadorGrilla,str(registro[0]),registro[2],registro[1])
        contadorGrilla +=1
    back.cerrar_conexion(conexion)





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
valorDefaul =tkinter.StringVar()
valorDefaul.set("A")
estadoRegistroEntrada =tkinter.Entry(registro,width=2,state="disabled",
        textvariable=valorDefaul)
#default

codigo.grid(row=0,column=0, sticky="new")
descripcion.grid(row=1,column=0, sticky="nswe")
estadoRegistro.grid(row=2,column=0)


codigoEntrada.grid(row=0,column=1, sticky="w")
descripcionEntrada.grid(row=1,column=1, sticky="we")
estadoRegistroEntrada.grid(row=2,column=1,sticky="w")

#agregamos un treeview al segundo frame tabla
grilla = ttk.Treeview(tabla, columns=("codigo","descripcion","estado"))
grilla.column("#0",width=5)
grilla.column("codigo",width=60)
grilla.column("descripcion",width=600)
grilla.column("estado",width=60)

#por defecto crea la primera columa
grilla.heading("#0", text="#")
#pongo nombre  a las otras dos columnas
grilla.heading("codigo", text="Codigo")
grilla.heading("descripcion", text="Descripcion")
grilla.heading("estado", text="Estado")
#grilla.insert("",tkinter.END,text="1",values=("001","Colgate","A"))
grilla.grid(row=0,column=0)
llenarGrilla()

#agregamos widgets al tercer Frame botones

btnAdicionar = tkinter.Button(botones, text="Adicionar", command=adicionarF)
btnModificar = tkinter.Button(botones, text="Modificar", command=modificar)
btnEliminar = tkinter.Button(botones, text="Eliminar")
btnCancelar = tkinter.Button(botones, text="Cancelar", command=cancelarBoton)
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
