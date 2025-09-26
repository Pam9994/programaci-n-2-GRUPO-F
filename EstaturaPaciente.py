import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
#funciones
def enmascarar_fecha(texto):
    limpio=''.join(filter(str.isdigit, texto)) 
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>8:
        formato_final=f"{limpio[:2]}, {limpio[2:]}"
    else:
        formato_final=limpio
    if fechaN.get()!=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_Nacimiento=datetime.strptime(fechaN.get(), "%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_Nacimiento.year
        edadVar.set(edad)
    else:
        edadVar.set(edad)
    return True

def guardar_en_archivo():
    with open ("pacienteEstatura.txt", "w", encoding="utf-8")as archivo:
        for paciente in pacientes_data:
            archivo.write(f"{paciente['nombre del paciente']}|{paciente['fecha de nacimiento']}| {paciente['calculo de edad']}|" 
                          f"{paciente['grupo sanguineo']}|{paciente['tipo de seguro']}|"
                          f"{paciente['centro medico']}|{paciente['estatura del paciente']}\n")

def cargar_treeview():
    #limpiar treeview
    for paciente in TreeViw.get_children():
        TreeViw.delete(paciente)
        #insertar cada paciente
    for i, item in enumerate(pacientes_data):
        TreeViw.insert(
            "","end", iid=str(i),
            values=(
                item["nombre del paciente"],
                item["fecha de nacimiento"],
                item["calculo de edad"],
                item["grupo sanguineo"],
                item["tipo de seguro"],
                item["centro medico"],
                item["estatura del paciente"]
                )
            )
#lista de pacientes
pacientes_data=[]
#funcion de registrar pacientes
def registrarPacientes():
    #crear diccionario
    paciente={
        "nombre del paciente":nombre.get(),
        "fecha de nacimiento":fechaN.get(),
        "calculo de edad":edadP.get(),
        "grupo sanguineo": grupo.get(),
        "tipo de seguro": tipo.get(),
        "centro medico": centro.get(),
        "estatura del paciente":est.get()
        }
    #agregar paciente a la lista
    pacientes_data.append(paciente)
    #linea modificada
    guardar_en_archivo()
    #cargar el treeviw
    cargar_treeview()
    
def cargar_desde_archivo_pacintes():
    try:
        with open("pacienteEstatura.txt", "r", encoding="utf-8")as archivo:
            pacientes_data.clear()
            for linea in archivo:
                datos=linea.strip().split("|")
                if len(datos)==7:
                    paciente={
                       "nombre del paciente":datos[0],
                       "fecha de nacimiento":datos[1],
                       "calculo de edad":datos[2],
                       "grupo sanguineo":datos[3],
                       "tipo de seguro":datos[4],
                       "centro medico":datos[5],
                       "estatura del paciente":datos[6]
                    }
                    pacientes_data.append(paciente)
    except FileNotFoundError:
        open("pacienteEstatura.txt", "w", encoding="utf-8").close()


#crear ventana
ventana_princpal=tk.Tk()
ventana_princpal.title("pacientas")
ventana_princpal.configure(bg="lavender")
ventana_princpal.geometry("1200x1000")

#nombredelpaciente
NombreD=tk.Label( text="nombre del paciente: ")
NombreD.grid(row=2, column=0, pady=5, padx=5)
nombre=tk.Entry()
nombre.grid(row=2, column=1, pady=5, padx=5)

#fecha77777777777
labelFecha=tk.Label(text="fecha de nacimiento:")
labelFecha.grid(row=3, column=0, padx=5, pady=5)
validacion_fecha=ventana_princpal.register(enmascarar_fecha)
fechaN=ttk.Entry(validate="key", validatecommand=(validacion_fecha, '%P'))
fechaN.grid(row=3, column=1, padx=5, pady=5)

#edad(lectura)7777777777777
labelEdad=tk.Label(text="Edad del paciente: ")
labelEdad.grid(row=4, column=0, padx=5, pady=5)
edadVar=tk.StringVar()
edadP=tk.Entry(textvariable=edadVar, state="readonly")
edadP.grid(row=4, column=1, pady=5, padx=5)

#Grupo sanguineo
grupoS=tk.Label(text="Grupo sanguineo:")
grupoS.grid(row=5, column=0, padx=5, pady=5)
grupo=tk.Entry()
grupo.grid(row=5, column=1, padx=5, pady=5)

#tipo de seguro
tiposeg=tk.Label(text="Tipo de seguro")
tiposeg.grid(row=4, column=2, pady=5, padx=5)
tipo=tk.StringVar()
tipo.set("ninguno")
comboTipo=ttk.Combobox(values=["privado", "publico", "ninguno"], textvariable=tipo)
comboTipo.grid(row=4, column=3, pady=5, padx=5)

#centro medico
labecentro=tk.Label(text="Centro medico: ")
labecentro.grid(row=6, column=2, padx=5, pady=5)
centro=tk.Entry()
centro.grid(row=6, column=3, pady=5, padx=5)

#estatura
esta=tk.Label(text="Etatura (en cm): ")
esta.grid(row=5, column=2, padx=5, pady=5)
est=tk.Entry()
est.grid(row=5, column=3, pady=5, padx=5)

#botones
btn_registrar=tk.Button( text="registar", command=registrarPacientes)
btn_registrar.grid(row=11, column=0, columnspan=2, pady=5)

TreeViw=ttk.Treeview(columns=("nombre", "fecha", "edad", "grupo", "tipo", "centro", "estatura"), show="headings")
#definir encabezados
TreeViw.heading("nombre", text="Nombre")
TreeViw.heading("fecha", text="Fecha de nacimeiento")
TreeViw.heading("edad", text="Edad")
TreeViw.heading("grupo",text="Grupo sanguineo")
TreeViw.heading("tipo", text="Tipo de seguro")
TreeViw.heading("centro",text="Centro medico")
TreeViw.heading("estatura", text="Estatura")
#Definir ancho de columnas
TreeViw.column("nombre", width=120)
TreeViw.column("fecha", width=120)
TreeViw.column("edad", width=60, anchor="center")
TreeViw.column("grupo", width=160, anchor="center")
TreeViw.column("tipo", width=60, anchor="center")
TreeViw.column("centro", width=100, anchor="center")
TreeViw.column("estatura", width=120, anchor="center")
#ubicar el Treeveren la cuadricula
TreeViw.grid(row=8, column=1, pady=5, padx=10, columnspan=2, sticky="nsew")
#Scroll vertical
Scroll_y=ttk.Scrollbar(orient="vertical", command=TreeViw.yview)
TreeViw.configure(yscrollcommand=Scroll_y.set)
Scroll_y.grid(row=10, column=2, sticky="ns")
cargar_desde_archivo_pacintes() #cargar satos desde archivo al inicio de la aplicacion

ventana_princpal.mainloop()