# Funiones generales
"""
.stip = limpia espacios
.find = busca la palabra
.lower = minusculas
.upper = mayusculas
.replace = remplaza la palabra
instance = comprobar dato
del   = eliminia
len   = comprueba si esta vacio  

"""
def tabla(numero):
    for contador in range(numero,11):
        print(f"Tabla de multiplicar del {contador}")
        for numeros in range(1,11):
            operacion = numeros*contador
            print(f"{contador} x {numeros} = {operacion}")
    
tabla(3)
# tabla(6)
# tabla(9)


        

