# tipos de Variables


nada = None
cadena = "Hola soy Junama"
cadena = "desarrollador web"
entero = 99
flotante = 4,2
boleano = True
lista = [10, 20, 30, 50, 100]
listaString = [44, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("master", "en", "python")
diccionerio = {
        "nombre": "Juanma",
        "apellido": "barrio",
        "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"probando"

#imprimir un variable

print(listaString)
print(diccionerio)

# mostar tipo de dato
print(type(listaString))
print(type(diccionerio))
print(rango)
print(dato_byte)
"""
insertar numero en una concadenación con str (string)
si se coloca un numero en print da u error , para que salga el numero escribir
ejemplo:
 str ---- dara el numero en comillas "1974"
 int ---- dara elnumero entero
 float--- dara el numero con decimales
 """

# Covertir datos
texto = "hola soy un numerito"

numerito = str(1974)
print(type(numerito))

print(texto + " " + numerito) 
numerito = int(1974)    # dara 1974
print(type(numerito))   # dara la clase detipo str
numerito = float(1974)  # dara 1974,0
print(numerito)

