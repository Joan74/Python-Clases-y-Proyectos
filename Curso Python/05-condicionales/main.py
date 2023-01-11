""" condicionales,, 
SI se cumple 
ejecutara una cosa 
SI NO:
ejecutara otra

if condicion
   instrucciones
else:
    otras instrucciones

# operadores de comparacion

== igual
!= diferente
< menor que
> mayor que 
<= menor o igual que
>= mayor o igual que

# operadores logicos
and y
or  O
!   negacion
not no tambien lo contrario

"""


"""

# Ejemplo 1

print("\n############## EJEMPLO 1 #################")

 # color = "verde"
print("\n")
color = input("Adivina cual es mi color favorito: ")

if color == "azul":
    print("Enorabuena!!")
    print(" El color es AZUL")

else:
    print(" El color NO es correcto")


# Ejemplo 2

print("\n############## EJEMPLO 2 #################")
print("\n")
year = int(input(" En que año estamos?"))


year = 2020

if year <= 2022:
        print(" Estamos de 2022 en adelante ")

else:
        print("Es un año anterior a 2023")



# Ejemplo 3

print("\n############## EJEMPLO 3 #################")

nombre = "laia Barrio"
ciudad = "Barcelona"
continente = "Europa"
edad = 10
mayoria_edad = 18


if edad >= mayoria_edad:
   
    print(f"{nombre} es mayor de edad!!")
    if continente != "Europa":
        print("Laia NO es europea")
    else:
        print("Laia SI es europea")    
else:
    print(f"{nombre} NO es mayor de edad")




# Ejemplo 4

print("\n############## EJEMPLO 4 #################")

# como utilizar if y else  pero muy sucio a la vista

dia = int(input("Introduce el dia de la semana: "))


if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves") 
            else:
                if dia == 5:
                    print("Es viernes") 
                else:
                    print("Es fin de semana")

# utlizar elif es lo mismo que lo anterior pero mas limpio la mejor

dia = int(input("Introduce el dia de la semana: "))
if dia == 1:
    print("Es lunes ")
elif dia == 2:
    print("Es martes")    
elif dia == 3:
    print("es miercoles")
elif dia == 4:
    print("Es jueves") 
elif dia == 5:
    print("Es viernes") 
else:
    print("es finde")
"""
# Ejemplo 5
# para añadir condiones se utliza and
print("\n############## EJEMPLO 5 #################")


edad_minima = 18
edad_maxima = 67
edad_oficial = int(input("Introduce tu edad: "))

if edad_oficial >= 18 and edad_oficial  <= 67: 
    print("Tienes la edad para trabajar !! ")
else:
     print("No tienes la edad")


# Ejemplo 6

print("\n############## EJEMPLO 6 #################")

pais = "spain"

if pais == "Mexico" or pais == "london" or pais == "grecia" or pais == "spain":
    print(f"{pais} es de habla hispana ")
else:
    print("No es de habla hispana")



# Ejemplo 7

print("\n############## EJEMPLO 7 #################")

pais = "spain"

if not (pais == "Mexico" or pais == "london" or pais == "grecia" or pais == "spain" ):
    print(f"{pais} No es de habla hispana ")
else:
    print(f"{pais} Si es pais de habla hispan")

# Ejemplo 8

print("\n############## EJEMPLO  #################")

pais = "EEUU"

if pais != "Mexico" and pais != "london" and pais != "grecia" and pais != "spain":

    print(f"{pais} No es de habla hispana ")
else:
    print(f"{pais} Si es pais de habla hispan")    





