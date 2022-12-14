"""
Ejercicio 4 
pedir dos numeros al usuario y hacer todas las operaciones
basicas de una calculadora:
"""
import os
os.system("clear")

n1 = float(input("Introduce un numero"))
n2 = float(input("Introduce segundo numero"))

print(" La Suma es: " + str(n1+n2))
print(" La Resta es: " + str(n1-n2))
print(" La Multiplicacion es: " + str(n1*n2))
print(" La Division es: " + str(n1 % n2))
