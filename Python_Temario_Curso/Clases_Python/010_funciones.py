"""Una funcion es un bloque de codigo reutilizable que realiza una tarea especifica."""


def my_function():
    print("Esto es una función.")


my_function()  # Llamada a la función

# Las funciones permitn esjecuar la misma operacion con distintos valores si modificar el codigo intero


def sum_two_values(first_numbre, second_number):
    print(first_numbre + second_number)


sum_two_values(5, 7)  # Llamada a la función con argumentos 5 y 7
sum_two_values(54754, 71231)  # Llamada a la función con argumentos 54754 y 71231
sum_two_values(1.4, 5.2)  # es tipo float


sum_two_values("5", "7")  # concatena los strings "5" y "7"


def sum_two_values(first_numbre: int, second_number: int):
    print(first_numbre + second_number)


sum_two_values("5", "7")


# funciones con return


def sum_two_values_with_return(fisrt_value, second_value):
    return fisrt_value + second_value


sum_result = sum_two_values_with_return(10, 5)


my_result = sum_two_values_with_return(10, 5)
print(my_result)

# funciones con varios parametros y f string


def print_name(name, surname):
    print(f"{name} {surname}")


print_name("Joel", "Otoya")


# Eso es lo que realmente ocurre
def print_name(name, surname):
    print(f"{name} {surname}")


print_name(name="Joel", surname="Otoya")

# parametros con valor por defecto (que significa *text)


def pint_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


pint_name_with_default("Joel", "Otoya")


def print_nupper_texta(*texts):
    for text in texts:
        print(text.upper())


print_nupper_texta("Hola", "Python", "Profe Geraldine")


def print_nupper_texta(*texts):
    for text in texts:
        print(text.upper())
