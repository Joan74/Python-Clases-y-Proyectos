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

def ahorcado():
    palabras = ["python", "programacion", "juego", "ordenador", "desarrollo"]
    palabra_secreta = random.choice(palabras)
    intentos = 5
    letras_adivinadas = []

    while intentos > 0:
        # Mostrar el dibujo del ahorcado
        dibujar_ahorcado(5 - intentos)

        # Mostrar el estado actual del juego
        palabra_mostrada = ""
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "
        print(palabra_mostrada)

        if palabra_mostrada == palabra_secreta:
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

        # Pedir al usuario una letra
        entrada = input("Ingresa una letra: ").lower()

        if len(entrada) != 1:
            print("Ingresa solo una letra válida.")
            continue

        letra_usuario = entrada

        if letra_usuario in letras_adivinadas:
            print("Ya has ingresado esa letra. ¡Intenta con otra!")
            continue

        if letra_usuario in palabra_secreta:
            letras_adivinadas.append(letra_usuario)
        else:
            intentos -= 1
            print("Letra incorrecta. Te quedan {} intentos.".format(intentos))

    if intentos == 0:
        dibujar_ahorcado(5)  # Dibujo final del ahorcado
        print("Lo siento, has perdido. La palabra correcta era '{}'.".format(palabra_secreta))

# Ejemplo de uso
print("Bienvenido al juego del ahorcado.")
ahorcado()
