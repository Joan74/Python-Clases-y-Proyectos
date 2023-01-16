import tkinter
import tkinter.messagebox

# ----------------- Ventana ---------------------
ventana = tkinter.Tk()
ventana.title("Test General")
ventana.geometry("1200x700")
ventana.resizable(1, 1)
def tabla(numero):
    print(f"Tabla de multiplicar {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    print("\n")       

# ----------------- Etiquetas -------------------

cabecera = tkinter.Label(ventana, text="      Programador Juan Manuel (Python)      ")
cabecera.pack()

# ------------------ Boton ----------------------


def saludo():
    tkinter.Label(ventana, text="Seguro?").pack()


def salir():
    ventana.destroy()


boton = tkinter.Button(ventana, text="Te gusta la ciencia", command= tabla,)
boton.pack(side=tkinter.LEFT)
#boton.place(x=10, y=20)

boton2 = tkinter.Button(ventana, text="Salir", command=salir,)
boton2.pack(side=tkinter.RIGHT)


# ---------------- message box -----------

tkinter.messagebox.showinfo("Test 1", "Comenzamos el Test!!")
respuesta = tkinter.messagebox.askquestion("", "¿Desea Salir?")
if respuesta == "yes":
    tkinter.messagebox.showinfo("", "Hasta Pronto!!!")
    ventana.destroy()
else:
    tkinter.messagebox.showinfo("", "Comenzamos")

# ------------------ IMAGEN ---------------------

# from tkinter import *
# img = tkinter.PhotoImage(
#     file="/Users/juanma/Documents/Hello-Python-main/Python Clases y Proyectos/Variado/Fondo.png")
# lbl_img = tkinter.Label(ventana, image=img)
# lbl_img.pack()


ventana.mainloop()  # Arrancara el programa en ventana
