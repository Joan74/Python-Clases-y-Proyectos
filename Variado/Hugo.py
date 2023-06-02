import time
import os
os.system("clear")
import random

def dibujar_ahorcado(intentos):
    dibujo = [
        '''
           +---+
           |   |
               |
               |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
               |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        ========='''
    ]

    print(dibujo[intentos])

print("Benvingut al penjat de objectes de la compra!\n")
time.sleep(1)

print("Com et dius?\n")
nom = input()
time.sleep(1)

print("\n", nom, "ara et posaré espais buits de cada lletra i tindràs 5 intents per endevinar el nombre.\n")
time.sleep(1)


def ahorcado():
    paraula = ["pa", "llet", "aigua", "sal", "iogurt", "ous", "sucre", "patates", "gelats", "ketchup", "macarrons", "pernil", "formatge", "paper", "galetes", "cereals", "carn", "suc"]
    paraula_secreta = random.choice(paraula)
    lletresendevinades = []
    intentsrestants = 5
    print(paraula)

while True:      
    
    while intentsrestants > 0:
        paraulamostrada = ''.join(lletra if lletra in lletresendevinades else ' _' for lletra in paraula)
        print(paraulamostrada)

        lletra = input("\nAfegeix una lletra: ")
        lletresendevinades.append(lletra)

        if lletra not in paraula:
            intentsrestants -= 1
            print("Lletra incorrecta. Et queden", intentsrestants, "intents.")
        elif intentsrestants == 0:
             print("T'has quedat perdut,", nom, ". La paraula era", paraula)
        elif intentsrestants == 0:
            print("\nHo sento,", nom, "t'has quedat sense intents :(")
            time.sleep(0.5)
            print("\nLa paraula correcta era: " + paraula)
        elif lletresendevinades == paraula_secreta:
            print("\nFelicitats", nom, "! La paraula era", paraula)
            time.sleep(2)
            os.system("clear")
            print("¿Vols Sortir? (si/no)")

            respuesta = input()
        elif respuesta == "si":
            print("Fins Aviat!!!!")
            time.sleep(0.5)
            os.system("clear")
            break
        else:
            print("Juguem un altre vegada!!!...")
            time.sleep(0.5)
            os.system("clear")
            

            