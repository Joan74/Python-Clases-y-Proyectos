
"""
Hacer un programa indefinido has que usuario introduzca
el numero 111



"""
contador = 1

while contador < 100:

    numero_usuario = int(input(f"Introduce un numero: "))
                    
    if numero_usuario == 111:
        break
        
    else:    
        
        print(f"Has introducido: {numero_usuario}")
        