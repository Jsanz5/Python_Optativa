# Imprime un mensaje en pantalla
print("hola python")

# -------------------------------------------
# Listas: Colecciones ordenadas y mutables
mi_lista = [1, "hola", 3.5, [4, 9]]  # Contiene diferentes tipos de datos, incluso otra lista
print(mi_lista)

# -------------------------------------------
# Tuplas: Colecciones ordenadas e inmutables
mi_tupla = (1, "hola", 3.5)
print(mi_tupla)

# -------------------------------------------
# Conjuntos (sets): Colecciones no ordenadas, sin duplicados
mi_conjunto = {1, 2, 3, 4, 5, 6, 6}  # El segundo 6 será ignorado
print(mi_conjunto)

# -------------------------------------------
# Mostrar el tipo de diferentes datos con type()
print(type("foajfowjof"))  # str (cadena de texto)
print(type(2))             # int (entero)
print(type(1.5))           # float (decimal)
print(type(True))          # bool (booleano)
print(type(3+1))           # int (resultado de suma de enteros)

# -------------------------------------------
# Variables de diferentes tipos
my_string_variable = "my_string_variable"
print(my_string_variable)

my_int_variable = 3
print(my_int_variable)

my_boolean_variable = True
print(my_boolean_variable)

# Imprime varias variables juntas
print(my_string_variable, my_int_variable, my_boolean_variable)

# -------------------------------------------
# Reasignación de variables
my_int_variable = 6  # Cambia el valor de la variable
print(my_int_variable)

# -------------------------------------------
# Conversión de tipo: de int a str
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))  # Verifica que ahora es str

# Imprime diferentes tipos en una sola línea
print(my_string_variable, type(my_int_variable), my_boolean_variable)

# -------------------------------------------
# Obtener longitud de una cadena
print(len(my_string_variable))  # Cuenta caracteres

# -------------------------------------------
# Asignación múltiple de variables
name, surname, alias, age = "Jowell", "Sanz", "M", "34"
print("Mi nombre es", name, surname, "y tengo", age, "años.")

# -------------------------------------------
# Entrada por teclado:
"""
first_name = input("Introduce tu nombre: ")
print("Tu nombre es:", first_name)
"""

# -------------------------------------------
# Cambio de tipo de una variable
print(type(name))  # str
name = 100         # Ahora es un entero
print(type(name))  # int

# -------------------------------------------
# Otro ejemplo de cambio de tipo
addres = str("Mi dirección")
print(type(addres))  # str

addres = 32
print(type(addres))  # int
