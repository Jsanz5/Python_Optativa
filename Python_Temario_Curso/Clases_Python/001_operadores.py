# Ejercicios Operaciones Aritméticas y de Cadenas

print(3 + 4)        # Suma de 3 y 4
print(3 - 4)        # Resta de 3 menos 4
print(3 * 4)        # Multiplicación de 3 por 4
print(3 / 4)        # División de 3 entre 4

print(3 % 4)        # Módulo: residuo de 3 entre 4
print(10 % 3)       # Módulo: residuo de 10 entre 3

print(10 // 3)      # División entera: cuántas veces cabe 3 en 10 sin decimales

print(2 ** 3)       # Potencia: 2 elevado a la 3

print("Hola "+ "python.")      # Concatenación de dos cadenas de texto

#print("Hola"-"python.")       # Inválido: no se puede restar cadenas (por eso está comentado)
#print("Hola"*"python.")       # Inválido: no se puede multiplicar una cadena por otra cadena (comentado)
#print("Hola" + 5)             # Inválido: no se puede concatenar cadena con número directamente (comentado)
print("Hola " + str(5))        # STR Convierte el número 5 a cadena y luego lo concatena con "Hola "
print("Hola " * 5)             # Repite la cadena "Hola " cinco veces

#print("Hola " * 2.5)
print("Hola " * int(2.5))

my_float = 2.5 * 2
print("Hola " * int(my_float))