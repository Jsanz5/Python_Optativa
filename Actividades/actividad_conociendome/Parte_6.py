""" Parte 6 - Reto de lógica
1.	Usa la edad que guardaste en la parte 1.
2.	Escribe un bloque de código que imprima un mensaje diferente según la edad:
o	Si la edad es menor de 18: muestra “Eres menor de edad”.
o	Si la edad es entre 18 y 30: muestra “Eres joven”.
o	Si es mayor de 30: muestra “Eres adulto”.
3.	Usa operadores lógicos (and, or) para combinar condiciones.
4.	Explica en un comentario qué hace tu código y por qué.
"""

from Parte_1 import edad

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad <= 30:
    print("Eres joven.")
else:
    print("Eres adulto.")