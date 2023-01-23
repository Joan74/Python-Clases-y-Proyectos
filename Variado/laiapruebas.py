juegos = [
    "Fornite","NFS","Crash"
]

print(juegos)

nuevo_juego = ""
while nuevo_juego != "parar":
    nuevo_juego = input("Introduce nuevo juego: ")
    if nuevo_juego != "parar":
        juegos.append(nuevo_juego)
for pelicula in juegos:
    print(pelicula)


# print("\n******************** CONTACTOS *********************")

# contactos = [
#    [ 
#         'Laia',
#         'LaiaGilMuños@icloud.com'

#    ],
#    [
#         'Juanma',
#         'joan151006@gmail.com'
#    ]
# ]

# for contacto in contactos:
#     for elemento in contacto:
#         if contacto.index(elemento) == 0:
#             print("Nombre: " + elemento)
       
#         else:
#             print("Email: " + elemento)
#     print()













