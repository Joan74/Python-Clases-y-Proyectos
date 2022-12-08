print()
import os
os.system ("clear")
print("\n")
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
print(f"Bienbenido/a {nombre} Veo que tienes {edad} años")
opcion = 0
while True:
    print("-----------------------------------")
    print("""
          Que deseas hacer?.
          1) Calculadora Basica
          2) Calculo de Intereses
          3) Salir
          
          
""")
    print("-----------------------------------")
    opcion = int(input("Elige opcion: "))
    print("-----------------------")
    if opcion == 1:
        
        n1 = int(input("Introduce un Numero: "))
        n2 = int(input("Introduce segundo Numero: "))
        print("-------------------------------")
        if n1 > n2:
            print(f"La Suma es : {n1+n2}")
            print(f"La Resta es : {n1-n2}")
            print(f"La Multipicacion es : {n1*n2}")
            print(f"La Division es : {n1/n2}")
        else:
            print("----------------------------------------------------")
            print("El SEGUNDO  numero no puede ser MAYOR al PRIMERO!!!!")
    
    elif opcion == 2:
        print("-----------------------------------------")
        print("#### CALCULO DE INTERES POR DEPOSTIO ####")
        print("-----------------------------------------")
        print()
        cantidad = float(input("¿Cantidad a invertir?: "))
        interes = float(input("¿Interes porcentaje anual?: "))
        años = int(input("¿Años?: "))
        print("-----------------------")
        print()
        print(f"Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
        print("-----------------------")
    elif opcion == 3:
         os.system ("clear"), exit()
    else:
         print("Opcion Incorrecta!!!!")