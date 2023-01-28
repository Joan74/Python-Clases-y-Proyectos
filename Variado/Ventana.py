from tkinter import *
#root = Tk()
import tkinter.messagebox
import time
import os

# ----------------- Ventana ---------------------
ventana = tkinter.Tk()
ventana.title("----- Test General -----")

ventana.geometry("1200x700")
ventana.resizable(0, 1)
valor = StringVar()
valor.set('Verdadero')
botonVerdad = valor,1
botonFalso = valor,2

# ------------------ IMAGEN ---------------------


img = tkinter.PhotoImage(file="/Users/juanma/Desktop/fondo.png")


lbl_img = tkinter.Label(ventana, image = img)


lbl_img.pack()


ventana.mainloop()  # Arrancara el programa en ventana


    


def tabla(numero):
    print(f"Tabla de multiplicar {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
    print("\n")

# ----------------- Etiquetas -------------------


cabecera = tkinter.Label(
    ventana, text="      Programador Juan Manuel (Python) \n\n\n---------------\nTest Cultural\n---------------")
cabecera.pack()


# ------------------ Boton ----------------------

def testCultural():
    import os
    os.system("clear")

    aciertos = 0
    fallos = 0
    si = False
    no = True

    while True:
        os.system("clear")
        botonVerdad = tkinter.Button(ventana, text="VERDADERO", command= OptionMenu,).pack()
        botonFalso = tkinter.Button(ventana, text="FALSO", command= OptionMenu,).pack()
        print("\n                         ---------------------------------------------------------------------")
        print("                         ------------------ TEST CIENCIAS VERDADERO O FALSO ------------------")
        print("                         ---------------------------------------------------------------------")

        print("\n")
        print("PULSA 1 VERDADERO")
        print("PULSA 2 FALSO")
        print()
        # PREGUNTAS
        preguntas = ["Los electrones son mas pequeños que los atomos ", "Toda la radioactidad es producida por el Hombre ",
                     "Los antivioticos curan enfermedades causadas tanto por virus como por bacterias ", "Los seres humanos provienen de especies animales anteriores ",
                     "Los rayos laser funcionan mediante la concentracion de ondas de sonido ", "Los continentes se han estado moviendo a lo largo de millones de años y continuarán hacíendolo en el futuro ",
                     "El centro de la Tierra está muy caliente ", "El Sol gira alrededor de la Tierra ", "Los primeros humanos vivieron al mismo tiempo que los dinosaurios ",
                     "El sol gira alrededor de los planetas"]

        def test():
            for pregunta in preguntas:
                print(f"\n{preguntas.index(pregunta)+1}. {pregunta}")
            return test

        test()
        print("\n")
        # RESPUESTAS
        opcion = int(input(f"\nRespuesta pregunta 1: "))
        if opcion == botonVerdad:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
            fallos += 1
        opcion = int(input(f"Respuesta pregunta 2: "))
        if opcion == botonVerdad:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
            fallos += 1
        opcion = int(input(f"Respuesta pregunta 3: "))
        if opcion == 2:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
            fallos += 1
        opcion = int(input(f"Respuesta pregunta 4: "))
        if opcion == 1:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
            fallos += 1
        opcion = int(input(f"Respuesta pregunta 5: "))
        if opcion == 2:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
            fallos += 1
        opcion = int(input(f"Respuesta pregunta 6: "))
        if opcion == 1:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
            fallos += 1
        opcion = int(input(f"Respuesta pregunta 7: "))
        if opcion == 1:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
        opcion = int(input(f"Respuesta pregunta 8: "))
        if opcion == 2:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
            fallos += 1
        opcion = int(input(f"Respuesta pregunta 9: "))
        if opcion == 2:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
            fallos += 1
        opcion = int(input(f"Respuesta pregunta 10: "))
        if opcion == 2:
            print("CORRECTO")
            aciertos += 1
        else:
            print("INCORRECTO")
            fallos += 1
        print(f"\nPreguntas acertadas : {aciertos}")
        print(f"Preguntas falladas : {fallos} ")
        if aciertos <= 4:
            print("\n-------------------------------------")
            print(f"          Test SUSPENDIDO           ")
            print("-------------------------------------")
        else:
            print("\n-------------------------------------")
            print(f"          Test APROBADO             ")
            print("-------------------------------------")
        print()
        print("¿Quieres salir? ")
        answer = input().lower
        if answer() == "si":
            print("Hasta Luego!!!!")
            time.sleep(2.5)
            os.system("clear")
            break
        if answer() == "no":
            print("Perfecto, Comenzamos...")
            time.sleep(2.5)
            os.system("clear")


def saludo():
    tkinter.Label(ventana, text="Seguro?").pack()


def salir():
    respuesta = tkinter.messagebox.askquestion("", "¿Desea Salir?")
    if respuesta == "yes":
        tkinter.messagebox.showinfo("", "HASTA LA PROXIMA")
        #ventana.destroy()
    else:
        tkinter.messagebox.showinfo("", "Comenzamos")
        tabla()

    ventana.destroy()


# Boton AUX
boton = tkinter.Button(ventana, text="TEST", command=testCultural,).pack()
botoNVerdad = tkinter.Button(ventana, text="VERDADERO", command= True,).pack()
botonFalso = tkinter.Button(ventana, text="FALSO", command= False,).pack()


#boton.place(x=10, y=20)

boton2 = tkinter.Button(ventana, text="Salir", command=salir,)
boton2.place(x=10, y=20)


# ---------------- message box -----------

# tkinter.messagebox.showinfo("Test 1", "Comenzamos el Test!!")



