import tkinter
import objeto as f

window = tkinter.Tk()


tablaMantenimiento = f.FrameTabla(master=window, text="GZZ_MARCAS", nombreFrame1="GAaaaaaaaaaaaa",nombreFrame2="GAAax2")
#poner titulo al padre
tablaMantenimiento.master.title("Mantenimiento tabla Zonas")
tablaMantenimiento.grid(row=1,column=0, sticky="nswe")

window.mainloop()
