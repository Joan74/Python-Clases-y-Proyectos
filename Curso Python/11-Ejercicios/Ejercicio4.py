"""
Crear un script que tenga 4 variables
Una lista, un string, un entero y un boleano
y que imprima un mensaje segun el tipo de dato de cada
variable, USAR FUNCIONES
"""


def traducirTipo(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"

    return result


def comprobarTipado(dato, tipo):

    test = isinstance(dato, tipo)
    result = ""

    if test:
        result = f"Este dato es del tipo {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    return result


mi_lista = ["Bon dia", 77]
titulo = "Quien frega hoy"
numero = 44
verdadero = True
print(comprobarTipado(mi_lista, list))
print(comprobarTipado(titulo, str))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))
