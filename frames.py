import tkinter
import connection as c
from tkinter import ttk
from typing import Dict, List, Tuple



class FrameTabla(tkinter.LabelFrame):
    #nombreFrame1 es el nombre del primer Frame, si el primer Frame es registro y el segundo podria ser grilla o el que crea conveniente
    def __init__(self,nombreFrame1,nombreFrame2,master=None,datosConexion=None, **kwargs):
        super().__init__(master,**kwargs)
        #control del input de estado de Registro. Se crea antes la variable
        self.valorPre= tkinter.StringVar()
        self.valorPre.set("")

        self.titulo =kwargs["text"]
        self.registro = tkinter.LabelFrame(self, text=nombreFrame1)
        self.registro.grid(row=0,column=0)
        self.tabla = tkinter.LabelFrame(self, text=nombreFrame2)
        self.tabla.grid(row=1,column=0)
        self.botones = tkinter.LabelFrame(self)
        self.botones.grid(row=2,column=0, sticky="nswe")
        self.widgetsRegistro()
        self.widgetsTabla()
        self.widgetsBotones()
        self.elementosGrilla = [];
        #Base de datos a la cual se conecta
        self.host=datosConexion[0]
        self.port = datosConexion[1]
        self.user = datosConexion[2]
        self.password = datosConexion[3]
        self.database = datosConexion[4]
        self.conexionTabla = c.Connection(self.host,self.user,self.password,self.database)
        self.actualizarElementosGrilla()
        self.llenarTodaGrilla()

        #Nombres que hacen referencia al nombre de la tabla
        self.campo1 = ""
        self.campo2 = ""
        self.campo3 = ""

        #En vista que el boton actualizar realizar muchas tareas se creara sus estados
        self.estadoBotonActualizar=""
    def cargarNomCampos(self,campo1,campo2,campo3):
        self.campo1=campo1
        self.campo2=campo2
        self.campo3=campo3


    def widgetsRegistro(self):
        #Labels
        codigo = tkinter.Label(self.registro, text="Codigo", anchor="w")
        descripcion = tkinter.Label(self.registro, text="Descripcion", anchor="w")
        estadoRegistro = tkinter.Label(self.registro, text="Estado Registro", anchor="w")
        #posicinamos
        codigo.grid(row=0,column=0, sticky="new")
        descripcion.grid(row=1,column=0, sticky="nswe")
        estadoRegistro.grid(row=2,column=0)
        #Inputs

        codigoEntrada =tkinter.Entry(self.registro,width=10,state="disabled")
        descripcionEntrada =tkinter.Entry(self.registro,width=60,state="disabled")
        estadoRegistroEntrada =tkinter.Entry(self.registro,width=2,state="disabled",
                textvariable=self.valorPre)
        #posicinamos
        codigoEntrada.grid(row=0,column=1, sticky="w")
        descripcionEntrada.grid(row=1,column=1, sticky="we")
        estadoRegistroEntrada.grid(row=2,column=1,sticky="w")


    #Funcion que me devuelve una lista de los widgets dentro de un Frame
    def hijosFrame(self, framePadre):
        listaChildren = framePadre.winfo_children()
        return listaChildren

    def widgetsTabla(self):
        #agremos un treeview
        grilla = ttk.Treeview(self.tabla, columns=("codigo","descripcion","estado"))
        grilla.column("#0",width=5)
        grilla.column("codigo",width=60)
        grilla.column("descripcion",width=600)
        grilla.column("estado",width=60)
#por defecto crea la primera columa
        grilla.heading("codigo", text="Código")
        grilla.heading("descripcion", text="Descripción")
        grilla.heading("estado", text="Estado")



        grilla.grid(row=0,column=0)

    def widgetsBotones(self):
        #creo botones
        btnAdicionar = tkinter.Button(self.botones, text="Adicionar", command=self.adicionar)
        btnModificar = tkinter.Button(self.botones, text="Modificar")
        btnEliminar = tkinter.Button(self.botones, text="Eliminar")
        btnCancelar = tkinter.Button(self.botones, text="Cancelar")
        btnInactivar = tkinter.Button(self.botones, text="Inactivar")
        btnReactivar = tkinter.Button(self.botones, text="Reactivar")
        btnActualizar = tkinter.Button(self.botones, text="Actualizar", command=self.actualizar)
        btnSalir = tkinter.Button(self.botones, text="Salir")
        #posicionamos botones

        self.botones.columnconfigure((0, 1, 2,3), weight=1)
        btnAdicionar.grid(row=0,column=0,sticky="we")
        btnModificar.grid(row=0,column=1,sticky="we")
        btnEliminar.grid(row=0,column=2,sticky="we")
        btnCancelar.grid(row=0,column=3,sticky="we")
        btnInactivar.grid(row=1,column=0,sticky="we")
        btnReactivar.grid(row=1,column=1,sticky="we")
        btnActualizar.grid(row=1,column=2,sticky="we")
        btnSalir.grid(row=1,column=3,sticky="we")

    def llenarGrillaUnaFila(self,codigoInput,descripcionInput,estadoRegistroInput):
        widgeDeFrameTabla = self.hijosFrame(self.tabla)
        widgeDeFrameTabla[0].insert("",tkinter.END,values=(codigoInput,descripcionInput,estadoRegistroInput))

    def llenarTodaGrilla(self):
        print(self.elementosGrilla)
        for registro in self.elementosGrilla:
            self.llenarGrillaUnaFila(str(registro[0]),registro[2],registro[1])


    def adicionar(self):
        self.habilitar()
        self.valorPre.set("A")
        self.estadoBotonActualizar="adicionar"


    def habilitar(self):
        print("se habilito inputs")
        inputs = self.hijosFrame(self.registro)
        print(len(inputs))
        inputs[3]["state"]="normal"
        inputs[4]["state"]="normal"
        inputs[5]["state"]="disabled"

    def deshabilitar(self):
        print("se habilito inputs")
        inputs = self.hijosFrame(self.registro)
        print(len(inputs))
        inputs[3]["state"]="disabled"
        inputs[4]["state"]="disabled"
        inputs[5]["state"]="disabled"

    def blanqueoInputs(self):
        print("entro blanqueoInputs")
        inputs = self.hijosFrame(self.registro)
        inputs[3].delete(0,tkinter.END)
        inputs[4].delete(0,tkinter.END)
        inputs[5].delete(0,tkinter.END)


    def actualizarElementosGrilla(self)->List:
        self.conexionTabla.connect()
        self.elementosGrilla = self.conexionTabla.recuperarDatosTabla(self.titulo)
        self.conexionTabla.close()

    def actualizar(self):
        #tomo los datos de los inputs
        inputs= self.hijosFrame(self.registro)
        codigoInput = inputs[3].get()
        descripcionInput = inputs[4].get()
        estadoRegistroInput = inputs[5].get()
        print(codigoInput,descripcionInput,estadoRegistroInput)
        print(self.campo1,self.campo2,self.campo3)
        diccionario ={
                self.campo1:int(codigoInput),
                self.campo2:estadoRegistroInput,
                self.campo3:descripcionInput,
                }
        print(diccionario)
        if self.estadoBotonActualizar=="adicionar":
            print("Entro a adicionar")
            self.conexionTabla.connect()
            insertar =self.conexionTabla.insert_record(self.titulo,diccionario)
            self.conexionTabla.close()
            self.blanqueoInputs()
            self.deshabilitar()
            self.actualizarElementosGrilla()
            self.llenarTodaGrilla()
            print(f"insertar {insertar}")
            self.mostrarVentanaEmergente(insertar)


    def mostrarVentanaEmergente(self,mensaje):
        ventanaEmergente = tkinter.Toplevel(self)
        ventanaEmergente.title("Warning")
        etiqueta = tkinter.Label(ventanaEmergente,text=mensaje)
        etiqueta.pack()
        ventanaEmergente.geometry("+%d+%d" % (self.winfo_rootx() + self.winfo_width() // 2 - ventanaEmergente.winfo_width() // 2,
            self.winfo_rooty() + self.winfo_height() // 2 - ventanaEmergente.winfo_height() // 2))
