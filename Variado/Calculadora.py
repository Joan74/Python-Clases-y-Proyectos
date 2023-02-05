print()
import os
os.system ("clear")

n1 = int(input("Introduce el primer numero: "))
n2 = int(input("Introduce el segundo numero: "))
opcion = 0
while True:
    print("""
    Dime ¿que deseas hacer?..

    1) Sumar
    2) Restar
    3) Multiplicar
    4) dividir
    5) Cambiar de numeros
    6) Salir
    """)
    opcion = int(input("Elige una Opción: "))
    if opcion == 1:
        print()
        print(f"RESULTADO: {n1+n2}")
    elif opcion == 2:
        print()
        print(f"RESULTADO: {n1-n2}")
    elif opcion == 3:
        print()
        print(f"RESULTADO: {n1*n2}")
    elif opcion == 4:
        print()
        print(f"RESULTADO: {n1/n2}")
    elif opcion == 5:
        os.system ("clear")
        n1 = int(input("Introduce el primer numero: "))
        n2 = int(input("Introduce el segundo numero: "))

    elif opcion == 6:
          exit()
    else:
        print("Opción Incorrecta!!!!")
