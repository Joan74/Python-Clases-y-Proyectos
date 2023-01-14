print("\n-----------------------------------------------------------------------------------------------------------------")
numero = 0

def calculadora():
    numero1 = int(input("\nIntroduce numero a multiplicar 1: "))
    numero2 = int(input("Introduce numero a multiplicar 2: "))
    print(f"La Multiplicacion es {numero1*numero2}")
    
    demanda()

def demanda():
    n1 = int(input("\nIntroduce numero 1: "))
    n2 = int(input("Introduce numero 2: "))
    if n1 < n2:
        for numero in range(n1,n2):
            print(len(numero))
            print(numero) 
            
    else:
        print(f"\nEl numero 1 debe ser menor al dos") 
       
    return demanda

calculadora()

