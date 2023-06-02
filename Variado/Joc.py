import random
import time
import os
os.system("clear") 

print("---------------------------------------------")
print("Benvingut al PENJAT de objectes de la compra!")
print("---------------------------------------------")
time.sleep(2)

print("\nCom et dius?")
print()
nom = input()
time.sleep(2)

print(f"\n{nom.upper()}, ""ara et posaré espais buits de cada lletra i tindràs 5 intents per endevinar el nombre.")
time.sleep(2)

def jugar_ahorcado():
    palabras = ["pa", "llet", "aigua", "sal", "iogurt", "ous", "sucre", "patates", "gelats",
               "ketchup", "macarrons", "pernil", "formatge", "paper", "galetes", "cereals", "carn", "suc"]
    palabra = random.choice(palabras)
    intentos = 5
    letras_adivinadas = []
    dibujo = [
                                """             
                                   +---+
                                       |
                                       |
                                       |
                                      ===""",
                                """
                                   +---+
                                   O   |
                                       |
                                       |
                                      ===""",
                                """
                                   +---+
                                   O   |
                                   |   |
                                       |
                                      ===""",
                                """
                                   +---+
                                   O   |
                                  /|   |
                                       |
                                      ===""",
                                """
                                   +---+
                                   O   |
                                  /|\  |
                                       |
                                      ===""",
                                """
                                   +---+
                                   O   |
                                  /|\  |
                                  /    |
                                      ===""",
                                """
                                   +---+
                                   O   |
                                  /|\  |
                                  / \  |
                                      ==="""
    ]
    
    while intentos > 0:
        # Mostrar el dibujo actual del ahorcado
        mostrar_dibujo(dibujo, intentos)
        
        # Mostrar la palabra con las letras adivinadas y guiones bajos para las no adivinadas
        mostrar_palabra(palabra, letras_adivinadas)
        
        if palabra_adivinada(palabra, letras_adivinadas):
            print(f"¡Felicitats! {nom} ¡Has adivinat la paraula correcta!!!!!")
            break
        
        letra = input("\nAfegeix una lletra: ")
        
        if len(letra) != 1:
            print("Per favor, ingresa solament una lletra.")
            continue
        
        if letra in letras_adivinadas:
            print("lletra duplicada. Intenta un Altre.")
            continue
        
        if letra in palabra:
            letras_adivinadas.append(letra)
        else:
            print("Lletra incorrecta.")
            intentos -= 1
            print("Et queden {} intents.".format(intentos))
        
    if intentos == 0:
        # Mostrar el dibujo final del ahorcado
        mostrar_dibujo(dibujo, intentos)
        print("¡¡¡¡T´has quedat sense intents. La paraula correcta es ####'{}'####.".format(palabra))
    
    jugar_nuevamente = input("¿Vols Jugar un altre cop? (s/n): ")
    
    if jugar_nuevamente.lower() == "s":
        time.sleep(1)
        os.system("clear")
        jugar_ahorcado()
    else:
        print("¡Gracies per jugar! ¡Fins Aviat!")
        time.sleep(3)
        os.system("clear")

def mostrar_palabra(palabra, letras_adivinadas):
    for letra in palabra:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

def palabra_adivinada(palabra, letras_adivinadas):
    for letra in palabra:
        if letra not in letras_adivinadas:
            return False
    return True

def mostrar_dibujo(dibujo, intentos):
    print(dibujo[6 - intentos])

print("¡Benvingut al joc del Penjat!")
jugar_ahorcado()