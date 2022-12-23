"""

FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a la función
tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    # BLOQUE / CONJUNTO DE INSTRUCCIONES
    
nombredeMiFuncion(mi_parametro)
"""

# EJEMPLO 1

print("############ EJEMPLO 1 ############")


def muestraNombre():  # Define la funcion
    print("Juanma")
    print("Marga")
    print("Arnau")
    print("Laia")
    print("\n")


muestraNombre()  # Invocar funcion
muestraNombre()  # Se puede invocar tantas veces quieras

# EJEMPLO 2: Parametros

print("############ EJEMPLO 2 ############")


def mostraTuNombre():
    print("Tu nombe es: Juanma")  # Añadir un valor fijo


mostraTuNombre()
print("----------------------------------------------")

# Mostar varios parametros
print()


def mostraTuNombre(nombre):  # El parametro seria la variable

    print(f"Tu nombre es: {nombre}")


mostraTuNombre("Juanma")
mostraTuNombre("Marga")
mostraTuNombre("Arnau")
mostraTuNombre("Laia")
print("----------------------------------------------")
print()

# Por introduccion de usuario


def mostraTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print(f"Tienes {edad} y eres mayor de edad")
    else:
        print(f"Tienes {edad} y eres menor de edad")


nombre = input("Intoduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostraTuNombre(nombre, edad)
print()
print("-------------------------------------------")
# EJEMPLO 3

print("############ EJEMPLO 3 ############")

def tabla(numero):
    print(f"Tabla de multiplicar {numero}")

    for contador in range(11):
        oprecion = numero*contador
        print(f"{numero} x {contador} = {oprecion}")
    print("\n")


tabla(7) # Le dices de que numero sera la tabla

print("-------------------------------------------")
# EJEMPLO 3.1

print()

for numero_tabla in range(1, 11):
    tabla(numero_tabla)
print("-------------------------------------------")
# EJEMPLO 4

print("############ EJEMPLO 4 ############")

# Parametros opcionales


def getEmpleado(nombre, dni=None):  # El dni sera opcional
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:  # Si es diferente o igual a que este vacio no lo mostrara
        print(f"DNI: {dni}")


getEmpleado("juanma")  # no mostrara el dni
getEmpleado("juanma", "52593187")  # si mostrara el dni al pasar el dato
print("-------------------------------------------")

# EJEMPLO 5: Parametros opcionales y Return o devolver datos

print("############ EJEMPLO 5 ############")


def saludame(nombre):
    saludo = f"Hola, Saludos {nombre}"

    return saludo


print(saludame("Juanma"))
print("-------------------------------------------")
# EJEMPLO 6:  Calculadora en Str

print("############ EJEMPLO 6 ############")


def calculadora(numero1, numero2,):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    divi = numero1 / numero2

    cadena = " "

    cadena += "Suma: " + str(suma)
    cadena += ("\n")
    cadena += "Resta: " + str(resta)
    cadena += ("\n")
    cadena += "Multiplicacion: " + str(multi)
    cadena += ("\n")
    cadena += "Division: " + str(divi)

    return cadena


print(calculadora(54, 4))
print()
print("-------------------------------------------")
# Solo hacer basicas


def calculadora(numero1, numero2, basicas=False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    divi = numero1 / numero2

    cadena = " "
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += ("\n")
        cadena += "Resta: " + str(resta)
        cadena += ("\n")
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += ("\n")
        cadena += "Division: " + str(divi)

    return cadena


print(calculadora(54, 4, True))

print("-------------------------------------------")
# EJEMPLO 7:  Funciones dentro de funciones

print("############ EJEMPLO 7 ############")


def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getApellido(apellidos):
    texto = f"El Apellido es: {apellidos}"
    return texto


print(getNombre("Juanm Manuel"), getApellido("Barrio"))

# esta opcion no hara falta tanto codigo


def devulvetodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellido(apellidos)
    return texto


print(devulvetodo("Juanma", "Barrio"))
print("-------------------------------------------")
# EJEMPLO 8:  Funciones LAMBDA Funcion anonima

print("############ EJEMPLO 8 ############")


def dime_el_year(year): return f"El año es {year}"


print(dime_el_year(2022))
