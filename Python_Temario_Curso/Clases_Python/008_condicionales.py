# Condicionales en Python

# Son estructuras que permiten que el programa tome decisiones en función de si una condición es verdadera o falsa.
# La estructura básica de una condicional en Python es la siguiente:
# if condición:
#     bloque de código si la condición es verdadera
# else:
#     bloque de código si la condición es falsa
# También podemos usar elif (else if) para verificar múltiples condiciones:
# if condición1:
#     bloque de código si la condición1 es verdadera
# elif condición2:
#     bloque de código si la condición2 es verdadera
# else:
#     bloque de código si ninguna condición es verdadera
# Ejemplo de condicionales en Python

my_condition = True

if my_condition:
    print("Se ejecuta la condición if")  # Este bloque se ejecuta si my_condition es True

    print("La ejecución continúa")

# otro ejemplo

my_condition = 5 * 2 # Resultado 10

if my_condition == 11:
    print("Se ejecuta la condición del segundo if")

    # si la condicion se cumple, se ejecuta este bloque

my_condition = 5 * 2 # Resultado 10

if my_condition == 10:
    print("La ejecución continúa") # Este bloque se ejecuta si my_condition es 10

#  Si la condición no se cumple, se ejecuta el bloque else

if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")

    print("La ejecución continúa")

# Tambien se puede tener mas de una condiciones dentro de un if utilizando operadores logicos and, or y not

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

    print("La ejecución continúa")


# Elif es una condicion que se usa cuando queremos comprobar mas de una condicion, pero no queremos usar solo una de ellas

if my_condition > 10 and my_condition < 20: #  primero se evalua esta condicion
    print("Es mayor que 10 y menor que 20")

elif my_condition == 1: # si la primera condicion es falsa, se evalua esta segunda condicion
    print("Es igual a 1")
else: # si ninguna de las condiciones anteriores se cumple, se ejecuta este bloque
    print("Es menor o igual que 10 o mayor o igual que 20")
    
    print("La ejecución continúa")

# Strings vacios en condicionales

"""if my_string: ""
print("El string  está vacío")"""

my_string = "Mi cadena de texto"

if not my_string:
    print("Mi cadena de texto está vacío")

