import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

def guardar_en_archivo():
    with open ("doctores.txt", "w", encoding="utf-8")as archivo:
        for doctores in Doctores_data:
            archivo.write(f"{doctores['nombre']}|{doctores['especialidad']}| {doctores['años de experiencia']}|" 
                          f"{doctores['genero']}|{doctores['hospital']}\n")
            
def cargar_treeview():
    #limpiar treeview
    for doctores in TreeViw.get_children():
        TreeViw.delete(doctores)
        #insertar cada paciente
    for i, item in enumerate(Doctores_data):
        TreeViw.insert(
            "","end", iid=str(i),
            values=(
                item["nombre"],
                item["especialidad"],
                item["años de experiencia"],
                item["genero"],
                item["hospital"],
            )
        )
        
Doctores_data=[]
def registrar():
    #crear diccionario
    paciente={
        "nombre":nombre.get(),
        "especialidad":especialidad.get(),
        "años de experiencia":años.get(),
        "genero":genero.get(),
        "hospital": hospital.get(),
    }
    #agregar paciente a la lista
    Doctores_data.append(paciente)
    #linea modificada
    guardar_en_archivo()
    #cargar el treeviw
    cargar_treeview()
    
def cargar_desde_archivo():
    try:
        with open("Doctores.txt", "r", encoding="utf-8")as archivo:
            Doctores_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==7:
                    paciente={
                       "nombre":datos[0],
                       "especialidad":datos[1],
                        "años de experiencia":datos[2],
                        "genero":datos[3],
                        "hospital":datos[4],
                    }
                    Doctores_data.append(paciente)
    except FileNotFoundError:
        open("doctores.txt", "w", encoding="utf-8").close()

#crear ventana
ventana_princpal=tk.Tk()
ventana_princpal.title("Doctores")
ventana_princpal.configure(bg="lightblue")
ventana_princpal.geometry("800x1000")

#nombreDoctor
NombreD=tk.Label( text="nombre completo: ")
NombreD.grid(row=2, column=0, pady=5, padx=5)
nombre=tk.Entry()
nombre.grid(row=2, column=5, pady=5, padx=5)

#especialidad
esp=tk.Label(text="Especialidad:")
esp.grid(row=3, column=0, padx=5, pady=5)
especialidad=tk.Entry()
especialidad.grid(row=3, column=5, padx=5, pady=5)

LabelGenro=tk.Label(text="Genero:")
LabelGenro.grid(row=3, column=0, padx=5, pady=5, sticky="W")

labelaños=tk.Label(text="años de experiencia")
labelaños.grid(row=5, column=0, pady=5, padx=5)

años=tk.StringVar()
años.set("0")
comboTipo=ttk.Spinbox(values=["0", "1", "2", "3", "4"], textvariable=años)
comboTipo.grid(row=5, column=1, pady=5, padx=5)

genero=tk.StringVar()
genero.set("Masculino")
radioMasculino=ttk.Radiobutton( text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, padx=5, pady=5)
radioFemenino=ttk.Radiobutton(text="femenino", variable="genero", value="femenino")
radioFemenino.grid(row=4, column=1, padx=5, pady=5)

#Hospital
labehosp=tk.Label(text="Hospital: ")
labehosp.grid(row=4, column=0, padx=5, pady=5)
hospital=tk.Entry( state="readonly")
hospital.grid(row=4, column=5, pady=5, padx=5)

btn_registrar=tk.Button( text="registar", command=registrar)
btn_registrar.grid(row=10, column=0, columnspan=2, pady=5)

TreeViw=ttk.Treeview(columns=("Nombre", "especialidad", "años", "genero", "hospital"), show="headings")
#definir encabezados
TreeViw.heading("Nombre", text="Nombre")
TreeViw.heading("especialidad", text="Especialidad")
TreeViw.heading("años", text="Años de experiencia")
TreeViw.heading("genero",text="Genero")
TreeViw.heading("hospital", text="Hospital")

#Definir ancho de columnas
TreeViw.column("Nombre", width=120)
TreeViw.column("especialidad", width=120)
TreeViw.column("años", width=60, anchor="center")
TreeViw.column("genero", width=100, anchor="center")
TreeViw.column("hospital", width=150, anchor="center")

#ubicar el Treeveren la cuadricula
TreeViw.grid(row=8, column=1, pady=5, padx=10, columnspan=2, sticky="nsew")

#Scroll vertical
Scroll_y=ttk.Scrollbar(orient="vertical", command=TreeViw.yview)
TreeViw.configure(yscrollcommand=Scroll_y.set)
Scroll_y.grid(row=7, column=2, sticky="ns")

cargar_desde_archivo() #cargar satos desde archivo al inicio de la aplicacion

ventana_princpal.mainloop()
