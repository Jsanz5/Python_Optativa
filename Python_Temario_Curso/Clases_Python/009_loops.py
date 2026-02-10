""" Los loops o bucles son estructuras que permiten repetir un bloque de codigo varias veces
mientras se cumpla una condicion o mientras hayan elementos que rrecorrer. En Python, los loops mas comunes son 'for' y 'while'."""

"""
my_condition = 0

while my_condition < 10:
 print(my_condition) # este es un bucle infinito

"""
# Ejemplo con 'while'
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2  # Incrementamos la condicion para evitar un bucle infinito de 2 en 2

# en python se puede usar else con los bucles
else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucon continua")

# Ejemplo uso de while seguido de if

my_condition = 0

while my_condition < 10:
    print(my_condition)

    my_condition += 2

    if my_condition == 10:
        print("mi condicion es igual a 10")
    else:
        print("mi condiciones es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print("mi condiciones es 15")

        print("La ejecucion continua")

# Detener con break

while my_condition < 20:
    my_condition += 1

    if my_condition == 15:
        print("se detiene la ejecucion del bucle")
        break

    print(my_condition)

print("La ejecucion continua")

# Bucle for -> este se ejecuta un numero determinado de veces, permite reccorree set, listas, tuplas, diccionarios

my_list = [35, 24, 62, 52, 12]
for element in my_list:
    print(element)

my_set = {"Jowell", "Otoya", 35}
for element in my_set:
    print(element)

my_tuple = (35,1.70, "Jowell", "Otoya")
for element in my_tuple:
    print(element)

# Los diccionarios solo imprimen las claves no los valores

my_dict = {
    "Nombre": "Jowell",
    "Apellido": "Otoya",
    "Edad": 35
}

for element in my_dict:
    print(element)

# si se desea recorrer unicamente los valores del diccionario se usa el metodo .values()

for element in my_dict.values():
    print(element)
else:
    print("Se han recorrido todos los elementos del diccionario")

# para recorrer tanto claves como valores se usa el metodo .items()

for key, value in my_dict.items(): # para recorrer tanto claves como valores
    print(f"Clave: {key} - Valor: {value}") # imprime clave y valor

# uso de for, continue y eslse en diccionarios

for element in my_dict:
    print(element)

    if element == "Edad":
     continue
else:
    print("El bule for para diccionarios ha finalizado")

# lo que realmente hace continue dentro de un bucle es no procesar el mismo elemento, salta inmediatamente al la siguiente iteracion del bucle for