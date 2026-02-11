#Parte 4 – Conjunto de números

#1.	Crea un conjunto (set) llamado números con algunos números repetidos, por ejemplo:
#2.	numeros = {1, 2, 2, 3, 4, 4, 5}
#3.	Muestra el conjunto en pantalla y observa qué sucede con los valores duplicados. 

numeros = {1, 2, 2, 3, 4, 4, 5}
print(numeros)

#4.	Agrega otro número al conjunto reescribiendo la variable, por ejemplo:
#5.	numeros = numeros | {6}
#6.	Muestra nuevamente el conjunto y observa el cambio.

numeros = numeros | {6}
print(numeros)

numeros = numeros | {6,7,8,9,10}
print(numeros)

#7.	Escribe un comentario explicando por qué los valores repetidos no aparecen más de una vez.

# Los valores repetidos no aparecen más de una vez en un set porque este solo almacena elementos únicos. 
# Si se añade un valor que ya existe, se ignora automáticamente