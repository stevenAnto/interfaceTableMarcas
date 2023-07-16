import tkinter
import connection as c
from tkinter import ttk
from typing import Dict, List, Tuple, Any

marcacode=None
unimedcode=None
class FrameTabla(tkinter.LabelFrame):

    def __init__(self, nombreFrame1: str, nombreFrame2: str, master: Any = None, datosConexion: Tuple = None, **kwargs):
        super().__init__(master, **kwargs)

        self.valorCod = tkinter.StringVar()
        self.valorCod.set("")
        self.valorNom = tkinter.StringVar()
        self.valorNom.set("")
        self.valorCan = tkinter.StringVar()
        self.valorCan.set("")
        self.valorDes = tkinter.StringVar()
        self.valorDes.set("")
        self.valorEst = tkinter.StringVar()
        self.valorEst.set("")
        self.valorMar = tkinter.StringVar()
        self.valorMar.set("")
        self.valorUniMedCod = tkinter.StringVar()
        self.valorUniMedCod.set("")

        self.titulo = kwargs["text"]
        self.registro = tkinter.LabelFrame(self, text=nombreFrame1)
        self.registro.grid(row=0, column=0)
        self.tabla = tkinter.LabelFrame(self, text=nombreFrame2)
        self.tabla.grid(row=1, column=0)
        self.botones = tkinter.LabelFrame(self)
        self.botones.grid(row=2, column=0, sticky="nswe")


        self.host = datosConexion[0]
        self.port = datosConexion[1]
        self.user = datosConexion[2]
        self.password = datosConexion[3]
        self.database = datosConexion[4]
        self.conexionTabla = c.Connection(self.host, self.user, self.password, self.database)
        self.widgetsRegistro()
        self.widgetsTabla()
        self.widgetsBotones()
        self.elementosGrilla = [];
        self.actualizarElementosGrilla()
        self.llenarTodaGrilla()


        self.campo1 = ""
        self.campo2 = ""
        self.campo3 = ""
        self.campo4 = ""
        self.campo5 = ""
        self.campo6 = ""
        self.campo7 = ""


        self.estadoBotonActualizar = ""

    def cargarNomCampos(self, campo1: str, campo2: str, campo3: str, campo4: str, campo5: str, campo6: str, campo7: str):
        self.campo1 = campo1
        self.campo2 = campo2
        self.campo3 = campo3
        self.campo4 = campo4
        self.campo5 = campo5
        self.campo6 = campo6
        self.campo7 = campo7

    def widgetsRegistro(self):

        codigo = tkinter.Label(self.registro, text="ArtCod", anchor="w")
        nombre = tkinter.Label(self.registro, text="ArtNom", anchor="w")
        cantidad = tkinter.Label(self.registro, text="ArtCan", anchor="w")
        descripcion = tkinter.Label(self.registro, text="ArtDes", anchor="w")
        estadoRegistro = tkinter.Label(self.registro, text="ArtEstReg", anchor="w")
        marca = tkinter.Label(self.registro, text="ArtMar", anchor="w")
        unidadMedida = tkinter.Label(self.registro, text="UniMedCod", anchor="w")


        codigo.grid(row=0, column=0, sticky="new")
        nombre.grid(row=1, column=0, sticky="nswe")
        cantidad.grid(row=4, column=0, sticky="nswe")
        descripcion.grid(row=2, column=0, sticky="nswe")
        estadoRegistro.grid(row=6, column=0)
        marca.grid(row=3, column=0, sticky="nswe")
        unidadMedida.grid(row=5, column=0, sticky="nswe")



        codigoEntrada = tkinter.Entry(self.registro, width=10, state="disabled", textvariable=self.valorCod)
        nombreEntrada = tkinter.Entry(self.registro, width=60, state="disabled", textvariable=self.valorNom)
        cantidadEntrada = tkinter.Entry(self.registro, width=60, state="disabled", textvariable=self.valorCan)
        descripcionEntrada = tkinter.Entry(self.registro, width=60, state="disabled", textvariable=self.valorDes)
        estadoRegistroEntrada = tkinter.Entry(self.registro, width=2, state="disabled", textvariable=self.valorEst)

        def obtener_marca(event):
            indice_seleccionado = marcaEntrada.current()
            if indice_seleccionado >= 0:
                global marcacode 
                marcacode = marcas[indice_seleccionado][0]
                print(f"El elemento seleccionado es: {indice_seleccionado}")
                
        self.conexionTabla.connect()
        query = "SELECT * FROM GZZ_MARCA WHERE MarEstReg = 'A'"
        marcas = self.conexionTabla.get_zonas_activas(query)
        self.conexionTabla.close()

            # Crear el Combobox de zonas
        marcaEntrada = ttk.Combobox(self.registro, width=60, state="disabled", textvariable=self.valorMar)
        marcaEntrada['values'] = [marca[1] for marca in marcas]

        # Asociar el evento de selección a la función obtener_indice_seleccionado
        marcaEntrada.bind("<<ComboboxSelected>>", obtener_marca)

        def obtener_uni(event):
            indice_seleccionado = unidadMedidaEntrada.current()
            if indice_seleccionado >= 0:
                global unimedcode 
                unimedcode = unis[indice_seleccionado][0]
                print(f"El elemento seleccionado es: {indice_seleccionado}")
                
        self.conexionTabla.connect()
        query = "SELECT * FROM GZZ_UNIDAD_MEDIDA WHERE EstRegCod = 'A'"
        unis = self.conexionTabla.get_zonas_activas(query)
        self.conexionTabla.close()

            # Crear el Combobox de zonas
        unidadMedidaEntrada = ttk.Combobox(self.registro, width=60, state="disabled", textvariable=self.valorUniMedCod)
        unidadMedidaEntrada['values'] = [uni[1] for uni in unis]

        # Asociar el evento de selección a la función obtener_indice_seleccionado
        unidadMedidaEntrada.bind("<<ComboboxSelected>>", obtener_uni)






        codigoEntrada.grid(row=0, column=1, sticky="w")
        nombreEntrada.grid(row=1, column=1, sticky="we")
        cantidadEntrada.grid(row=4, column=1, sticky="we")
        descripcionEntrada.grid(row=2, column=1, sticky="we")
        estadoRegistroEntrada.grid(row=6, column=1, sticky="w")
        marcaEntrada.grid(row=3, column=1, sticky="we")
        unidadMedidaEntrada.grid(row=5, column=1, sticky="we")



    #Funcion que me devuelve una lista de los widgets dentro de un Frame
    def hijosFrame(self, framePadre:Any):
        listaChildren = framePadre.winfo_children()
        return listaChildren
    
    def widgetsTabla(self):
        grilla = ttk.Treeview(self.tabla, columns=("codigo", "nombre", "cantidad", "descripcion", "estado", "marca", "unidadmedida"))
        grilla.column("#0", width=5)
        grilla.column("codigo", width=60)
        grilla.column("nombre", width=600)
        grilla.column("cantidad", width=60)
        grilla.column("descripcion", width=60)
        grilla.column("estado", width=60)
        grilla.column("marca", width=60)
        grilla.column("unidadmedida", width=60)

        grilla.heading("codigo", text="ArtCod")
        grilla.heading("nombre", text="ArtNom")
        grilla.heading("cantidad", text="ArtCan")
        grilla.heading("descripcion", text="ArtDes")
        grilla.heading("estado", text="ArtEstReg")
        grilla.heading("marca", text="ArtMar")
        grilla.heading("unidadmedida", text="UniMedCod")

        grilla.grid(row=0, column=0)

    def widgetsBotones(self):
        btnAdicionar = tkinter.Button(self.botones, text="Adicionar", command=self.adicionar)
        btnModificar = tkinter.Button(self.botones, text="Modificar", command=self.modificar)
        btnEliminar = tkinter.Button(self.botones, text="Eliminar", command=self.eliminar)
        btnCancelar = tkinter.Button(self.botones, text="Cancelar", command=self.cancelar)
        btnInactivar = tkinter.Button(self.botones, text="Inactivar", command=self.inactivar)
        btnReactivar = tkinter.Button(self.botones, text="Reactivar", command=self.reactivar)
        btnActualizar = tkinter.Button(self.botones, text="Actualizar", command=self.actualizar)
        btnSalir = tkinter.Button(self.botones, text="Salir", command=self.salir)

        self.botones.columnconfigure((0, 1, 2, 3), weight=1)
        btnAdicionar.grid(row=0, column=0, sticky="we")
        btnModificar.grid(row=0, column=1, sticky="we")
        btnEliminar.grid(row=0, column=2, sticky="we")
        btnCancelar.grid(row=0, column=3, sticky="we")
        btnInactivar.grid(row=1, column=0, sticky="we")
        btnReactivar.grid(row=1, column=1, sticky="we")
        btnActualizar.grid(row=1, column=2, sticky="we")
        btnSalir.grid(row=1, column=3, sticky="we")

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
            self.putTextInputs(valores[0],valores[1],valores[2],valores[3],"I",marcacode,unimedcode)
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
            self.putTextInputs(valores[0],valores[1],valores[2],valores[3],"A",marcacode,unimedcode)
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
            self.putTextInputs(valores[0],valores[1],valores[2],valores[3],"*",marcacode,unimedcode)
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
            self.putTextInputs(valores[0],valores[1],valores[2],valores[3],valores[4],marcacode,unimedcode)
            inputs = self.hijosFrame(self.registro)
            inputs[8]["state"]="normal"
            inputs[9]["state"]="normal"
            inputs[10]["state"]="normal"
            inputs[11]["state"]="disabled"
            inputs[12]["state"]="normal"
            inputs[13]["state"]="normal"

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
        codigoInput = inputs[7].get()
        nombreInput = inputs[8].get()
        cantidadInput = inputs[9].get()
        descripcionInput = inputs[10].get()
        estadoRegistroInput = inputs[11].get()
        marcaInput = marcacode
        unidadMedidaInput = unimedcode
        print(codigoInput,nombreInput,cantidadInput,descripcionInput,estadoRegistroInput,marcaInput,unidadMedidaInput)
        print(self.campo1,self.campo2,self.campo3,self.campo4,self.campo5,self.campo6,self.campo7)
        diccionario ={
                self.campo1:int(codigoInput),
                self.campo2:nombreInput,
                self.campo3:int(cantidadInput),
                self.campo4:descripcionInput,
                self.campo5:estadoRegistroInput,
                self.campo6:int(marcaInput),
                self.campo7:int(unidadMedidaInput),
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
    def llenarGrillaUnaFila(self,codigoInput:str,nombreInput:str,cantidadInput:str,descripcionInput:str,estadoRegistroInput:str,marcaInput:str,unidadMedidaInput:str):
        widgeDeFrameTabla = self.hijosFrame(self.tabla)
        widgeDeFrameTabla[0].insert("",tkinter.END,values=(codigoInput,nombreInput,cantidadInput,descripcionInput,estadoRegistroInput,marcaInput,unidadMedidaInput))

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
            self.llenarGrillaUnaFila(str(registro[0]),registro[1],str(registro[2]),registro[3],registro[4],str(registro[5]),str(registro[6]))



    def putTextInputs(self,codigoInput:str,nombreInput:str,cantidadInput:str,descripcionInput:str,estadoRegistroInput:str,marcaInput:str,unidadMedidaInput:str):
        print("entro a colocar texto")
        self.valorCod.set(codigoInput)
        self.valorNom.set(nombreInput)
        self.valorCan.set(cantidadInput)
        self.valorDes.set(descripcionInput)
        self.valorEst.set(estadoRegistroInput)
        self.valorMar.set(marcaInput)
        self.valorUniMedCod.set(unidadMedidaInput)

    def habilitar(self):
        print("se habilito inputs")
        inputs = self.hijosFrame(self.registro)
        print(len(inputs))
        inputs[7]["state"]="normal"
        inputs[8]["state"]="normal"
        inputs[9]["state"]="normal"
        inputs[10]["state"]="normal"
        inputs[11]["state"]="disabled"
        inputs[12]["state"]="normal"
        inputs[13]["state"]="normal"

    def deshabilitar(self):
        print("se habilito inputs")
        inputs = self.hijosFrame(self.registro)
        print(len(inputs))
        inputs[7]["state"]="disabled"
        inputs[8]["state"]="disabled"
        inputs[9]["state"]="disabled"
        inputs[10]["state"]="disabled"
        inputs[11]["state"]="disabled"
        inputs[12]["state"]="disabled"
        inputs[13]["state"]="disabled"


    def blanqueoInputs(self):
        print("entro blanqueoInputs")
        inputs = self.hijosFrame(self.registro)
        self.valorCod.set("")
        self.valorNom.set("")
        self.valorCan.set("")
        self.valorDes.set("")
        self.valorEst.set("")
        self.valorMar.set("")
        self.valorUniMedCod.set("")


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
