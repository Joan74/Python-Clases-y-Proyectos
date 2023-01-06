
#import pyodbc
import os
os.system('clear')


class Pregunta:
    def __init__(self, valor_valido, pregunta, respuestas, explicacion):
        self.valor_valido = valor_valido
        self.pregunta = pregunta
        self.respuestas = respuestas.split(",",)
        self.explicacion = explicacion

    def validarpregunta(self, valor):
        return self.valor_valido == valor


list = []
list.append(Pregunta(1, "¿Capital de España?", "Barcelona,Madrid,Bilbao,Valencia,Sevilla",
                     "Madrid es un municipio y una ciudad de España, con categoría histórica de villa, ​ es la capital del Estado​ y de la Comunidad de Madrid."))
list.append(Pregunta(2, "¿Formula del Agua?", "C3PO,CO2,H2O",
                     "El agua es una sustancia cuya molécula está compuesta por dos átomos de hidrógeno y uno de oxígeno unidos por un enlace covalente"))
list.append(Pregunta(0, "¿Capital de Cataluña?", "Barcelona,Madrid,Bilbao,Valencia,Sevilla",
                     "Barcelona, la capital cosmopolita de la región de Cataluña en España, es conocida por su arte y arquitectura."))
list.append(Pregunta(1, "La luna es un satelite de jupiter?", "Si,No"))

for obj in list:
    while True:
        try:
            respuesta = int(
                input(f"Responda a la pregunta {obj.pregunta}, valores posibles {obj.respuestas} --> "))-1
        except ValueError:
            print("Entrar un número valido.")
            continue
        if(respuesta > len(obj.respuestas)):
            print(
                f"Error.\n Debe responder un valor entre 1 y {len(obj.respuestas)}")
            continue

        if not obj.validarpregunta(respuesta):
            print(
                f"Error. Es {obj.respuestas[obj.valor_valido]}.\n {obj.explicacion}")
        else:
            print(f"Correcto.\n {obj.explicacion}")
        break