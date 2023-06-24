import tkinter

window = tkinter.Tk()
window.title("CARGO")

frame = tkinter.Frame(window)
frame.pack()

user_infor_frame = tkinter.LabelFrame(frame, text="User Information")
user_infor_frame.grid(row=0,column=0)

first_name_label= tkinter.Label(user_infor_frame, text="First Name")
first_name_label.grid(row=0, column= 0)
last_name_label= tkinter.Label(user_infor_frame, text="Last Name")
last_name_label.grid(row=1, column= 0)


firstNameEntry=tkinter.Entry(user_infor_frame, width=50)
firstNameEntry.grid(row =0,column=1)
lastNameEntry=tkinter.Entry(user_infor_frame)
lastNameEntry.grid(row=1,column=1)

#agregar padding
for widget in user_infor_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="new", padx=20, pady=20)

registered_label =tkinter.Label(courses_frame, text="Registation")
registered_check =tkinter.Checkbutton(courses_frame, text="Currently Registation")
registered_label.grid(row=0, column=0)
registered_check.grid(row=1,column=0)

boton  = tkinter.Button(frame, text="Enter dat")
boton.grid(row=3, column=0 ,sticky ="news", padx=20, pady=10)




window.mainloop()
