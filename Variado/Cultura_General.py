import os
os.system("clear")
print("\n")
aciertos = 0
fallos = 0
opcion = 0

print("                   --------------------------------------------------------------")
print("                   -                                                            -")
print("                   -                 TEST CULTURA GENERAL                       -")
print("                   -                                                            -")
print("                   --------------------------------------------------------------")
print("\n")
print("ESTE TEST CONSTARA DE 10 PREGUNTAS")
print("---------------------------------------")
print("\n")
nombre = input("Introduce tu nombre para comenzar: ")
print(f"\nDe acuerdo {nombre.upper()} vamos a comenzar.........")
print("\n(1.) ¿CUALES SON LOS CINCO TIPOS DE SABORES PRIMARIOS?")
print("---------------------------------------------")
print("\n1- Dulce,Amrago,Salado,Caliente y Frio")
print("\n2- Amargo,Acido,Caliente,Frio y Dulce")
print("\n3- Dulce, Amargo, Salado, Acido y Umami")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 3:
    aciertos += 1
    print()
    print("""CORRECTO...El gusto es uno de nuestros cinco sentidos. Los sabores primarios son dulce, amargo, ácido, 
            salado y umami.""")
else:
    fallos += 1
    print()
    print("""INCORRECTO...El gusto es uno de nuestros cinco sentidos. Los sabores primarios son dulce, amargo, ácido, 
             salado y umami.""")

print("\n(2.) ¿CUAL ES EL LUGAR MAS FRIO DE LA TIERRA?:")
print("---------------------------------------------")
print("\n1- Groelandia")
print("\n2- Russia")
print("\n3- Antartida")
print("\n4- Alaska")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 3:
    aciertos += 1
    print("\nCORRECTO...La Antártida, que está cubierta de capas con un espesor de entre dos mil y tres mil metros")
else:
    fallos += 1
    print("\nINCORRECTO...La Antártida, que está cubierta de capas con un espesor de entre dos mil y tres mil metros")
print("\n(3.) ¿QUIEN ESCRIBIO LA ODISEA?:")
print("---------------------------------------------")
print("\n1. Gustavo Adolfo Vequer")
print("\n2. Antonio Machado")
print("\n3. Homero")
print("\n4. Camilo Jose Cela")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 3:
    aciertos += 1
    print("\nCORRECTO...Este poema de 24 cantos fue escrito por Homero.")
else:
    fallos += 1
    print("\nINCORRECTO...Este poema de 24 cantos fue escrito por Homero.")
print("\n(4.) ¿COMO SE LLAMA LA CAPITAL DE MONGOLIA?:")
print("---------------------------------------------")
print("\n1. Kathuma")
print("\n2. Ulan Bator")
print("\n3. kenia")
print("\n4. Thala")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 2:
    aciertos += 1
    print()
    print("""CORRECTO...La capital de Mongolia es Ulan Bator. El cociente intelectual (CI) 
         medio de los habitantes de este país está entre los 10 más altos del mundo""")
else:
    fallos += 1
    print()
    print("""INCORRECTO...La capital de Mongolia es Ulan Bator. El cociente intelectual (CI) 
         medio de los habitantes de este país está entre los 10 más altos del mundo """)
print("\n(5). ¿CUAL ES EL RIO MAS LARGO DEL MUNDO?:")
print("---------------------------------------------")
print("\n1. Nilo")
print("\n2. Cairo")
print("\n3. Amazonas")
print("\n5. Ebro")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 3:
    aciertos += 1
    print("\nCORRECTO...Aunque algunos pueden creer que es el Nilo… en realidad es el Amazonas.")
else:
    fallos += 1
    print("\nINCORRECTO...Aunque algunos pueden creer que es el Nilo… en realidad es el Amazonas.")
print("\n(6.) ¿COMO SE LLAMABA LA REINA DEL REINO UNIDO?:")
print("---------------------------------------------")
print("\n1. Isabel I")
print("\n2. Isabel II")
print("\n3. Isabel III")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 2:
    aciertos += 1
    print("\nCORRECTO...La monarca británica se llamaba Isabel II.")
else:
    fallos += 1
    print("\nINCORRECTO...La monarca británica se llamaba Isabel II.")
print("\n(7.) ¿EN QUE CONTINENTE SE ENCUENTRA ECUADOR?:")
print("---------------------------------------------")
print("\n1. Europa")
print("\n2. Oceania")
print("\n3. America")
print("\n4. Antartida")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 3:
    aciertos += 1
    print("\nCORRECTO...Ecuador es un país latinoamericano y, por tanto, se encuentra en América.")
else:
    fallos += 1
    print("\nINCORRECTO..Ecuador es un país latinoamericano y, por tanto, se encuentra en América.")
print("\n(8.) ¿DONDE SE ORIGINARON LOS JUEGOS OLIMPICOS?")
print("---------------------------------------------")
print("\n1. Atenas")
print("\n2. Volos")
print("\n3. Salonica")
print("\n4. Grecia")
print("\n5. Olimpia")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 4:
    aciertos += 1
    print("\nCORRECTO...Se originaron en Grecia. Se llaman así porque se celebraban en la ciudad de Olimpia.")
else:
    fallos += 1
    print("\nINCORRECTO...Se originaron en Grecia. Se llaman así porque se celebraban en la ciudad de Olimpia.")
print("\n(9.)¿QUE TIPO DE ANIMAL ES LA BALLENA?:")
print("---------------------------------------------")
print("\n1. Peces")
print("\n2. Poriferos")
print("\n3. Rotiferos")
print("\n4. Mamiferos")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 4:
    aciertos += 1
    print("\nCORRECTO...La ballena es un mamífero marino de hasta 30 metros de longitud.")
else:
    fallos += 1
    print("\nINCORRECTO...La ballena es un mamífero marino de hasta 30 metros de longitud.")
print("\n(10.) ¿CUANDO SE ACABO LA II GUERRA MUNDIAL? ")
print("---------------------------------------------")
print("\n1. 1945")
print("\n2. 1954")
print("\n3. 1951")
print("\n5. 1940")
opcion = int(input(f"\nElige una opción {nombre.upper()}: "))
if opcion == 1:
    aciertos += 1
    print("\nCORRECTO...La II Guerra Mundial finalizó en 1945.")
else:
    fallos += 1
    print("\nINCORRECTO...La II Guerra Mundial finalizó en 1945.")

print("\nRESULTADO DE PREGUNTAS:")
print("-------------------------")
print(f"\nPREGUNTAS ACERTADAS: {aciertos}")
print(f"\nPREGUNTAS FALLADAS: {fallos}")
if aciertos <= 4:
    print(f"\nHAS SUSPENDIDO EL TEST {nombre.upper()} ")
    print("-------------------------------")
    print()
    print()

else:
    print(f"\nHAS APROVADO EL TEST {nombre.upper()}")
    print("-------------------------------")
    print()
    print()
