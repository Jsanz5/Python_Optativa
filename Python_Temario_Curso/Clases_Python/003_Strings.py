""" Longitud de un string """
my_strig ="Mi String"
my_other_string = "Mi Other String"
print(len(my_strig))
print(len(my_other_string))

""" Concatenación de strings """
print(my_strig + " " + my_other_string)
my_new_line_string = "Este es un string \ncon salto de línea"
print(my_new_line_string)

""" String con tabulación """
my_tab_string = "\tEste es un string con tabulación"
print(my_tab_string)

""" String Escape """

my_scape_string = "Este es un string \n escapado"
print(my_scape_string)

""" Formateo de cadenas """
name,surname,age = "Jc","Sanz",34

print("Hola soy" + " " + name + " " + surname + " y tengo " + str(age) + " años.")

print("Hola soy %s %s y tengo %d años." % (name,surname,age))

print("Hola soy {} {} y tengo {} años.".format(name,surname,age))

print(f"Hola soy {name} {surname} y tengo {age} años.")

"""Desempaquetado de caracteres en python"""
language = "Python"
a,b,c,d,e,f = language

print(a) #Muestra P
print(b) #Muestra y
print(c) #Muestra t
print(d) #Muestra h
print(e) #Muestra o
print(f) #Muestra n


"""Division (slicing) de strings(cadenas)"""

language = "Python"

language_slice = language[1:3] #Muestra desde la posición 1 hasta la 3 sin incluirla
print(language_slice)

language_slice = language[1:] #Muestra desde la posición 1 hasta el final
print(language_slice)

language_slice = language[-2:] #Muestra desde el inicio hasta la posición 2 sin incluirla
print(language_slice)


""" Reversed string """

reversed_language = language[::-1] #Muestra el string al revés
print(reversed_language)


""" Funciones de strings """

print(language.capitalize()) #Muestra "Python" con la primera letra en mayúscula
print(language.upper())      #Muestra "PYTHON" completamente en mayúsculas
print(language.count("t"))   #Muestra 1 porque la letra "t" aparece una vez en Python
print(language.isnumeric())  #Muestra False porque Python no es un número
print("1".isnumeric())       #Muestra True porque 1 es un número
print(language.lower())      #Muestra "python" en minúsculas
print(language.upper().isupper())  #Muestra True porque Python está completamente en mayúsculas
print(language.startswith("Py")) #Muestra True porque Python comienza con "Py"

