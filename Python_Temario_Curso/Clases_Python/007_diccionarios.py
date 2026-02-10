# La clave y el valor pueden ser de cualquier tipo de dato
# Se puede crear incluso un valor set ya que puede ser de cualquier tipo de dato
# Una de las ventajas de los diccionarios es que permite acceder directamente a los valores mediante sus claves.
# Si queremos cambiar el valor aosciado a una clave, simpmenete asignamos un nuevo valor usando la misma clave.


# creacion de construcor dict()

my_dict = dict() # creo un diccionario vacío
print(type(my_dict))

my_other_dict = {} # otra forma de crear un diccionario vacío
print(type(my_other_dict)) # Imprime el tipo de dato (diccionario)


my_other_dict = {
"Nombre": "Joel",
"Apellido": "Sanz",
"Edad": 34,
1: "Python" } # Definición de un diccionario
print(type(my_other_dict)) # Imprime el tipo de dato (diccionario)

my_dict = {
"Nombre": "Joel",
"Apellido": "Sanz",
"Edad": 34,
"Lenguajes": {"Python", "Java", "C++"} } # Definición de un diccionario
print(type(my_dict)) # Imprime el tipo de dato (diccionario)

print(my_other_dict) # Imprime el diccionario completo
print(my_dict) # Imprime el diccionario completo


# la funcion len() cuenta el número de claves-valor en el diccionario
print(len(my_other_dict)) # Imprime cuantos pares clave-valor hay en el diccionario
print(len(my_dict)) # Imprime cuantos pares clave-valor hay en el diccionario

print(my_other_dict["Nombre"]) # Imprime el valor asociado a la clave "Nombre"

my_dict["Nombre"] = "Carles" # Modifico el valor asociado a la clave "Nombre"
print(my_dict["Nombre"]) # Imprime el valor modificado asociado a la clave "Nombre

# para agregar una nueva clave con su valor a un diccionario, simplemente asignamos un valor a una nueva clave

my_dict["Calle"] = "Calle nou" # Agrego una nueva clave-valor al diccionario
print(my_dict) # Imprime el diccionario con la nueva clave-valor añadida


# para eliminar una clave-valor del diccionario, usamos la palabra reservada del junto con la clave que queremos eliminar

del my_dict["Calle"] # Elimina la clave-valor "Calle" del diccionario
print(my_dict) # Imprime el diccionario sin la clave-valor "Calle"


# Si usamos IN en un diccionario, Python verifica si la clave existe en el diccionario
print("Joel" in my_dict) # Verifica si la clave "Joel" está en el diccionario (devuelve True o False)
print("Nombre" in my_dict) # Verifica si la clave "Nombre" está en el diccionario (devuelve True o False)

# metodos en los diccionarios

print(my_dict.items()) # Imprime todos los pares clave-valor del diccionario
print(my_dict.keys()) # Imprime todas las claves del diccionario
print(my_dict.values()) # Imprime solo los valores del diccionario

""" metodo fromkeys() es un metodo de clase que crea un nuevo diccionario
 a partir de una secuencia de claves y un valor por defecto"""

# puede ser util usarlos cuando queremos inicializar un diccionario con claves predefinidas y valores por defecto
my_new_dict = my_other_dict.fromkeys(("Nombre", 1)) # Crea un nuevo diccionario con las claves "Nombre" y 1, y valores por defecto None
print(my_new_dict) # Imprime el nuevo diccionario creado con fromkeys()

my_new_dict = dict.fromkeys(my_dict) # Crea un nuevo diccionario con las mismas claves que my_dict y valores por defecto None
print(my_new_dict) # Imprime el nuevo diccionario creado con fromkeys()

my_new_dict = dict.fromkeys(my_dict,"Joel") # Crea un nuevo diccionario con las mismas claves que my_dict y el valor por defecto "Joel"
print(my_new_dict) # Imprime el nuevo diccionario creado con fromkeys() y valor
