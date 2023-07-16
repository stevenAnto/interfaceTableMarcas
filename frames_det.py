import tkinter
import connection as c
from tkinter import ttk
from typing import Dict, List, Tuple, Any

cabecode=None
artcode=None

class FrameTabla(tkinter.LabelFrame):
    #nombreFrame1 es el nombre del primer Frame, si el primer Frame es registro y el segundo podria ser grilla o el que crea conveniente
    def __init__(self,nombreFrame1:str,nombreFrame2:str,master:Any=None,datosConexion:Tuple=None, **kwargs):
        super().__init__(master,**kwargs)
        #control del input de estado de Registro. Se crea antes la variable
        self.valorCod= tkinter.StringVar()
        self.valorCod.set("")
        self.valorCan= tkinter.StringVar()
        self.valorCan.set("")
        self.valorCabCod= tkinter.StringVar()
        self.valorCabCod.set("")
        self.valorArt= tkinter.StringVar()
        self.valorArt.set("")
        self.valorEst= tkinter.StringVar()
        self.valorEst.set("")

        self.titulo =kwargs["text"]
        self.registro = tkinter.LabelFrame(self, text=nombreFrame1)
        self.registro.grid(row=0,column=0)
        self.tabla = tkinter.LabelFrame(self, text=nombreFrame2)
        self.tabla.grid(row=1,column=0)
        self.botones = tkinter.LabelFrame(self)
        self.botones.grid(row=2,column=0, sticky="nswe")
        
        #Base de datos a la cual se conecta
        self.host=datosConexion[0]
        self.port = datosConexion[1]
        self.user = datosConexion[2]
        self.password = datosConexion[3]
        self.database = datosConexion[4]
        self.conexionTabla = c.Connection(self.host,self.user,self.password,self.database)
        self.widgetsRegistro()
        self.widgetsTabla()
        self.widgetsBotones()
        self.elementosGrilla = [];
        self.actualizarElementosGrilla()
        self.llenarTodaGrilla()

        #Nombres que hacen referencia a los campos de la tabla
        self.campo1 = ""
        self.campo2 = ""
        self.campo3 = ""
        self.campo4 = ""
        self.campo5 = ""

        #En vista que el boton actualizar realizar muchas tareas se creara sus estados
        self.estadoBotonActualizar=""
    def cargarNomCampos(self,campo1:str,campo2:str,campo3:str,campo4:str,campo5:str):
        self.campo1=campo1
        self.campo2=campo2
        self.campo3=campo3
        self.campo4=campo4
        self.campo5=campo5


    def widgetsRegistro(self):
        #Labels
        codigo = tkinter.Label(self.registro, text="Codigo", anchor="w")
        cantidad = tkinter.Label(self.registro, text="cantidad", anchor="w")
        cabcod = tkinter.Label(self.registro, text="Código cabecera", anchor="w")
        articulo = tkinter.Label(self.registro, text="articulo", anchor="w")
        estadoRegistro = tkinter.Label(self.registro, text="Estado Registro", anchor="w")
        #posicinamos
        codigo.grid(row=0,column=0, sticky="new")
        cantidad.grid(row=1,column=0, sticky="nswe")
        cabcod.grid(row=2,column=0, sticky="nswe")
        articulo.grid(row=3,column=0, sticky="nswe")
        estadoRegistro.grid(row=4,column=0)
        #Inputs

        codigoEntrada =tkinter.Entry(self.registro,width=10,state="disabled",
                textvariable=self.valorCod)
        cantidadEntrada =tkinter.Entry(self.registro,width=60,state="disabled",
                textvariable=self.valorCan)
        
        estadoRegistroEntrada =tkinter.Entry(self.registro,width=2,state="disabled",
                textvariable=self.valorEst)
        

        def obtener_marca(event):
            indice_seleccionado = cabcodEntrada.current()
            if indice_seleccionado >= 0:
                global cabecode 
                cabecode = marcas[indice_seleccionado][0]
                print(f"El elemento seleccionado es: {indice_seleccionado}")
                
        self.conexionTabla.connect()
        query = "SELECT * FROM L1T_STOCK_ENTRADA_CAB WHERE StoEntCanEstReg = 'A'"
        marcas = self.conexionTabla.get_zonas_activas(query)
        self.conexionTabla.close()

            # Crear el Combobox de zonas
        cabcodEntrada = ttk.Combobox(self.registro, width=60, state="disabled", textvariable=self.valorCabCod)
        cabcodEntrada['values'] = [marca[0] for marca in marcas]

        # Asociar el evento de selección a la función obtener_indice_seleccionado
        cabcodEntrada.bind("<<ComboboxSelected>>", obtener_marca)

        def obtener_uni(event):
            indice_seleccionado = articuloEntrada.current()
            if indice_seleccionado >= 0:
                global artcode 
                artcode = unis[indice_seleccionado][0]
                print(f"El elemento seleccionado es: {indice_seleccionado}")
                
        self.conexionTabla.connect()
        query = "SELECT * FROM L1M_ARTICULO WHERE ArtEstReg = 'A'"
        unis = self.conexionTabla.get_zonas_activas(query)
        self.conexionTabla.close()

            # Crear el Combobox de zonas
        articuloEntrada = ttk.Combobox(self.registro, width=60, state="disabled", textvariable=self.valorArt)
        articuloEntrada['values'] = [uni[1] for uni in unis]

        # Asociar el evento de selección a la función obtener_indice_seleccionado
        articuloEntrada.bind("<<ComboboxSelected>>", obtener_uni)

        #posicinamos
        codigoEntrada.grid(row=0,column=1, sticky="w")
        cantidadEntrada.grid(row=1,column=1, sticky="we")
        cabcodEntrada.grid(row=2,column=1, sticky="we")
        articuloEntrada.grid(row=3,column=1, sticky="we")
        estadoRegistroEntrada.grid(row=4,column=1,sticky="w")


    #Funcion que me devuelve una lista de los widgets dentro de un Frame
    def hijosFrame(self, framePadre:Any):
        listaChildren = framePadre.winfo_children()
        return listaChildren

    def widgetsTabla(self):
        #agremos un treeview
        grilla = ttk.Treeview(self.tabla, columns=("codigo","cantidad","cabcod","articulo","estado"))
        grilla.column("#0",width=5)
        grilla.column("codigo",width=60)
        grilla.column("cantidad",width=60)
        grilla.column("cabcod",width=60)
        grilla.column("articulo",width=60)
        grilla.column("estado",width=60)
#por defecto crea la primera columa
        grilla.heading("codigo", text="Código")
        grilla.heading("cantidad", text="Cantidad")
        grilla.heading("cabcod", text="CabCod")
        grilla.heading("articulo", text="Articulo")
        grilla.heading("estado", text="Estado")


        grilla.grid(row=0,column=0)

    def widgetsBotones(self):
        #creo botones
        btnAdicionar = tkinter.Button(self.botones, text="Adicionar", command=self.adicionar)
        btnModificar = tkinter.Button(self.botones, text="Modificar", command=self.modificar)
        btnEliminar = tkinter.Button(self.botones, text="Eliminar", command=self.eliminar)
        btnCancelar = tkinter.Button(self.botones, text="Cancelar", command=self.cancelar)
        btnInactivar = tkinter.Button(self.botones, text="Inactivar", command=self.inactivar)
        btnReactivar = tkinter.Button(self.botones, text="Reactivar", command=self.reactivar)
        btnActualizar = tkinter.Button(self.botones, text="Actualizar", command=self.actualizar)
        btnSalir = tkinter.Button(self.botones, text="Salir", command=self.salir)
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

    #funcions de los botones
    def adicionar(self):
        self.habilitar()
        self.valorEst.set("A")
        self.estadoBotonActualizar="adicionar"

    def inactivar(self):
        widgeDeFrameTabla = self.hijosFrame(self.tabla)
        grilla = widgeDeFrameTabla[0]
        seleccion = grilla.selection()
        if seleccion:
            self.estadoBotonActualizar="inactivar"
            itemp =seleccion[0]
            valores = grilla.item(itemp,"values")
            self.putTextInputs(valores[0],valores[1],cabecode,artcode,"I")
        else:
            self.mostrarVentanaEmergente("no hay seleciion")

    def reactivar(self):
        widgeDeFrameTabla = self.hijosFrame(self.tabla)
        grilla = widgeDeFrameTabla[0]
        seleccion = grilla.selection()
        if seleccion:
            self.estadoBotonActualizar="reactivar"
            itemp =seleccion[0]
            valores = grilla.item(itemp,"values")
            self.putTextInputs(valores[0],valores[1],cabecode,artcode,"A")
        else:
            self.mostrarVentanaEmergente("no hay seleciion")

    def eliminar(self):
        widgeDeFrameTabla = self.hijosFrame(self.tabla)
        grilla = widgeDeFrameTabla[0]
        seleccion = grilla.selection()
        if seleccion:
            self.estadoBotonActualizar="eliminar"
            itemp =seleccion[0]
            valores = grilla.item(itemp,"values")
            self.putTextInputs(valores[0],valores[1],cabecode,artcode,"*")
        else:
            self.mostrarVentanaEmergente("no hay seleciion")

    def modificar(self):
        widgeDeFrameTabla = self.hijosFrame(self.tabla)
        grilla = widgeDeFrameTabla[0]
        seleccion = grilla.selection()
        if seleccion:
            self.estadoBotonActualizar="modificar"
            itemp =seleccion[0]
            valores = grilla.item(itemp,"values")
            self.putTextInputs(valores[0],valores[1],cabecode,artcode,valores[4])
            inputs = self.hijosFrame(self.registro)
            inputs[6]["state"]="normal"
            inputs[7]["state"]="disabled"
            inputs[8]["state"]="normal"
            inputs[9]["state"]="normal"
 

        else:
            self.mostrarVentanaEmergente("no hay seleciion")

    def cancelar(self):
        self.estadoBotonActualizar=""
        self.blanqueoInputs()
        self.deshabilitar()
        self.actualizarElementosGrilla()
        self.llenarTodaGrilla()

    def actualizar(self):
        print("entro a actualizar con boton ", self.estadoBotonActualizar)
        #tomo los datos de los inputs
        inputs= self.hijosFrame(self.registro)
        codigoInput = inputs[5].get()
        cantidadInput = inputs[6].get()
        cabcodInput = cabecode
        articuloInput = artcode
        estadoRegistroInput = inputs[7].get()
        print(codigoInput,cantidadInput,cabcodInput,articuloInput,estadoRegistroInput)
        print(self.campo1,self.campo2,self.campo3,self.campo4,self.campo5)
        diccionario ={
                self.campo1:int(codigoInput),
                self.campo2:int(cantidadInput),
                self.campo3:int(cabcodInput),
                self.campo4:int(articuloInput),
                self.campo5:estadoRegistroInput,
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
        elif self.estadoBotonActualizar =="inactivar":
            print("entro inactivar")
            self.conexionTabla.connect()
            actualizar = self.conexionTabla.update_record(self.titulo,self.campo1,
                    int(codigoInput),diccionario)
            self.conexionTabla.close()
            self.blanqueoInputs()
            self.deshabilitar()
            self.actualizarElementosGrilla()
            self.llenarTodaGrilla()
            print(f"insertar {actualizar}")
            self.mostrarVentanaEmergente(actualizar)
        elif self.estadoBotonActualizar=="reactivar":
            print("se reactivar")
            self.conexionTabla.connect()
            actualizar = self.conexionTabla.update_record(self.titulo,self.campo1,
                    int(codigoInput),diccionario)
            self.conexionTabla.close()
            self.blanqueoInputs()
            self.deshabilitar()
            self.actualizarElementosGrilla()
            self.llenarTodaGrilla()
        elif self.estadoBotonActualizar=="eliminar":
            print("se eliminara")
            self.conexionTabla.connect()
            actualizar = self.conexionTabla.update_record(self.titulo,self.campo1,
                    int(codigoInput),diccionario)
            self.conexionTabla.close()
            self.blanqueoInputs()
            self.deshabilitar()
            self.actualizarElementosGrilla()
            self.llenarTodaGrilla()
        elif self.estadoBotonActualizar=="modificar":
            print("se modificara")
            self.conexionTabla.connect()
            actualizar = self.conexionTabla.update_record(self.titulo,self.campo1,
                    int(codigoInput),diccionario)
            self.conexionTabla.close()
            self.blanqueoInputs()
            self.deshabilitar()
            self.actualizarElementosGrilla()
            self.llenarTodaGrilla()

    def salir(self):
        #destruyo al padre jejejje
        self.master.destroy()


    #Funciones auxiliares
    def llenarGrillaUnaFila(self,codigoInput:str,cantidadInput:str,cabcodInput:str,articuloInput:str,estadoRegistroInput:str):
        widgeDeFrameTabla = self.hijosFrame(self.tabla)
        widgeDeFrameTabla[0].insert("",tkinter.END,values=(codigoInput,cantidadInput,cabcodInput,articuloInput,estadoRegistroInput))

    def llenarTodaGrilla(self):
        widgeDeFrameTabla = self.hijosFrame(self.tabla)
        grilla = widgeDeFrameTabla[0]
        filas = grilla.get_children()
        print("filas",filas)
        #vaciar grilla
        for fila in filas:
            if grilla.item(fila):
                grilla.delete(fila)
        print(self.elementosGrilla)
        #llenar de nuevo
        for registro in self.elementosGrilla:
            self.llenarGrillaUnaFila(str(registro[0]),str(registro[1]),str(registro[2]),str(registro[3]),registro[4])



    def putTextInputs(self,codigoInput:str,cantidadInput:str,cabcodInput:str,articuloInput:str,estadoRegistroInput:str):
        print("entro a colocar texto")
        self.valorCod.set(codigoInput)
        self.valorCan.set(cantidadInput)
        self.valorCabCod.set(cabcodInput)
        self.valorArt.set(articuloInput)
        self.valorEst.set(estadoRegistroInput)

    def habilitar(self):
        print("se habilito inputs")
        inputs = self.hijosFrame(self.registro)
        print(len(inputs))
        inputs[5]["state"]="normal"
        inputs[6]["state"]="normal"
        inputs[7]["state"]="disabled"
        inputs[8]["state"]="normal"
        inputs[9]["state"]="normal"

    def deshabilitar(self):
        print("se habilito inputs")
        inputs = self.hijosFrame(self.registro)
        print(len(inputs))
        inputs[5]["state"]="disabled"
        inputs[6]["state"]="disabled"
        inputs[7]["state"]="disabled"
        inputs[8]["state"]="disabled"
        inputs[9]["state"]="disabled"


    def blanqueoInputs(self):
        print("entro blanqueoInputs")
        inputs = self.hijosFrame(self.registro)
        self.valorCod.set("")
        self.valorCan.set("")
        self.valorCabCod.set("")
        self.valorArt.set("")
        self.valorEst.set("")


    def actualizarElementosGrilla(self)->List:
        self.conexionTabla.connect()
        self.elementosGrilla = self.conexionTabla.recuperarDatosTabla(self.titulo)
        self.conexionTabla.close()




    def mostrarVentanaEmergente(self,mensaje:str):
        ventanaEmergente = tkinter.Toplevel(self)
        ventanaEmergente.title("Warning")
        etiqueta = tkinter.Label(ventanaEmergente,text=mensaje)
        etiqueta.pack()
        ventanaEmergente.geometry("+%d+%d" % (self.winfo_rootx() + self.winfo_width() // 2 - ventanaEmergente.winfo_width() // 2,
            self.winfo_rooty() + self.winfo_height() // 2 - ventanaEmergente.winfo_height() // 2))
