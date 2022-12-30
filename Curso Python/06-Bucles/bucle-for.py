"""
# FOR

for variable in elemento_iterable (LISTA, RANGO ETC)
    BLOQUE INSTRUCCIONES 
Para cortar un bucle escribir break   


"""

contador = 0
resultado = 0


for contador in range(0, 5):
    print("voy por  el "+ str(contador))
    resultado = resultado + contador 
    # Es lo mismo resultado += contador

print(f"El resultado es: {resultado}")


# Ejemplo tablas de multipicar

print("\n############### EJEMPLO ###############")

numero_usuario = int(input("\n¿De que número quieres la tabla?: "))


if numero_usuario < 1:
    numero_usuario = 1
print(f"#### Tabla de multiplicar del numero: {numero_usuario} ####")
for numero_tabla in range(1, 11):
    
    # Ejemplo de prohibir un nuemro y parar bucle
    if numero_usuario == 9:
        print("No se puede ejecutar la tabla de 9 !!!")
        break

        print("\n")
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("\nMultiplicacion ejecutada:")
