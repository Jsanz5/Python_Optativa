# Parte 1 – Datos personales

# 1. Crea tres variables para guardar:

nombre = "Jowell"
edad = 34
estudiante = True

if estudiante:
    soy_estudiante = "soy estudiante"
else: 
    soy_estudiante = "no soy estudiante"

"""
Este bloque solo controla si se ejecuta o no el código que está adentro, 
pero no limita el acceso a variables definidas en el mismo archivo. 
Por eso, cuando se ejecute ese bloque, puede usar y mostrar sin problema esas variables.
"""
if __name__ == "__main__":
    print(
        "Hola soy " + nombre + "," + " tengo " + str(edad) + 
        " años " + "y actualmente " + str(soy_estudiante) + " del curso Daw."
    )

    print(type(nombre))
    print(type(edad))
    print(type(estudiante))
