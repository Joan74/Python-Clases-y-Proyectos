
"""
Cuanto es el x porciento de x numreros


"""
print("\n")
numero = float(input("Introduce Un numero: "))
print(" ")
porcentaje = float(input(f"Que porcentaje quieres sacar de {numero}?: "))
print(" ")
operacion = (numero * (porcentaje/100))
print(f"El {porcentaje}% de {numero} es {operacion} ")
