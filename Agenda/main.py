print("\n-----------------------------------------------------------------------------------------------------------------")
agenda = []
nuevo_contacto = ""
while nuevo_contacto != "parar":
    nuevo_contacto = input("Introduce el Nombre: ")
    nuevo_contacto = input("Introduce el Email: ")
    nuevo_contacto = int(input("Introduce Movil: "))
    agenda.append(nuevo_contacto)
    

    
for contac in agenda:
    print(f"{agenda.index(contac)+ 1}.{contac}")
print("\n")