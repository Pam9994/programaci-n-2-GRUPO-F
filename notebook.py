import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#crear ventana
ventana_princpal=tk.Tk()
ventana_princpal.title("libro de pacientas")
ventana_princpal.configure(bg="lightblue")
ventana_princpal.geometry("400x600")

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
fechaN=tk.Entry(freame_pacientes)
fechaN.grid(row=1, column=1, padx=5, pady=5)

#edad(lectura)
labelEdad=tk.Label(freame_pacientes, text="Edad del paciente: ")
labelEdad.grid(row=2, column=0, padx=5, pady=5)
edadP=tk.Entry(freame_pacientes, state="readonly")
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
labelGrupoSanguineo.grid(row=5, column=0, pady=5, padx=5)
GrpoSanguinioEntry=tk.Entry(freame_pacientes)
GrpoSanguinioEntry.grid(row=5, column=0, pady=5, padx=5)

#tipo de seguro
labelTipo=tk.Label(freame_pacientes, text="Tipo de seguro")
labelTipo.grid(row=5, column=1, pady=5, padx=5)

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
ventana_princpal.mainloop()