def numero_usuario(numero1):
    numero1 = int(input("Introduce un numero: "))
    return numero1



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

print(numero_usuario(5))
print(calculadora(numero_usuario))





































# def calculadora ():
#     resultado = ""
#     resultado += f"La SUMA de {numero_usuario} es {numero_usuario+numero_usuario}"
#     resultado += "\n"
#     resultado += f"La RESTA de {numero_usuario} es {numero_usuario-numero_usuario}"
#     resultado += "\n"
#     resultado += f"La MULTIPLICACION de {numero_usuario} es {numero_usuario*numero_usuario}"
#     resultado += "\n"
#     resultado += f"La DIVISION de {numero_usuario} es {numero_usuario/numero_usuario}"
#     return resultado

# numero_usuario(calculadora)
