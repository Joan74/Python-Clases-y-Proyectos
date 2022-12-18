"""
Programa que compruebe si una variable esta vacia
y si esta vacia rellenarla con texto en minuscula 
y mostrarla en mayusculas
"""

texto = ""
if len(texto.strip()) <= 0:
    texto = "hola soy minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenidp {texto}")