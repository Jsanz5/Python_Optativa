# Clase Tuplas

my_tuple = tuple() # creo una tupla vacía
my_other_tuple = () # otra forma de crear una tupla vacía

my_tuple = (34,"Joel","Sanz", 1.70) # Definición de una tupla

print(my_tuple) # Imprime la tupla completa
print(type(my_tuple)) # Imprime el tipo de dato (tupla)

print(my_tuple[0]) # Imprime el primer elemento de la tupla
print(my_tuple[-1]) # Imprime el último elemento de la tupla


# esto no es un tupla, es una lista
"""
my_tuple = [34,"Joel","Sanz"] # Cambio de tupla a lista
print(type(my_tuple)) # Imprime el tipo de dato (lista )"""


# metodo count para contar elementos
print(my_tuple.count("Joel")) # Cuenta cuántas veces aparece "Joel" en la tupla

# metodo index para identificar la posición de un elemento
print(my_tuple.index("Joel")) # Devuelve el índice de "Joel" en la tupla
print(my_tuple.index("Sanz")) # Devuelve el índice de "Sanz" en la tupla


""" metodo count e index no funcionan si el elemento no existe en la tupla,
pues no se pueden modificar en una tupla, ya que son inmutables

my_tuple[1]= 1.70
print(my_tuple)
"""

# Concatenación de tuplas
"""
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)"""


# Convertir tupla en lista
my_tuple = list(my_tuple) # convierto la tupla en lista
print(type(my_tuple)) # Imprime el tipo de dato (lista )

my_tuple [2] = "Ilerna" # Modifico un elemento de la lista
my_tuple.insert(4,"Estudiante") # inserto un nuevo elemento en la lista
print(my_tuple) # Imprimo la lista modificada


my_tuple = tuple(my_tuple)
print(my_tuple) # Imprime la tupla modificada
print(type(my_tuple)) # Imprime el tipo de dato (tupla )


"""
# eliminar elementos de la lista

del my_tuple[4] # da error, se debe eliminar todo el elemento
print(my_tuple) # Imprime la tupla modificada

"""

