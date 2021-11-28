
#Crear una interfaz gráfica por medio de la cuál obtengan: 
    #a) Nombre completo
    #b) CURP 
    #c) RFC 
    #d) Sexo (Femenino o Masculino) de sus clientes. En este utilizarán un radiobutton
    #e) Mediante tres checkbuttons deberá escoger si le interesa o no alguna de las tres opciones que le podemos ofrecer (inventa el giro de tu negocio y qué le podrías ofrecer)
    #f) Debe incluir por lo menos una imágen y el ícono de la interfazfrom tkinter import *
from tkinter import *

# Configuración de la raíz
raiz = Tk()
raiz.title("Tarea Clase 10")

#Marco para entrada de datos
marco1 = Frame(raiz)
marco1.pack(side='top', anchor="w")
marco1.config(width=480, height=320, cursor="dotbox")
marco1.config(bg="#fef5e7")
marco1.config(bd=6)
marco1.config(relief="ridge")

#Creamos las etiquetas
label1 = Label(marco1, text="Nombre Completo")
label1.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry1 = Entry(marco1)
entry1.grid(row=0, column=1, padx=5, pady=5)
entry1.config(justify="right")

label2 = Label(marco1, text="CURP")
label2.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry2 = Entry(marco1)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show="*")

label3 = Label(marco1, text="RFC")
label3.grid(row=2, column=0, sticky="e", padx=5, pady=5)
entry3 = Entry(marco1)
entry3.grid(row=2, column=1, padx=5, pady=5)
entry3.config(justify="center", show="*")

#Radiobotones para sexo

marco2 = Frame(raiz)
marco2.pack()
marco2.config(width=480, height=320, cursor="dotbox")
marco2.config(bg="#fef5e7")
marco2.config(bd=6)
marco2.config(relief="ridge")

def seleccionar():
    monitor.config(text="{}".format(sexo.get()))

def reset():
    sexo.set(None) #Establecemos el valor en nulo
    monitor.config(text="")

sexo = IntVar()

Label(marco2, text = "Sexo").pack()

Radiobutton(marco2, text="Femenino", variable=sexo, value=1, command=seleccionar).pack()
Radiobutton(marco2, text="Masculino", variable=sexo, value=2, command=seleccionar).pack()

monitor = Label(marco2)
monitor.pack()

Button(marco2, text="Eliminar Selección", command=reset).pack()

#Checkbuttons

marco3 = Frame(raiz)
marco3.pack()
marco3.config(width=480, height=320, cursor="dotbox")
marco3.config(bg="#fef5e7")
marco3.config(bd=6)
marco3.config(relief="ridge")


def pizza():
    cadena = ""
    if (doblequeso.get()):
        cadena += "Con Doble Queso"
    else:
        cadena += "Sin Doble Queso"

    if (extrapeperoni.get()):
        cadena += ", con Extra Peperoni"
    else:
        cadena += ", sin Extra Peperoni"

    if (togo.get()):
        cadena += " y para llevar"
    else:
        cadena += " y para comer en el establecimiento"
        
    monitor.config(text=cadena)

doblequeso = IntVar() 	# 1 si, 0 no
extrapeperoni = IntVar()
togo = IntVar()

from PIL import ImageTk, Image
imagen = ImageTk.PhotoImage(file="pizza.jpg")
Label(marco3, image=imagen).pack(side="left")


Label(marco3, text="¿Cómo quieres tu pizza de Peperoni?").pack(anchor="w")
Checkbutton(marco3, text="Con Doble Queso", variable=doblequeso, onvalue=1, offvalue=0, command=pizza).pack(anchor="w")
Checkbutton(marco3, text="Con Extra Peperoni", variable=extrapeperoni, onvalue=1, offvalue=0, command=pizza).pack(anchor="w")
Checkbutton(marco3, text="Para Llevar", variable=togo, onvalue=1, offvalue=0, command=pizza).pack(anchor="w")

monitor = Label(marco3)
monitor.pack()


raiz.mainloop()
