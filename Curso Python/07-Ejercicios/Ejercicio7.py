"""
Hacer un programa que muestre tos los numeros imapares
entre dos numeroa que elija el usuario

"""
print("######### Numeros impares ########\n")

numero1 = int(input(f" Introduce primer numero: "))
numero2 = int(input(f" Introduce segundo numero: "))


if numero1 < numero2:
    
    for x in range(numero1, (numero2 + 1)):
        if x%2 == 0:
            print(f"{x} Es par")
        else: 
            print(f"{x} Es inpar")
else:
    
     print("El numero 2 debe ser mayor al numero 1")
    
