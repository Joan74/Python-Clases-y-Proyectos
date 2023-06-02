import random
import time
import os
os.system("clear")
# os.system("cls") Este es de Windowns
print("---------------------------------------------")
print("Benvingut al penjat de objectes de la compra!")
print("---------------------------------------------")
time.sleep(2)

print("\nCom et dius?")
print()
nom = input()
time.sleep(2)

print(f"\n{nom.upper()}, ""ara et posaré espais buits de cada lletra i tindràs 5 intents per endevinar el nombre.")
time.sleep(2)


def sortir():
    resposta = input("Vols Sortir?!!..(si/no): ")
    if resposta.lower() == "si":
        return True
    else:
        time.sleep(1)
        os.system("clear")
        altreparaula()


def dibujar_ahorcado(intents):
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
          /|\  |
               |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        =========''',
        '''
           +---+
           |   |
           O   |
          /|\  |
          / \  |
               |
        ========='''
    ]

    print(dibujo[intents])


altreparaula = 1

while altreparaula == 1:
    paraula = ["pa", "llet", "aigua", "sal", "iogurt", "ous", "sucre", "patates", "gelats",
               "ketchup", "macarrons", "pernil", "formatge", "paper", "galetes", "cereals", "carn", "suc"]
    paraula = random.choice(paraula)
    lletresendevinades = []
    intentsrestants = 5

    while intentsrestants > 0:
        paraulamostrada = ''.join(
            lletra if lletra in lletresendevinades else ' _' for lletra in paraula)
        print(paraulamostrada)
        dibujar_ahorcado(5 - intentsrestants)
        lletra = input("\nAfegeix una lletra: ")
        lletresendevinades.append(lletra)

        if lletra not in paraula:
            intentsrestants -= 1
            print("Lletra incorrecta. Et queden", intentsrestants, "intents.")
            print("\nLa paraula correcta era: " + paraula)
            sortir()
        elif set(lletresendevinades) == set(paraula):
            print("\nFelicitats", nom, "! La paraula era", paraula)
            time.sleep(2)
            sortir()
        elif intentsrestants == 0:
            print("\nHo sento,", nom, "t'has quedat sense intents :(")
            print("\nLa paraula correcta era: " + paraula)
            time.sleep(2)
            os.system("clear")
            sortir()
