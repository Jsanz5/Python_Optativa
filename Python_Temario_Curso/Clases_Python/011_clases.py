# Las clases permiten organizar el codigo, reutilizarlo en diferentes partes del progrmama, y crear objetos con propiedades y comportamientos específicos.

# Definición de una clase
# tienen atributos, metodos y un constructor que pueden ser utilizados para crear objetos con características y comportamientos específicos.


class MyEmptyPerson:
    pass  # es ua alabra reservada para indicar que no se ha implementado nada en la clase, pero se puede usar para crear objetos de esta clase.


# las varibales, funciones y metodos, se escriben en minusculas, y si tienen varias palabras se separan por guion bajo, esto se llama snake_case.
# las clases se escriben en mayusculas, y si tienen varias palabras se separan por guion bajo, esto se llama CamelCase.

# Creación de un objeto a partir de la clase
# print(MyEmptyPerson)

# Creación de una clase con atributos y métodos
# print(MyEmptyPerson())

# uso de un constructor para inicializar los atributos de la clase


class Person:
    def __init__(self, name, surname):
        self.name = name  # el constructor se llama __init__ y se ejecuta automáticamente cuando se crea un objeto de la clase, recibe los parámetros necesarios para inicializar los atributos de la clase.
        self.surname = surname


# el metodo __init__ es un metodo especial que se ejecuta automáticamente cuando se crea un objeto de la clase, y se utiliza para inicializar los atributos de la clase.

# Uso de self para acceder a los atributos y métodos de la clase

"""
class Person:
    def __init__(self, name, surname):
        self.name = name # el atributo name se inicializa con el valor del parámetro name, y se accede a él a través de self.name
        self.surname = surname # el atributo surname se inicializa con el valor del parámetro surname, y se accede a él a través de self.surname
"""

# creación de un objeto

my_person = Person("Jowell", "Sanz")
print(
    f"{my_person.name} {my_person.surname}"
)  # se accede a los atributos name y surname a través del objeto my_person, utilizando la sintaxis my_person.name y my_person.surname.


# otro ejemplo


class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"  # se crea un nuevo atributo full_name que concatena el nombre y el apellido, y se accede a él a través de self.full_name

    def walk(self):
        print(
            f"{self.full_name} está caminando"
        )  # se accede al atributo full_name a través de self.full_name para mostrar el mensaje de que la persona está caminando.


# uso del objeto

my_person = Person("Jowell", "Sanz")
print(
    my_person.full_name
)  # se accede al atributo full_name a través del objeto para mostrar el nombre completo de la persona, utilizando la sintaxis my_person.full_name.

# esto ejecuta el metodo walk, que muestra el mensaje de que la persona está caminando, utilizando el atributo full_name para mostrar el nombre completo de la persona.
my_person.walk()  # se llama al método walk a través del objeto my_person, utilizando la sintaxis my_person.walk()


# modificacion de un atributo

my_person = Person("Jowell", "Sanz")
print(
    my_person.full_name
)  # se muestra el nombre completo de la persona, utilizando el atributo full_name a través del objeto my_person.

my_person.walk()  # se llama al método walk a través del objeto my_person, utilizando la sintaxis my_person.walk()

my_person.full_name = "Andres (el loco de los gatos)"  # se modifica el atributo full_name a través del objeto my_person, utilizando la sintaxis my_person.full_name = "nuevo valor"
print(
    my_person.full_name
)  # se muestra el nuevo valor del atributo full_name a través del objeto my_person, utilizando la sintaxis my_person.full_name

# este ejemplo demuestra cómo se puede modificar el valor de un atributo de un objeto después de que ha sido creado, y cómo se puede acceder al nuevo valor del atributo a través del objeto.
