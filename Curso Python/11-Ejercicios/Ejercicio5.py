"""
Crear un lista con el contenido de esta tabla

ACCION      AVENTURA            DEPORTES
GTA         CRASH                FIFA  22  
MATRIX      ASSINS               WRC
RESIDENT    PRINCE PERSIA        MOTOGP 22

"""

tabla = [
{
    "categoria": "ACCION",
    "juegos": ['GTA', 'MATRIX', 'RESIDENT']
},
{
    "categoria": "AVENTURA",
    "juegos": ['CRASH', 'ASSASINS', 'PRINCE OF PERSIA']
},
{
    "categoria": "DEPORTES",
    "juegos": ['FIFA 22', 'WRC', 'MOTOGP 22']
}
]
for categoria in tabla:
    print(f"------------{categoria['categoria']}------------")
    for juego in categoria['juegos']:
        print(juego)
