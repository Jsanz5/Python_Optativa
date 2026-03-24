import math
from math import pi
from math import pi as PI_VALUE

import my_module
from my_module import printValue, sum

my_module.sum(5, 3, 1)  # Llamada a la función sum del módulo con argumentos 5, 3 y 1
my_module.printValue("Hello, Python!")


sum(1, 2, 3)  # Llamada a la función sum del módulo con argumentos 1, 2 y 3
printValue("Hello, Python!")

print(math.pi)  # Imprime el valor de pi utilizando el módulo math
print(
    math.pow(2, 8)
)  # Imprime el resultado de 2 elevado a la potencia de 8 utilizando el módulo math

print(pi)  # Imprime el valor de pi utilizando la importación directa del módulo math

print(
    PI_VALUE
)  # Imprime el valor de pi utilizando la importación con alias del módulo math
