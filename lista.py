#lista y combo box
#listbox una lista de seleccion
#combobox menu de ociones varias
import tkinter as tk
from tkinter import messagebox
ventana=tk.Tk()
ventana.title("Ejemplo listBox")

sintomasLabel=tk.Label(ventana, text="Sintomas")
sintomasLabel.grid(row=0, column=0, padx=5, pady=5, sticky="w")
#crear listbox
lista=tk.Listbox(ventana, selectmode=tk.SINGLE)
lista.insert(1, "delor de cabeza")
lista.insert(2, "Fibre")
lista.insert(3, "Tos")
lista.insert(4, "Dificultad para respirar")
lista.grid(row=0, column=1, pady=10, sticky="we")
#boton para mostrar seleccion
def mostrar():
    seleccionado=lista.get(lista.curselection())
    tk.messagebox.showinfo("Seleccion", f"Has elegido:{seleccionado}")
boton=tk.Button(ventana, text="mostrar seleccion", command=mostrar)
boton.grid(row=1, column=0, padx=10, pady=10)


ventana.mainloop()