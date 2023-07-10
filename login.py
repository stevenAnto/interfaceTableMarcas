import tkinter as tk
from tkinter import messagebox
import mysql.connector

def login():
  username = username_entry.get()
  password = password_entry.get()

  try:
    connection = mysql.connector.connect(
      host='localhost', 
      port=3306, 
      user=username, 
      password=password, 
      database='control_stock_libreria'
      )
  except mysql.connector.Error as e:
    connection = None
    messagebox.showwarning("Login failed", f"Error connecting to database: {e}")
  window.destroy()

window = tk.Tk()
window.title("Login")

username_label = tk.Label(text="Username")
username_entry = tk.Entry()

password_label = tk.Label(text="Password")
password_entry = tk.Entry(show="*")

login_button = tk.Button(text="Login", command=login)

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)

password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)

login_button.grid(row=2, column=0, columnspan=2)

window.mainloop()