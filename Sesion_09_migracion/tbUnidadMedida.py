import tkinter
from tkinter import ttk
import backend as back
#Instancio una ventana


window = tkinter.Tk()
window.title("Mantenimiento tabla GZZ_UNIDAD_MEDIDA")

#Agregando funcionalidad a los botones
codigoInput= descripcionInput= estadoRegistroInput=""
contador=0
marFlaAct= False
#Debido a que la relacion de muchas funciones usan al boton actualizar,
#Pondremos estados a todos los botones, asi el boton actualizar sabra que
#que accion realizar
estadosBotonActualizar=""
def adicionarF():
    global estadosBotonActualizar
    estadosBotonActualizar="insertar"
    print(f"estadosBotonActualizar {estadosBotonActualizar}")
    habilitar()
    blanqueoInputs()
def eliminarF():
    global estadosBotonActualizar
    seleccion = grilla.selection()
    if seleccion:
        estadosBotonActualizar="eliminar"
        print(f"estadosBotonActualizar {estadosBotonActualizar}")
        #codigo
        item1=seleccion[0]
        valores = grilla.item(item1,"values")
        habilitar()
        codigoEntrada.insert(0,valores[0])
        codigoEntrada["state"]="disabled"
        descripcionEntrada.insert(0,valores[1])
        descripcionEntrada["state"]="disabled"
        valorDefaul.set("*")
        estadoRegistroEntrada["state"]="disabled"
    else:
        print("no hay seleccion")
    print(seleccion)
def inactivarF():
    global estadosBotonActualizar
    seleccion = grilla.selection()
    if seleccion:
        estadosBotonActualizar="inactivar"
        print(f"estadosBotonActualizar {estadosBotonActualizar}")
        #codigo
        item1=seleccion[0]
        valores = grilla.item(item1,"values")
        habilitar()
        codigoEntrada.insert(0,valores[0])
        codigoEntrada["state"]="disabled"
        descripcionEntrada.insert(0,valores[1])
        descripcionEntrada["state"]="disabled"
        valorDefaul.set("I")
        estadoRegistroEntrada["state"]="disabled"
    else:
        print("no hay seleccion")
    print(seleccion)

def reactivarF():
    global estadosBotonActualizar
    seleccion = grilla.selection()
    if seleccion:
        estadosBotonActualizar="reactivar"
        print(f"estadosBotonActualizar {estadosBotonActualizar}")
        #codigo
        item1=seleccion[0]
        valores = grilla.item(item1,"values")
        habilitar()
        codigoEntrada.insert(0,valores[0])
        codigoEntrada["state"]="disabled"
        descripcionEntrada.insert(0,valores[1])
        descripcionEntrada["state"]="disabled"
        valorDefaul.set("A")
        estadoRegistroEntrada["state"]="disabled"
    else:
        print("no hay seleccion")
    print(seleccion)
def salirF():
    window.destroy()


def verificarFlag():
    global marFlaAct
    if codigoEntrada.get()!="" and descripcionEntrada.get()!="":
        marFlaAct=True
def modificarF():
    global estadosBotonActualizar
    seleccion = grilla.selection()
    if seleccion:
        estadosBotonActualizar="update"
        #codigo
        item1=seleccion[0]
        valores = grilla.item(item1,"values")
        habilitar()
        codigoEntrada.insert(0,valores[0])
        codigoEntrada["state"]="disabled"
        descripcionEntrada.insert(0,valores[1])
        estadoRegistroEntrada.insert(0,valores[2])
        estadoRegistroEntrada["state"]="disabled"
    else:
        print("no hay seleccion")
    print(seleccion)


def enviarBD():
    global marFlaAct
    global estadosBotonActualizar
    codigoInput = codigoEntrada.get()
    descripcionInput=descripcionEntrada.get()
    estadoRegistroInput=estadoRegistroEntrada.get()
    acciones = ["update","eliminar","inactivar","reactivar"]
    verificarFlag()
    print("masFlaAct",marFlaAct)
    if marFlaAct:
        print("Estado de masFlaAct",marFlaAct)
        if estadosBotonActualizar in acciones:
            actualizo = actualizarRegistro(codigoInput,descripcionInput,estadoRegistroInput)
            mostrarVentanaEmergente(actualizo)
        
        if estadosBotonActualizar=="insertar":
            print(codigoInput,descripcionInput,estadoRegistroInput)
            conexion = back.establecer_conexion()
            nomTable = "GZZ_UNIDAD_MEDIDA"
            atributosTabla = "(UniMedCod, UniMedNom, EstRegCod)"
            inserto=back.insertar(conexion,nomTable,atributosTabla,int(codigoInput),
            descripcionInput,estadoRegistroInput)
            back.cerrar_conexion(conexion)
            mostrarVentanaEmergente(inserto)

        else:
            print("no tiene estado el boton")
        estadosBotonActualizar=""
        valorDefaul.set("A")
        llenarGrilla()

    else:
        mostrarVentanaEmergente("Estado marFlaAct :"+str(marFlaAct))
        print("Error")

    blanqueoInputs()
    deshabilitar()
    marFlaAct=False
    print("Termino de atualizar, y regreso al bandera",marFlaAct)
    #blanqueo de inputs
def cancelarBoton():
    global marFlaAct
    global estadosBotonActualizar
    habilitar()
    blanqueoInputs()
    grilla.selection_remove(grilla.selection())
    valorDefaul.set("A")
    deshabilitar()
    marFlaAct=False;
    estadosBotonActualizar=""

def blanqueoInputs():
    codigoEntrada["state"]="normal"
    descripcionEntrada["state"]="normal"
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

def actualizarRegistro(codigo, nombre, estado):
    global flaBotonActualizar
    verificarFlag()
    conexion = back.establecer_conexion()
    tabName = "GZZ_UNIDAD_MEDIDA"
    colName = "UniMedNom"
    colER = "EstRegCod"
    colCod = "UniMedCod"
    actualizar=back.actualizar(conexion,tabName,colName,colER,colCod,int(codigo),nombre,estado)
    back.cerrar_conexion(conexion)
    marFlaAct=False
    codigoEntrada.delete(0,tkinter.END)
    return actualizar



def enviarGrilla(codigoInput,descripcionInput,estadoRegistroInput):
    grilla.insert("",tkinter.END,values=(codigoInput,descripcionInput,estadoRegistroInput))


def llenarGrilla():
    #error pro treeview vacio
    grilla.delete(*grilla.get_children())
    conexion = back.establecer_conexion()
    registrosTodos = back.seleccionar(conexion,"GZZ_UNIDAD_MEDIDA")
    contadorGrilla=0
    for registro in registrosTodos:
        enviarGrilla(str(registro[0]),registro[1],registro[2])
        contadorGrilla +=1
    back.cerrar_conexion(conexion)

def mostrarVentanaEmergente(texto):
    ventanaEmergente = tkinter.Toplevel(window)
    ventanaEmergente.title("Warning")

    etiqueta = tkinter.Label(ventanaEmergente, text=texto)
    etiqueta.pack(padx=20,pady=20)
    ventanaEmergente.geometry("+%d+%d" % (window.winfo_rootx() + window.winfo_width() // 2 - ventanaEmergente.winfo_width() // 2,
                                           window.winfo_rooty() + window.winfo_height() // 2 - ventanaEmergente.winfo_height() // 2))





    ventanaEmergente.grab_set()







#Instancio un objeto Frame, que sera parte de windon
frame = tkinter.LabelFrame(window, text="GZZ_UNIDAD_MEDIDA")
#por buena practica este Fram contendra todos los widgets
frame.grid(row=0,column=0,sticky="nswe")

registro = tkinter.LabelFrame(frame,text="Registro de Unidades de Medida")
tabla = tkinter.LabelFrame(frame,text="Tabla de Unidades de Medida")
botones = tkinter.LabelFrame(frame)
#ubicamos los tres frames, situamos a la izquierda y agregamos padding
registro.grid(row=0,column=0, sticky="nswe")
tabla.grid(row=1,column=0)
#expande a lo horizontal
botones.grid(row=3,column=0, sticky="nswe")

#agregamos widgets el primer frame Registro
codigo = tkinter.Label(registro, text="Código", anchor="w")
descripcion = tkinter.Label(registro, text="Nombre", anchor="w")
estadoRegistro = tkinter.Label(registro, text="Estado Registro")


codigoEntrada =tkinter.Entry(registro,width=10,state="disabled")
descripcionEntrada =tkinter.Entry(registro,width=80,state="disabled")
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
grilla = ttk.Treeview(tabla, columns=("codigo","nombre","estado"))
grilla.column("#0",width=5)
grilla.column("codigo",width=60)
grilla.column("nombre",width=600)
grilla.column("estado",width=60)

#por defecto crea la primera columa
#pongo nombre  a las otras dos columnas
grilla.heading("codigo", text="Código")
grilla.heading("nombre", text="Nombre")
grilla.heading("estado", text="Estado")
#grilla.insert("",tkinter.END,text="1",values=("001","Colgate","A"))
grilla.grid(row=0,column=0)
llenarGrilla()

#agregamos widgets al tercer Frame botones

btnAdicionar = tkinter.Button(botones, text="Adicionar", command=adicionarF)
btnModificar = tkinter.Button(botones, text="Modificar", command=modificarF)
btnEliminar = tkinter.Button(botones, text="Eliminar", command=eliminarF)
btnCancelar = tkinter.Button(botones, text="Cancelar", command=cancelarBoton)
btnInactivar = tkinter.Button(botones, text="Inactivar",command=inactivarF)
btnReactivar = tkinter.Button(botones, text="Reactivar", command=reactivarF)
btnActualizar = tkinter.Button(botones, text="Actualizar", command=enviarBD)
btnSalir = tkinter.Button(botones, text="Salir", command=salirF)

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
