"""
Modulos: son funcionalidades ya hechas para reutilizar
en python hay muchos modulos, que se pueden consultar aqui.
https://docs.python.org/3/py-modindex.html
podemos conseguir modulos que ya vienen en el lenguaje,
por internet, o crear nuestros modulos
"""

# Importar modulo propio
import mimodulo
print(mimodulo.holaMundo("Juan Manuel")) # Se pude llamar asi
print(mimodulo.calculadora(3, 5, True))
from mimodulo import holaMundo # asi con menos codigo

from mimodulo import * # Asi llamara a todo lo que haya en el modulo
print(holaMundo("Juan Manuel"))
print(calculadora(3, 5, True))

# Modulo fechas
import datetime

print(datetime.date.today())
fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, ") # La fecha como tu quieres qque salga dia mes año
print(fecha_personalizada)

# Modulos matematicas

import math

print("Raiz cuadrada de 10: ", math.sqrt(10)) # raiz cuadradada de 10
print("Numero Pi: ", float(math.pi))
print("Redondear Baja: ", math.floor(7.78797))
print("Redondear Alza : ", math.ceil(7.78797))

# Modulo random
import random

print("Numero aletorio entre 15 y 67: ", random.randint(15, 67))

