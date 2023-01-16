"""
Escribir un script que nos muestre por pantalla
todos los numeros pares hasta el 120

"""


print("################ EJERCICIO2 ################")

for contador in range(1, 121):
    if contador % 2 == 0:
        print(f"{contador}: Es Par")
    else:
        print(f"{contador}: Es Inpar")
