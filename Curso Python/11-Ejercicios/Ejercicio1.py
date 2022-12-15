"""
Hacer un programa que tenga una lista
de 8 numeros enteros y que haga lo siguiente:
OK - Recorrer la lista y mostrarla 
OK - Hacer funcion que recorra lista y mostrarla por string
OK - Ordenarla y mostrarla
OK - Mostrar su longitud
- Buscar algun elemento que el usuario pida por teclado

  
"""
# Crear lista

numeros = [10, 50, 60, 40, 20, 30, 80, 70]

# Hacer funcion que recorra lista y mostrarla por string


def mostarLista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " +str(elemento)
        resultado += "\n"
    return resultado


# Recorrer la lista y mostrarla
print("######### RECORRER Y MOSTAR #########")
"""
for numero in numeros:
    print(numero)
"""    

print(mostarLista(numeros))    

# Ordenar y Mostrar

numeros.sort()
print(mostarLista(numeros)) 

# Mostrar longitud
print(len(numeros))

# Buscar algun elemento que el usuario pida por teclado

busqueda = int(input("Introduce el numero: "))