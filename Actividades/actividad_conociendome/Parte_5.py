# Parte 1
nombre = "Jowell"
edad = 34
estudiante = False

if estudiante:
    soy_estudiante = "soy estudiante"
else:
    soy_estudiante = "no soy estudiante"

# Parte 2
gusto_1 = "Comer"
gusto_2 = "Cantar"
gusto_3 = "Bailar"
gustos = [gusto_1, gusto_2, gusto_3]

# Parte 3
comidas_favoritas = ("Arroz_Chaufa", "Arroz_Con_Pollo", "Tallarines_Rojos")

# Parte 4
numeros = {1, 2, 2, 3, 4, 4, 5}

# Parte 5 - Tipos de datos y resumen
print("Tipo de dato de 'nombre':", type(nombre))
print("Tipo de dato de 'gustos':", type(gustos))
print("Tipo de dato de 'comidas_favoritas':", type(comidas_favoritas))
print("Tipo de dato de 'numeros':", type(numeros))

# Crear lista resumen
resumen = [gustos, comidas_favoritas, numeros]

# Mostrar contenido de resumen
print("Contenido de la lista resumen:", resumen)

# Comentario
"""
Combinar distintos tipos de datos en una lista permite guardar información variada en un solo lugar, 
lo que hace el código más flexible y organizado.
"""