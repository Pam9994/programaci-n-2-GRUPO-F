import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#funcion pra mostrar los datos seleccionado
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("Seleccion", f"Has elegido la opcion: {seleccion}")

#crea ventana principal
ventana=tk.Tk()
ventana.title("emjemplo comobox")
ventana.geometry("600x450")
#etiqueta
etiqueta=tk.Label(ventana, text="Seleccion especialidad: ")
etiqueta.grid(row=0, column=0, padx=10, pady=10, sticky="w")

#Crea Combobox
opcion=["Cardiologia", "Neurologia", "Pediatria", "dermatologia"]
combo=ttk.Combobox(ventana, values=opcion, state="readonly")
combo.current(0) #seleccion de primera opcion por defecto
combo.grid(row=0, column=1, padx=10, pady=10)


#boton para confirmar seleccion
boton=tk.Button(ventana, text="aceptar", command=mostrar)
boton.grid(row=1, column=0, columnspan=2, pady=15)    

ventana.mainloop()