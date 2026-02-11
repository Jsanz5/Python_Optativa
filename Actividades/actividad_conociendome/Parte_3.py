# Parte 3 – Comidas favoritas

# 1. Crear la tupla con tres comidas que te gusten mucho.
comidas_favoritas = ("Arroz_Chaufa", "Arroz_Con_Pollo", "Tallarines_Rojos")

# 2. Mostrar la tupla completa
print("Mis comidas favoritas son:", comidas_favoritas)

# 3. Intentar cambiar uno de los valores de la tupla (solo como experimento).
#comidas_favoritas[2] = "Ceviche"

# Comentario sobre el error:
# Esto me da un error porque las tuplas en Python son inmutables.
# No se pueden modificar sus valores una vez hayan sido creadas.
# El error que aparece es: TypeError: 'tuple' object does not support item assignment

# 4. Usa len() para contar cuántas comidas hay en la tupla.
cantidad_comidas = len(comidas_favoritas)
print("Cantidad de comidas en la tupla:", cantidad_comidas)
