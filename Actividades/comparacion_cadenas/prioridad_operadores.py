# Usando Operador and

print(10 > 5 and 2 < 8)
print(7 == 7 and 3 != 4)
print(5 > 10 and 2 < 3)
print(5 < 3 or 2 < 4)
print((3 + 2 == 5) and (6 < 2))


# Usando Operador not

"""El operador not invierte el valor booleano de una expresión."""

print(not (5 > 3))        # esto es True, pero el not lo invierte a False.
print(not (2 == 2))       # esto es True, y el not lo invierte a False.
print(not (4 < 1))        # esto es False, y el not lo invierte a True.
print(not (7 != 7))       # esto es False, y el not lo invierte a True.
print(not (3 <= 5 and 1 < 0))  # esto es True, 1 < 0 es False, el and da False y el not lo invierte a True.