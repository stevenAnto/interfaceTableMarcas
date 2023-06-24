import tkinter

class FrameTabla(tkinter.LabelFrame):
    def __init__(self, master=None, **Kwargs):
        super().__init__(master,**Kwargs)
        self.registro = tkinter.LabelFrame(self, text="Registro de Cargo")
        self.registro.grid(row=0,column=0)
        self.tabla = tkinter.LabelFrame(self, text="Registro de Cargo")
        self.tabla.grid(row=1,column=0)
        self.botones = tkinter.LabelFrame(self, text="Registro de Cargo")
        self.botones.grid(row=2,column=0)
        self.widgetsRegistro()


    def widgetsRegistro(self):
        codigo = tkinter.Label(self.registro, text="Codigo", anchor="w")
        descripcion = tkinter.Label(self.registro, text="Descripcion", anchor="w")
        estadoRegistro = tkinter.Label(self.registro, text="Estado Registro", anchor="w")
        codigo.grid(row=0,column=0, sticky="new")
        descripcion.grid(row=1,column=0, sticky="nswe")
        estadoRegistro.grid(row=2,column=0)
