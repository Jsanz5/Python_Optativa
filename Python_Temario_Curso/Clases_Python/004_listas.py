""" Listas en Python """

my_list = list()
my_other_list = []

print(len(my_list)) #muestra la longitud de la lista

my_list = [18,28,21,20,18] #se crea una lista con valores enteros
print(my_list)
print(len(my_list))

my_other_list = [34,"Jowell","Sanz"] #se crea una lista con valores de diferentes tipos
print(my_other_list)
print(len(my_other_list))

print(type(my_list)) #muestra el tipo de dato

print(my_other_list[0]) #accede al primer elemento de la lista
print(my_other_list[1]) #accede al segundo elemento de la lista
print(my_other_list[2]) #accede al tercer elemento de la lista

print(my_other_list[-1]) #accede al ultimo elemento de la lista
print(my_other_list[-2]) #accede al penultimo elemento de la lista

#print(my_other_list[4]) #intenta acceder a un indice que no existe, genera un error)

print(my_other_list.count("Jowell")) #cuenta cuantas veces aparece el elemento "Jowell" en la lista
print(my_list.count(18)) #cuenta cuantas veces aparece el elemento 18 en la lista

"""Desempaquetado de listas"""

name, age , surname = my_other_list
my_other_list[0], my_other_list[1] #asigna los valores de la lista a las variables correspondientes
print(name)

my_list = "Hola Python" #asigna una cadena de texto a la variable my_list
print(my_list)
print(type(my_list)) #muestra el tipo de dato (String)

"""Agregar elementos a una lista"""
my_other_list.append("Ilerna") #agrega un nuevo elemento al final de la lista
print(my_other_list)

"""Insertar elementos en una lista"""
my_other_list.insert(1,"Blue") #agrega un nuevo elemento en la posicion 1
print(my_other_list)

my_other_list[1] = "Red" #modifica el elemento en la posicion 1
print(my_other_list)

"""Eliminar elementos de una lista"""
my_list = [18,28,21,20,18] # Restaurar la lista de números antes de eliminar
my_list.remove(18) #elimina el elemento 18 de la lista
print(my_list)

print(my_list.pop()) #elimina el ultimo elemento de la lista y lo devuelve
print(my_list)

print(my_list.pop(2)) #elimina el elemento en la posicion 2 y lo devuelve
print(my_list)

"""Eliminar"""

del my_list[1] #elimina el elemento en la posicion 2
print(my_list)

my_list.clear() #elimina todos los elementos de la lista
print(my_list)

my_list = [18,28,21,20,18]
my_new_list = my_list.copy() #copia la lista en una nueva variable
print(my_list)
print(my_new_list)

my_new_list.reverse() #invierte el orden de los elementos en la lista
print(my_new_list)


my_new_list.sort() #ordena los elementos de la lista de menor a mayor
print(my_new_list)