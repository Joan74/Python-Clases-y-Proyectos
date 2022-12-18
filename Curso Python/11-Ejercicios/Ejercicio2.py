"""
Escribir un programa que añada a una valores a una lista 
mientras que su longitud sea menor a 120 y luego mostar la lista
Usar while y for
"""
print("\n############# Con Bucle FOR #############")
print("------------------------------------------")

coleccion = []
for contador in range(0, 120):
    coleccion.append(f"elemento - {contador}")
    print(f"Mostrando el " + coleccion[contador])
print(coleccion)
print()
print("\n############# Con Bucle WHILE #############")
print("----------------------------------------------")

coleccion = []
x = 0

while x < 120:
    coleccion.append(f"elemento - {x}")
    print(f"Mostrando el " + coleccion[x])
    x += 1

print(coleccion)
