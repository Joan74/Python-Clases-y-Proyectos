# preguntas = ["Los electrones son mas pequeños que los atomos ", "Toda la radioactidad es producida por el Hombre ",
#              "Los antivioticos curan enfermedades causadas tanto por virus como por bacterias ", "Los seres humanos provienen de especies animales anteriores ",
#              "Los rayos laser funcionan mediante la concentracion de ondas de sonido ", "Los continentes se han estado moviendo a lo largo de millones de años y continuarán hacíendolo en el futuro ",
#              "El centro de la Tierra está muy caliente ", "El Sol gira alrededor de la Tierra ", "Los primeros humanos vivieron al mismo tiempo que los dinosaurios ",
#              "El sol gira alrededor de los planetas"]


# def mostrarlista():
#     for pregunta in preguntas:
#         print(f"\n{preguntas.index(pregunta)+1}. {pregunta}")

#     return mostrarlista


# mostrarlista()

class Pregunta:
    def __init__(self, valor_valido, pregunta, respuestas):
        self.valor_valido=valor_valido
        self.pregunta=pregunta
        self.respuestas=respuestas.split(",",);
    def validarpregunta(self, valor):
        return self.valor_valido == valor;
list = []
print("\nBarcelona, Madrid,  Bilbao, Valencia, Sevilla")
list.append(Pregunta(1, "¿Capital de España?: ", "Barcelona, Madrid,  Bilbao, Valencia, Sevilla" ))
list.append(Pregunta(2, "¿Formula del Agua?", "C3PO,CO2,H2O" ))

for obj in list:
    respuesta = int(input(f"Responda a la pregunta {obj.pregunta}: "))
    if not obj.validarpregunta(respuesta)+1: 
        print("Error")
    else:
        print("Correcto")