print("\n-----------------------------------------------------------------------------------------------------------------")


def calculadora():
    numero1 = int(input("\nIntroduce numero 1: "))
    numero2 = int(input("Introduce numero 2: "))
    print(f"La Multiplicacion es {numero1*numero2}")
    for base in range(numero1, numero2):
        print(f"{base} X {base} = {base*base}")


def demanda():
    n1 = int(input("\nIntroduce numero 1: "))
    n2 = int(input("Introduce numero 2: "))
    if n1 < n2:
        for numero in range(n1 + 1, n2):
            print(numero)
            calculadora()
    else:
        print(f"\nEl numero 1 debe ser menor al dos")
        demanda()


demanda()
