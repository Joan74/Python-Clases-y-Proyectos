cantantes = ['Pecos', 'Julio Iglesias', 'Manzanita', 'Jose luis Perales']
numeros = [1, 2, 4, 8, 3, 5]

# Ordenar la lista
numeros.sort()  # ordena los numeros
# cantantes.sort() # Ordena alfabeticamente
print(numeros)


# Añadir elementos
cantantes.append('Ana Balen y Parrita')
# esta opcion hay que darle la posicion donde ira (1)
cantantes.insert(1, 'Peret')
#cantantes.sort() # Ordena alfabeticamente


# Eliminar elementos
cantantes.remove('Pecos') # Eliminar directamente quien quieres
#cantantes.pop(1)  # Eliminara el cantante que este en posision 1
#print(cantantes)

# Dar vuelta a una lista
print(numeros)
numeros.reverse() # dara la vuelta a los numeros
print(numeros)

# Buscar dentro de la lista

print('Julio Iglesias' in cantantes) # Devuelve un True ya que esta si no daria False

# Contar elementos
print(cantantes)
print(len(cantantes)) # Me dira el numero de cantantes que hay

# Cuantas veces aparece un elemento

print(numeros.count(8))

# Conseguir Indice
print(cantantes.index('Manzanita')) # Me dira cuantas veces esta en la lista

# Unir listas

cantantes.extend(numeros) # Unira cantantes y lista de numeros
print(cantantes)


