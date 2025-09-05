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
def cargar_treeview():
    #limpiar treeview
    for paciente in TreeViw.get_children():
        TreeViw.delete(paciente)
        #insertar cada paciente
    for i, item in enumerate(pacientes_data):
        TreeViw.insert(
            "","end", iid=str(i),
            values=(
                item["nombre"],
                item["fecha de nacimienta"],
                item["edad"],
                item["genero"],
                item["grupo sanguineo"],
                item["tipo de seguro"],
                item["centro medico"]
                )
            )
#lista de pacientes
pacientes_data=[]
#funcion de registrar pacientes
def rgistrarPacientes():
    #crear diccionario
    paciente={
        "nombre":nombreP.get(),
        "fecha de nacimienta":fechaN.get(),
        "edad":edadVar.get(),
        "genero":genero.get(),
        "grupo sanguineo": GrpoSanguinioEntry.get(),
        "tipo de seguro": tipo_seguro.get(),
        "centro medico": centromedico.get()
    }
    #agregar paciente a la lista
    pacientes_data.append(paciente)
    #cargar el treeviw
    cargar_treeview()
    
#crear ventana
ventana_princpal=tk.Tk()
ventana_princpal.title("libro de pacientas")
ventana_princpal.configure(bg="lightblue")
ventana_princpal.geometry("800x1000")

#crear contenedor Notebook
pestaña=ttk.Notebook(ventana_princpal)

#crear frame ( uno por pestaña)
freame_pacientes=ttk.Frame(pestaña)
freame_Doctores=ttk.Frame(pestaña)
#agregar pestañas al Notebook
pestaña.add(freame_pacientes, text="pacentes")
pestaña.add(freame_Doctores,text="doctores")
#mostrar las pestañas en la ventana
pestaña.pack(expand=True, fill="both")
#nombre
labelNombre=tk.Label(freame_pacientes, text="nombre completo: ")
labelNombre.grid(row=0, column=0, pady=5, padx=5)
nombreP=tk.Entry(freame_pacientes)
nombreP.grid(row=0, column=1, pady=5, padx=5)

#fecha
labelFecha=tk.Label(freame_pacientes, text="fecha de nacimiento:")
labelFecha.grid(row=1, column=0, padx=5, pady=5)
validacion_fecha=ventana_princpal.register(enmascarar_fecha)
fechaN=ttk.Entry(freame_pacientes, validate="key", validatecommand=(validacion_fecha, '%P'))
fechaN.grid(row=1, column=1, padx=5, pady=5)


#edad(lectura)
labelEdad=tk.Label(freame_pacientes, text="Edad del paciente: ")
labelEdad.grid(row=2, column=0, padx=5, pady=5)
edadVar=tk.StringVar()
edadP=tk.Entry(freame_pacientes, textvariable=edadVar, state="readonly")
edadP.grid(row=2, column=1, pady=5, padx=5)
#genero
LabelGenro=tk.Label(freame_pacientes, text="Genero:")
LabelGenro.grid(row=3, column=0, padx=5, pady=5, sticky="W")

genero=tk.StringVar()
genero.set("Masculino")
radioMasculino=ttk.Radiobutton(freame_pacientes, text="Masculino", variable=genero, value="Masculino")
radioMasculino.grid(row=3, column=1, padx=5, pady=5)
radioFemenino=ttk.Radiobutton(freame_pacientes, text="femenino", variable="genero", value="femenino")
radioFemenino.grid(row=4, column=1, padx=5, pady=5)

#Grupo sanguineo
labelGrupoSanguineo=tk.Label(freame_pacientes, text="Grupo sanguineo: ")
labelGrupoSanguineo.grid(row=5, column=2, pady=5, padx=5)
GrpoSanguinioEntry=tk.Entry(freame_pacientes)
GrpoSanguinioEntry.grid(row=6, column=2, pady=5, padx=5)

#tipo de seguro
labelTipo=tk.Label(freame_pacientes, text="Tipo de seguro")
labelTipo.grid(row=5, column=0, pady=5, padx=5)

tipo_seguro=tk.StringVar()
tipo_seguro.set("publico")
comboTipo=ttk.Combobox(freame_pacientes, values=["publico", "privado", "ninguno"], textvariable=tipo_seguro)
comboTipo.grid(row=5, column=1, pady=5, padx=5)

#centro medico
labelCentro=tk.Label(freame_pacientes, text="Centro medico")
labelCentro.grid(row=6, column=0, pady=5, padx=5)
centromedico=tk.StringVar()
centromedico.set("Hospital central")
comboCentro=ttk.Combobox(freame_pacientes, values=["Hospital central", "clinica norte", "centro sur"], textvariable=centromedico)
comboCentro.grid(row=6, column=1, pady=5, padx=5)

#fream para los botones
btn_frame=tk.Frame(freame_pacientes)
btn_frame.grid(row=8, column=0, columnspan=2, pady=5, sticky="w")

#boton REistrar
btn_registrar=tk.Button(btn_frame, text="registar", command=rgistrarPacientes)
btn_registrar.grid(row=1, column=0, columnspan=2, pady=5)
#boton eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.grid(row=0, column=1, columnspan=1, padx=5, pady=5)

#crea TreeViw para mostrar paciente
TreeViw=ttk.Treeview(freame_pacientes, columns=("Nombre", "fechaN", "Edad", "genero", "grupoS", "tipoS", "centroM"), show="headings")
#definir encabezados
TreeViw.heading("Nombre", text="Nombre completo")
TreeViw.heading("fechaN", text="Fecha de nacimiento")
TreeViw.heading("Edad", text="Edad")
TreeViw.heading("genero",text="Genero")
TreeViw.heading("grupoS", text="Grupo Sanguinieo")
TreeViw.heading("tipoS", text="Tipo de seguro")
TreeViw.heading("centroM", text="Centro medico")

#Definir ancho de columnas
TreeViw.column("Nombre", width=120)
TreeViw.column("fechaN", width=120)
TreeViw.column("Edad", width=60, anchor="center")
TreeViw.column("genero", width=100, anchor="center")
TreeViw.column("grupoS", width=50, anchor="center")
TreeViw.column("tipoS", width=100, anchor="center")
TreeViw.column("centroM", width=120)

#ubicar el Treeveren la cuadricula
TreeViw.grid(row=8, column=1, pady=5, padx=10, columnspan=2, sticky="nsew")

#Scroll vertical
Scroll_y=ttk.Scrollbar(freame_pacientes, orient="vertical", command=TreeViw.yview)
TreeViw.configure(yscrollcommand=Scroll_y.set)
Scroll_y.grid(row=7, column=2, sticky="ns")


NombreD=tk.Label(freame_Doctores, text="Registro de doctores ")
NombreD.configure(font="Arialblack")
NombreD.grid(row=0, column=5, pady=5, padx=5)

#nombreDoctor
labelNombreD=tk.Label(freame_Doctores, text="nombre completo: ")
labelNombreD.grid(row=2, column=0, pady=5, padx=5)
nombreD=tk.Entry(freame_Doctores)
nombreD.grid(row=2, column=5, pady=5, padx=5)

#fechaDoctor
labelFechaD=tk.Label(freame_Doctores, text="fecha de nacimiento:")
labelFechaD.grid(row=3, column=0, padx=5, pady=5)
fechaD=tk.Entry(freame_Doctores)
fechaD.grid(row=3, column=5, padx=5, pady=5)

#edad(lectura)
labeEdad=tk.Label(freame_Doctores, text="Edad del paciente: ")
labeEdad.grid(row=4, column=0, padx=5, pady=5)
edadD=tk.Entry(freame_Doctores, state="readonly")
edadD.grid(row=4, column=5, pady=5, padx=5)


Telefo=tk.Label(freame_Doctores, text="nombre completo: ")
Telefo.grid(row=5, column=0, pady=5, padx=5)
TelD=tk.Entry(freame_Doctores)
TelD.grid(row=5, column=5, pady=5, padx=5)

#fream para los botones
btn_frame=tk.Frame(freame_Doctores)
btn_frame.grid(row=10, column=3, columnspan=4, pady=5, sticky="ns")

#boton REistrar
btn_registrard=tk.Button(btn_frame, text="registar", command="")
btn_registrard.grid(row=10, column=3, columnspan=1, pady=5)
btn_registrard.configure(bg="green")
#boton eliminar
btn_eliminar=tk.Button(btn_frame, text="Eliminar", command="")
btn_eliminar.configure(bg="red")
btn_eliminar.grid(row=10, column=6, columnspan=2, padx=5, pady=5)



ventana_princpal.mainloop()
