nombre = "Juan"
def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

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


print(calculadora())