"""
Diccionario:
Un tipo de dato  que almacena un conjunto de datos.
en formato clave > valor.
Es parecido a un array asociativo o un objeto jason
"""

persona = {
    "nombre": "Juan Manuel",
    "apellidos": "Barrio Sanchez",
    "Email": "Joan151006@gmail.com"
}
print(persona)
print(persona["apellidos"])  # acceder a uno en concreto

# Lista con diccionarios

contactos = [
    {                                       # Indice 0
        'Nombre': 'Juan Manuel',
        'Email': 'Joan151006@gmail.com'
    },
    {                                           # Indice 1
        'Nombre': 'Marga',
        'Email': 'margagil1974@gmail.com'
    },
    {                                           # Indice 2
        'Nombre': 'Arnau',
        'Email': 'Arnaubarriogil@gmail.com'
    }
]
print(contactos)
print(contactos[0]['Nombre'])  # mostrara el indice 0 y el nombre
print(contactos[1]['Nombre'])  # mostrara el indice 1 y el nombre
print(contactos[2]['Nombre'])  # mostrara el indice 2 y el nombre
#contactos[0]['Nombre'] = "Papa"  # Cambiara el nombre
print(contactos[0]['Nombre'])  # mostrara el indice 0 y el nombre cambiado

# Mostar listado completo

print("\nListado de contactos")
print("-----------------------------------------------")
for contacto in contactos:
    print(f'Nombre del contacto: {contacto["Nombre"]}')
    print(f'Email  del contacto: {contacto["Email"]}')
    print("-----------------------------------------------")
    print()