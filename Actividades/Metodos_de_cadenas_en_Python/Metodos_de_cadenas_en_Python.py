"""Actividad - Métodos de cadenas en Python
Ojetivo: Practicar el uso de los métodos: capitalize(), upper(), count(), isnumeric(), lower(), isupper(), startswith()
Escribe un programa en Python que almacene una palabra en la variable language y muestre por pantalla la siguiente
información utilizando métodos de cadenas:

1.La palabra con la primera letra en mayúscula."""

language = "python"
print(language.capitalize())

"""2.La palabra completamente en mayúsculas."""

language = "python"
print(language.upper())

"""3.Cuántas veces aparece la letra en la palabra."""

language = "python"
print(language.count("t"))

"""4.Si la palabra está formada únicamente por números."""

language = "python"
print(language.isnumeric()) #Muestra False porque python no es un número

"""5.Una comprobación numérica usando el texto "1"."""

language = "1"
print(language.isnumeric()) #muestra True porque 1 es un número

"""6.La palabra en minúsculas."""

language = "PYTHON"
print(language.lower())

"""7.Si la palabra está completamente en mayúsculas."""

language = "PYTHON"
print(language.isupper()) #Muestra True porque PYTHON está completamente en mayúsculas

"""8.Si la palabra comienza con Nota: Todos los resultados deben mostrarse con print()."""

language = "Python"
print(language.startswith("py")) #Muestra True porque Python comienza con "Py"