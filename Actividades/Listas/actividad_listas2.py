"""1. Crea un nuevo archivo en tu entorno de trabajo llamado actividad_listas2.py."""

"""""
2. Declara una lista llamada precios que contenga al menos seis valores
numéricos (pueden representar precios de productos o servicios).
o Asegúrate de incluir al menos un valor repetido."""

precios = ["luz","internet",28,18,21,28]
print(precios)


"""
3. Crea otra lista llamada empleado con cuatro datos distintos:
o nombre, edad, puesto de trabajo y ciudad.
(Ejemplo: [&quot;Lucía&quot;, 29, &quot;Diseñadora&quot;, &quot;Barcelona&quot;])"""

empleado = ["Ana",30,"Ingeniera","Madrid"]
print(empleado)


"""
4. Analiza las listas:
o Muestra ambas listas con print().
o Usa len() para mostrar cuántos elementos tiene cada lista.
o Usa type() para verificar el tipo de dato."""

print(precios)
print(len(precios))
print(type(precios))

print(empleado)
print(len(empleado))
print(type(empleado))


"""
5. Accede a elementos específicos:
o Muestra el primer, tercer y último elemento de la lista empleado.
o Usa índices negativos para acceder al penúltimo elemento."""


print(empleado[0])
print(empleado[2])
print(empleado[-1])
print(empleado[-2])


"""
6. Actualiza información:
o Cambia la ciudad o el puesto de trabajo del empleado.
o Agrega un nuevo elemento con .append() (por ejemplo, un
departamento o área).
o Inserta un nuevo dato en la segunda posición con .insert() (por
ejemplo, un número de empleado)."""

empleado[3] = "Valencia"
empleado.append("Ingeniería")
empleado.insert(1, 12345)

print(empleado)

"""
7. Elimina información:
o Usa .remove() para quitar un precio específico de la lista precios.
o Usa .pop() para eliminar el último precio e imprimir el valor eliminado.
o Usa del para eliminar el segundo elemento de la lista empleado."""

precios.remove(18)
ultimo_precio = precios.pop()
print("Precio eliminado:", ultimo_precio)
del empleado[1]
print(empleado)

"""
8. Combina listas:
o Crea una nueva lista llamada datos_empresa que combine empleado y
precios usando el operador +.
o Muestra el resultado."""

datos_empresa = empleado + precios
print(datos_empresa)


"""
9. Aplica métodos de listas:
o Usa .count() para contar cuántas veces se repite un mismo precio.
o Usa .copy() para duplicar la lista precios antes de vaciarla con .clear().
o Imprime ambas listas para comparar."""

repetido = precios.count(28)
print("El precio 28 se repite", repetido, "veces.")
precios_copia = precios.copy()
precios.clear()
print("Lista original vaciada:", precios)
print("Copia de la lista precios:", precios_copia)


"""
10. Ordena y reorganiza:
o Crea una lista llamada ventas con números enteros y ordénala de
menor a mayor con .sort().
o Luego invierte el orden con .reverse() y muestra el resultado final."""

ventas = [250, 100, 300, 150, 200]
ventas.sort()
print("Ventas ordenadas de menor a mayor:", ventas)
ventas.reverse()
print("Ventas en orden inverso:", ventas)

"""Crea una lista llamada lenguajes con los lenguajes de programación que te gustaría
aprender."""

lenguajes = ["Java", "JavaScript", "Python", "PHP", "Go"]

# Mostrar solo los dos primeros usando slicing
print("Primeros dos lenguajes:", lenguajes[:2])

#Cambia uno por otro que ya conozcas.
lenguajes[3] = "C#"
print("Lista tras reemplazar un lenguaje:", lenguajes)

#Agrega un nuevo lenguaje al final y elimina el primero.
lenguajes.append("Ruby")
del lenguajes[0]
print("Lista tras agregar y eliminar elementos:", lenguajes)

#Mostrar el contenido y tipo de las listas correctamente / Modificar, eliminar y agregar elementos sin errores.
print("Contenido final:", lenguajes)
print("Tipo:", type(lenguajes))

# .insert()
lenguajes.insert(1, "Kotlin")
print("Después de insert:", lenguajes)

# .remove()
lenguajes.remove("Go")
print("Después de remove:", lenguajes)

# .pop()
eliminado = lenguajes.pop(-1)   # último elemento
print("Después de pop:", lenguajes, "| Eliminado:", eliminado)

# .count()
lenguajes.append("Python")
print("Cantidad de 'Python':", lenguajes.count("Python"))

# .copy()
copia_lenguajes = lenguajes.copy()
print("Copia de la lista:", copia_lenguajes)

# .sort() 
copia_lenguajes.sort()
print("Copia ordenada:", copia_lenguajes)

# .reverse() 
copia_lenguajes.reverse()
print("Copia invertida:", copia_lenguajes)

# .clear()
lista_vacia = copia_lenguajes.copy()
lista_vacia.clear()
print("Lista vaciada:", lista_vacia)

# Acceso con índices positivos y negativos
print("Primer elemento (índice 0):", lenguajes[0])
print("Último elemento (índice -1):", lenguajes[-1])