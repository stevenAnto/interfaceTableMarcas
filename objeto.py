import tkinter
from tkinter import ttk

class FrameTabla(tkinter.LabelFrame):
    def __init__(self, master=None, **Kwargs):
        super().__init__(master,**Kwargs)
        self.registro = tkinter.LabelFrame(self, text="Registro de Cargo")
        self.registro.grid(row=0,column=0)
        self.tabla = tkinter.LabelFrame(self, text="Tabla_Marcas")
        self.tabla.grid(row=1,column=0)
        self.botones = tkinter.LabelFrame(self)
        self.botones.grid(row=2,column=0, sticky="nswe")
        #estilos


        self.widgetsRegistro()
        self.widgetsTabla()
        self.widgetsBotones()
        #atributos globales
        self.codigoEntrada
        self.descripcionEntrada
        self.estadoRegistroEntrada


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

        self.codigoEntrada =tkinter.Entry(self.registro,width=10,state="disabled")
        self.descripcionEntrada =tkinter.Entry(self.registro,width=60,state="disabled")
        self.estadoRegistroEntrada =tkinter.Entry(self.registro,width=2,state="disabled")
        #posicinamos
        self.codigoEntrada.grid(row=0,column=1, sticky="w")
        self.descripcionEntrada.grid(row=1,column=1, sticky="we")
        self.estadoRegistroEntrada.grid(row=2,column=1,sticky="w")

    def widgetsTabla(self):
        #agremos un treeview
        grilla = ttk.Treeview(self.tabla, columns=("descripcion","estado"))

#por defecto crea la primera columa
        grilla.heading("#0", text="Codigo")
#pongo nombre  a las otras dos columnas
        grilla.heading("descripcion", text="Descripcion")
        grilla.heading("estado", text="Estado")

        grilla.grid(row=0,column=0)

    def widgetsBotones(self):
        #creo botones
        btnAdicionar = tkinter.Button(self.botones, text="Adicionar", command=self.habilitar)
        btnModificar = tkinter.Button(self.botones, text="Modificar")
        btnEliminar = tkinter.Button(self.botones, text="Eliminar")
        btnCancelar = tkinter.Button(self.botones, text="Cancelar")
        btnInactivar = tkinter.Button(self.botones, text="Inactivar")
        btnReactivar = tkinter.Button(self.botones, text="Reactivar")
        btnActualizar = tkinter.Button(self.botones, text="Actualizar")
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

    def habilitar(self):
        print("se habilito inputs")
        self.codigoEntrada["state"]="normal"
        self.descripcionEntrada["state"]="normal"
        self.estadoRegistroEntrada["state"]="normal"

    def enviarBD(self):
