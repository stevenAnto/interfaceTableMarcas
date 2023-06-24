import tkinter
import objeto as f

window = tkinter.Tk()
frame = tkinter.LabelFrame(master=window, text="prueba")
frame.grid(row=0,column=0,sticky="nswe")
registro = tkinter.LabelFrame(frame,text="Registro de Marcas")
registro.grid(row=0,column=0, sticky="nswe")


tablaMantenimiento = f.FrameTabla(master=window, text="GZZ_MARCAS")
#poner titulo al padre
tablaMantenimiento.master.title("Mantenimiento tabla Zonas")
tablaMantenimiento.grid(row=1,column=0, sticky="nswe")

window.mainloop()
