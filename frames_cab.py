import tkinter
import connection as c
from tkinter import ttk
from typing import Dict, List, Tuple, Any

procode=None
empcode=None

class FrameTabla(tkinter.LabelFrame):
    #nombreFrame1 es el nombre del primer Frame, si el primer Frame es registro y el segundo podria ser grilla o el que crea conveniente
    def __init__(self,nombreFrame1:str,nombreFrame2:str,master:Any=None,datosConexion:Tuple=None, **kwargs):
        super().__init__(master,**kwargs)
        #control del input de estado de Registro. Se crea antes la variable
        self.valorCod= tkinter.StringVar()
        self.valorCod.set("")
        self.valorAnio= tkinter.StringVar()
        self.valorAnio.set("")
        self.valorMes= tkinter.StringVar()
        self.valorMes.set("")
        self.valorDia= tkinter.StringVar()
        self.valorDia.set("")
        self.valorPro= tkinter.StringVar()
        self.valorPro.set("")
        self.valorEst= tkinter.StringVar()
        self.valorEst.set("")
        self.valorEmp= tkinter.StringVar()
        self.valorEmp.set("")

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
        self.campo6 = ""
        self.campo7 = ""

        #En vista que el boton actualizar realizar muchas tareas se creara sus estados
        self.estadoBotonActualizar=""
    def cargarNomCampos(self,campo1:str,campo2:str,campo3:str,campo4:str,campo5:str,campo6:str,campo7:str):
        self.campo1=campo1
        self.campo2=campo2
        self.campo3=campo3
        self.campo4=campo4
        self.campo5=campo5
        self.campo6=campo6
        self.campo7=campo7


    def widgetsRegistro(self):
        #Labels
        codigo = tkinter.Label(self.registro, text="Codigo", anchor="w")
        anio = tkinter.Label(self.registro, text="año", anchor="w")
        mes = tkinter.Label(self.registro, text="mes", anchor="w")
        dia = tkinter.Label(self.registro, text="dia", anchor="w")
        proveedor = tkinter.Label(self.registro, text="proveedor", anchor="w")
        estadoRegistro = tkinter.Label(self.registro, text="Estado Registro", anchor="w")
        emp = tkinter.Label(self.registro, text="emp", anchor="w")

        #posicinamos
        codigo.grid(row=0,column=0, sticky="new")
        anio.grid(row=1,column=0, sticky="nswe")
        mes.grid(row=2,column=0, sticky="nswe")
        dia.grid(row=3,column=0, sticky="nswe")
        proveedor.grid(row=4,column=0, sticky="nswe")
        estadoRegistro.grid(row=6,column=0)
        emp.grid(row=5,column=0, sticky="nswe")
        
        #Inputs

        codigoEntrada =tkinter.Entry(self.registro,width=10,state="disabled",
                textvariable=self.valorCod)
        anioEntrada =tkinter.Entry(self.registro,width=60,state="disabled",
                textvariable=self.valorAnio)
        mesEntrada =tkinter.Entry(self.registro,width=60,state="disabled",
                textvariable=self.valorMes)
        diaEntrada =tkinter.Entry(self.registro,width=60,state="disabled",
                textvariable=self.valorDia)
        
        estadoRegistroEntrada =tkinter.Entry(self.registro,width=2,state="disabled",
                textvariable=self.valorEst)
        
        def obtener_marca(event):
            indice_seleccionado = proveedorEntrada.current()
            if indice_seleccionado >= 0:
                global procodecode 
                marcacode = marcas[indice_seleccionado][0]
                print(f"El elemento seleccionado es: {indice_seleccionado}")
                
        self.conexionTabla.connect()
        query = "SELECT * FROM L1M_PROVEEDOR WHERE ProEstReg = 'A'"
        marcas = self.conexionTabla.get_zonas_activas(query)
        self.conexionTabla.close()

            # Crear el Combobox de zonas
        proveedorEntrada = ttk.Combobox(self.registro, width=60, state="disabled", textvariable=self.valorPro)
        proveedorEntrada['values'] = [marca[1] for marca in marcas]

        # Asociar el evento de selección a la función obtener_indice_seleccionado
        proveedorEntrada.bind("<<ComboboxSelected>>", obtener_marca)

        def obtener_uni(event):
            indice_seleccionado = empEntrada.current()
            if indice_seleccionado >= 0:
                global empcode 
                empcode = unis[indice_seleccionado][0]
                print(f"El elemento seleccionado es: {indice_seleccionado}")
                
        self.conexionTabla.connect()
        query = "SELECT * FROM GZZ_EMPLEADO WHERE EstRegCod = 'A'"
        unis = self.conexionTabla.get_zonas_activas(query)
        self.conexionTabla.close()

            # Crear el Combobox de zonas
        empEntrada = ttk.Combobox(self.registro, width=60, state="disabled", textvariable=self.valorEmp)
        empEntrada['values'] = [uni[1] for uni in unis]

        # Asociar el evento de selección a la función obtener_indice_seleccionado
        empEntrada.bind("<<ComboboxSelected>>", obtener_uni)

        #posicinamos
        codigoEntrada.grid(row=0,column=1, sticky="w")
        anioEntrada.grid(row=1,column=1, sticky="we")
        mesEntrada.grid(row=2,column=1, sticky="we")
        diaEntrada.grid(row=3,column=1, sticky="we")
        proveedorEntrada.grid(row=4,column=1, sticky="we")
        estadoRegistroEntrada.grid(row=6,column=1,sticky="w")
        empEntrada.grid(row=5,column=1, sticky="we")



    #Funcion que me devuelve una lista de los widgets dentro de un Frame
    def hijosFrame(self, framePadre:Any):
        listaChildren = framePadre.winfo_children()
        return listaChildren

    def widgetsTabla(self):
        #agremos un treeview
        grilla = ttk.Treeview(self.tabla, columns=("codigo","anio","mes","dia","proveedor","estado","empleado"))
        grilla.column("#0",width=5)
        grilla.column("codigo",width=60)
        grilla.column("anio",width=60)
        grilla.column("mes",width=60)
        grilla.column("dia",width=60)
        grilla.column("proveedor",width=60)
        grilla.column("estado",width=60)
        grilla.column("empleado",width=60)
#por defecto crea la primera columa
        grilla.heading("codigo", text="Código")
        grilla.heading("anio", text="Año")
        grilla.heading("mes", text="Mes")
        grilla.heading("dia", text="Dia")
        grilla.heading("proveedor", text="Proveedor")
        grilla.heading("estado", text="Estado")
        grilla.heading("empleado", text="Empleado")



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
            self.putTextInputs(valores[0],valores[1],valores[2],valores[3],procode,"I",empcode)
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
            self.putTextInputs(valores[0],valores[1],valores[2],valores[3],procode,"A",empcode)
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
            self.putTextInputs(valores[0],valores[1],valores[2],valores[3],procode,"*",empcode)
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
            self.putTextInputs(valores[0],valores[1],valores[2],valores[3],procode,valores[5],empcode)
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
        anioInput = inputs[8].get()
        mesInput = inputs[9].get()
        diaInput = inputs[10].get()
        proInput = procode
        estadoRegistroInput = inputs[12].get()
        empInput = empcode
        print(codigoInput,anioInput,mesInput,diaInput,proInput,estadoRegistroInput,empInput)
        print(self.campo1,self.campo2,self.campo3,self.campo4,self.campo5,self.campo6,self.campo7)
        diccionario ={
                self.campo1:int(codigoInput),
                self.campo2:int(anioInput),
                self.campo3:int(mesInput),
                self.campo4:int(diaInput),
                self.campo5:int(proInput),
                self.campo6:estadoRegistroInput,
                self.campo7:int(empInput),

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
    def llenarGrillaUnaFila(self,codigoInput:str,anioInput:str,mesInput:str,diaInput:str,proInput:str,estadoRegistroInput:str,empInput:str):
        widgeDeFrameTabla = self.hijosFrame(self.tabla)
        widgeDeFrameTabla[0].insert("",tkinter.END,values=(codigoInput,anioInput,mesInput,diaInput,proInput,estadoRegistroInput,empInput))

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
            self.llenarGrillaUnaFila(str(registro[0]),str(registro[1]),str(registro[2]),str(registro[3]),str(registro[4]),registro[5],str(registro[6]))



    def putTextInputs(self,codigoInput:str,anioInput:str,mesInput:str,diaInput:str,proInput:str,estadoRegistroInput:str,empInput:str):
        print("entro a colocar texto")
        self.valorCod.set(codigoInput)
        self.valorAnio.set(anioInput)
        self.valorMes.set(mesInput)
        self.valorDia.set(diaInput)
        self.valorPro.set(proInput)
        self.valorEst.set(estadoRegistroInput)
        self.valorEmp.set(empInput)


    def habilitar(self):
        print("se habilito inputs")
        inputs = self.hijosFrame(self.registro)
        print(len(inputs))
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
        self.valorAnio.set("")
        self.valorMes.set("")
        self.valorDia.set("")
        self.valorPro.set("")
        self.valorEst.set("")
        self.valorEmp.set("")


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
