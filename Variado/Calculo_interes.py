import os
print()
os.system("clear")

print("#### CALCULO DE INTERES POR DEPOSTIO ####")
print()
cantidad = float(input("¿Cantidad a invertir?: "))
interes = float(input("¿Interes porcentaje anual?: "))
años = int(input("¿Años?: "))
total = round(cantidad * (interes / 100 + 1) ** años, 2)
ganancia = total - cantidad
print(f"\nCapital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
print("-----------------------")
print("\n-----------------------------------------")
print(f"El Capital de Beneficio es: {ganancia}")
print("-----------------------------------------")
print()

