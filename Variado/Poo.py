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