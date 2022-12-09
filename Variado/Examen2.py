from datetime import datetime  # Mostar fecha y hora
import os
import time #Importar tiempo
os.system("clear")
print("--------------------------")
now = datetime.now()
print(now)
print("--------------------------")
print()
nombre = input("Introduce tu nombre: ")
print()
print(
    f"Bienbenido/a {nombre}, Este examen constara de dos preguntas por categorias COMENZAMOS:")

opcion = 0
while True:
    print("""      
Elige categoria:

1- Naturales
2- Matematicas
3- Ciencia
4- Peliculas
5- Series
6- Salir
""")
    opcion = int(input(f"Elige una opción {nombre}: "))
    if opcion == 6:
        os.system("clear")
        exit()

    if opcion == 1: # NATURALES
        España = 1
        print(" \n         --------- Has elegido Naturales!!!!---------")
        print()
        print("¿Donde se encuentra España?")
        print()
        print("1- EEUU: ")
        print("2- Asia ")
        print("3- Europa ")
        print()
        opcion = int(input(f"Elige una opción {nombre}: "))
        if opcion == 3:
            print(f"\nCorrecto {nombre}, España esta en EUROPA!!!")
        else:
            print(f"\nIncorrecto {nombre}, España esta en EUROPA!!!")
        print()
        print("La capital de España es: ")
        print()
        print("1- Barcelona ")
        print("2- Madrid ")
        print("3- Andalucia")
        print("4- Pais Vasco")
        opcion = int(input(f"\nElige una opción {nombre}: "))

        if opcion == 2:
            print(f"\nCorrecto {nombre}, Madrid es la capital de España")
        else:
            print(f"\nIncorrecto {nombre}, Madrid es la capital de España")
        print()
        time.sleep(5.0) # Dara 5 segundos hasta ejecutar el siguiente comando
        os.system("clear")
    elif opcion == 2: # MATEMATICAS
        print()
        print(f" \n         --------- Has elegido Matematicas !!!!---------")
        print()
        print("La suma de 80 + 174 es:")
        print("-----------------------")
        print()
        print("1- 255")
        print("2- 354")
        print("3- 254")
        print("4- 286")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 3:
            print(f"\nCorrecto {nombre}, El resultado es 254!!!!")
        else:
            print(
                f"\nIncorrecto {nombre}, tienes que repasar la suma, el resultado es 254")
        print()

        print("La multipliacion de 20 x 30 es:")
        print("\n1- 700")
        print("2- 800")
        print("3- 600")
        print("4- 500")
        print()
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 3:
            print(f"\nCorrecto {nombre}, El resultado es 600!!!!!")
        else:
            print(f"\nIncorrecto {nombre}, el resultado es 600!!!")
        time.sleep(5.0)
        os.system("clear")
    elif opcion == 3: # CIENCIA
        print(f"\n         --------- Has elegido Ciencias!!!!---------")
        print()
        print("Cual es el tercer planeta de nuestro sistema solar: ")
        print()
        print("1- Marte")
        print("2- Venus")
        print("3- Tierra")
        print("4- Mercurio")
        print("5- Jupiter")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        print()
        if opcion == 3:
            print(f"Correcto {nombre}, La tierra es el tercer planeta")
        else:
            print(f"Incorrecto {nombre}, El tercer planeta es la tierra!!!!")
        print()
        print("¿Ha que distancia se encuentra el espacio sobre el nivel del mar?")
        print()
        print("1- 150 KM")
        print("2- 100 KM")
        print("3- 300 KM")
        print()
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 2:
            print(
                f"\nCorrecto {nombre}, El espacio comienza a 100 km del nivel del mar")
        else:
            print(
                f"\nIncorrecto {nombre}, El espacio comienza a 100 km del nivel del mar")
        time.sleep(5.0)
        os.system("clear")
    elif opcion == 4: # PELICULAS
        print(f"\n         --------- Has elegido Peliculas!!!---------")
        print()
        print("Cual es el nombre del actor de BLACK PANTHER:")
        print("\n1- Chadwick Boseman")
        print("2- Michael B. Jordan")
        print("3- Wiston Duke")
        print("4- John Kani")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 1:
            print(f"\nCorrecto {nombre}, El actor es Chadwick Boseman")
        else:
            print(f"\nIncorrecto {nombre}, El actor es Chadwick Boseman")

        print("\n¿En cuantas peliculas sale THOR?")
        print("\n1- 3")
        print("2- 4")
        print("3- 6")
        print("4- 8")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        print()
        if opcion == 3:
            print(f"""\nCorrecto {nombre}, sale en:                
Thor
Thor el mundo Oscuro
Thor Ragnarok
Thor Love thunder
Infinity war
End Game""")
        else:
            print(f"""\nIncorrecto {nombre}, Sale en:
Thor
Thor el mundo Oscuro
Thor Ragnarok
Thor Love thunder
Infinity war
End Game""")
        time.sleep(5.0)
        os.system("clear")
    elif opcion == 5: # SERIES
        print(f"\n         --------- Has elegido Series!!!!---------")
        print()
        print("En que serie sale el personaje de Wanda:")
        print("\n1- Loki")
        print("2- Bruja escarlata")
        print("3- Ms Marvel")
        print("4- Hawkeye")
        print("5- Moon knight")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        if opcion == 2:
            print(
                f"\nCorrecto {nombre}, Wanda protagonizo La bruja escarlata ")
        else:
            print(
                f"\nIncorrecto {nombre}, Wanda protagonizo La bruja escarlata ")
        print("\n En la serie Moon Knight, cuantos personalidades tiene el actor pricipal")
        print("\n1- Marc Spector")
        print("2- Marc Spector + Steven Grant")
        print("3- Super mario + Steven Grant")
        print("4- Steven Grant + Marc Spector + Jake Lockley")
        opcion = int(input(f"\nElige una opción {nombre}: "))
        print()
        if opcion == 4:
            print(f"""Correcto {nombre}, Tiene 3 personalidades:
Steven Grant
Marc Spector
Jake Lockley""")
        else:
            print(f"""Incorrecto {nombre}, Tiene 3 personalidades:
Steven Grant
Marc Spector
Jake Lockley""")
        time.sleep(5.0)
        os.system("clear")
