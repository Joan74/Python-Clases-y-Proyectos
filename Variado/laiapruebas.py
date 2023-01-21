def calculador(n1, n2, basicas=False):

    suma = n1+n2
    resta = n1-n2
    multi = n1*n2
    divi = n1/n2

    cadena = ""
    if basicas == False:

        cadena += "Suma" + str(suma)
        cadena += "\n"
        cadena += "Resta" + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion" + str(multi)
        cadena += "\n"
        cadena += "Division" + str(divi)

    return cadena


print(calculador(5, 5,True ))
