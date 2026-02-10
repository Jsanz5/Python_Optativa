# sets o elementos python

my_set = set() # creo un set vacío
my_other_set = {} # otra forma de crear un set vacío, pero en realidad es un diccionario

print(type(my_set)) # Imprime el tipo de dato (set)
print(type(my_other_set)) # Imprime el tipo de dato (diccionario)

my_other_set = {"Joel", 34, 1.70, "Sanz"}
print(type(my_other_set)) # Imprime el tipo de dato (set)

"""
[] se usa para listas
() se usa para tuplas
{} se usa para sets o diccionarios

"""

print(len(my_other_set)) # Imprime cuantos objetos hay en el set

# diferencias entre sets, listas y tuplas

my_other_set.add("Carles") # añade un nuevo elemento al set
print(my_other_set) # Imprime el set con el nuevo elemento añadido


# los SETS no permiten elementos repetidos
my_other_set = {"Joel", 34, 1.70, "Sanz", "Joel", 34}
print(type(my_other_set)) # Imprime el set sin elementos repetidos
my_other_set.add("Sanz") # intenta añadir un elemento repetido
print(my_other_set) # Imprime el set sin elementos repetidos


# Los SETS no mantienen un orden específico por lo que no garantizan el orden de los elementos
print("Joel" in my_other_set) # Verifica si "Joel" está en el set (devuelve True o False
print("Sanz" in my_other_set) # Verifica si "Carles" está en el set (devuelve True o False


# Eliminar SETS
my_other_set = {"Joel", 34, 1.70, "Sanz", "Carles"}
my_other_set.remove("Carles") # Elimina el elemento "Carles" del set
print(my_other_set) # Imprime el set sin el elemento "Carles"

# para eliminar todos los elementos del set
my_other_set.clear() # Elimina todos los elementos del set por completo
print(my_other_set) # Imprime el set vacío

""" para eliminar por completo el set
my_other_set = {"Joel", 34, 1.70, "Sanz", "Carles"}
del my_other_set # Elimina el set por completo
print(my_other_set) # Da error porque el set ya no existe"""

my_set = {"Joel", "Sanz", 1.70}
my_list = list(my_set)  # convierto el set en lista
print(type(my_list)) # Imprime el tipo de dato (lista )
print(my_list) # Imprime la lista convertida desde el set

# para unir conjuntos de sets
my_other_set = {"Carles", "Ilerna"}
my_new_set = my_set.union(my_other_set) # une dos sets en uno nuevo
print(my_new_set) # Imprime el set resultante de la unión

