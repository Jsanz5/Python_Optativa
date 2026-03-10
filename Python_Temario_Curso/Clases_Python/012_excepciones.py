# Excepciones en Python

"""esto genera error ya que sumar un número (int) con una cadena de texto (str)
no es posible, arrojará error de tipo (TypeError)"""

numberOne = 5
numberTwo = 1
# numberTwo = "1"

print(numberOne + numberTwo)  # Arroja error de tipo (TypeError)

# try exept#
try:
    print(numberOne + int(numberTwo))
    print("No se ha producido un error")

# se ejecuta si se produce una exepción
except:
    print("Se ha producido un error")

# try exept else#

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except:
    # se ejecuta si se produce una exepción
    print("Se ha producido un error")

else:
    # se ejecuta si no se ejecuta una exepción
    print("La ejecución continúa correctamente")

finally:
    # se ejecuta siempre
    print("Fin del bloque de control de excepciones")
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")

except:
    # se ejecuta si se produce una exepción
    print("Se ha producido un error")

else:
    # se ejecuta si no se ejecuta una exepción
    print("La ejecución continúa correctamente")

finally:
    # se ejecuta siempre
    print("Fin del bloque de control de excepciones")
    # Excepciones por tipo
try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:
    print("Se ha producido un ValueError")
except TypeError:
    print("Se ha producido un TypeError")

# Captura de la información de la excepción

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as my_random_error_name:
    print(my_random_error_name)
