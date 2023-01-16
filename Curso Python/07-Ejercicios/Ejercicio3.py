"""
Ejercicio 3.
Escribir un programa que muestre los cuadrados (numero multiplicado por si mismo)
de los 60 primeros numeros naturales (del 1 al 60)
resolver con for y con while


"""
contador = 1

while contador in range(61):
    cuadrado = contador*contador
    print(f" el cuadrado de  {contador} es {cuadrado} ")

    contador += 1


print("\n------------------------------------------------")
print()
# se multiplicara por el numero
# For

for numero in range(61+1):

    cuadrado = numero*numero
    print(f"el cuadrado de {numero} es {cuadrado}")
