import tkinter as tk

ventanaPrincipal=tk.Tk()
ventanaPrincipal.title("Pruebas")
ventanaPrincipal.geometry("600x450")
ventanaPrincipal.configure(bg="#75e4e4")

Label=tk.Label(ventanaPrincipal,text=":", bg="#80DDD1")
Label.grid(row=0,column=0,padx=10,pady=5,sticky="w") 

Label=tk.Label(ventanaPrincipal,text=":", bg="#80DDD1")
Label.grid(row=1,column=0,padx=10,pady=5,sticky="w")

entry=tk.Entry(ventanaPrincipal)
entry.grid(row=0,column=1,padx=10,pady=5,sticky="we")

entry=tk.Entry(ventanaPrincipal)
entry.grid(row=1,column=1,padx=10,pady=5,sticky="we")

ventanaPrincipal.mainloop()