print("\n*** Práctica de Condicionales en Python ***\n")

"""1.Condición simple (if)
Situación: La empresa registra las horas trabajadas por cada empleado.
Instrucciones:
Crea una variable que represente el número de horas trabajadas.
Utiliza un if para comprobar si el valor es mayor que cero y muestra un mensaje indicando
que las horas fueron registradas correctamente."""

print("1.Condición simple (if)")

horas_trabajadas = 40 # Asigno variable de horas trabajadas

if horas_trabajadas > 0: # Hago que la condición sea mayor a 0 como se indica
    print("Las horas fueron registradas correctamente.") # Realizo el print monstrando que las horas fueron registradas correctamente



"""2.Uso de if y else
Situación: La empresa controla la puntualidad de los empleados.
Instrucciones:
Crea una variable que represente la hora de llegada del empleado.
Usa if y else para mostrar un mensaje diferente según si el empleado llega a tiempo o llega
tarde."""

print("\n2.Uso de if y else")

hora_ingreso = 9 # Asigno variable de hora de ingreso
hora_limite = 9 # Asigno una variable de hora limite
if hora_ingreso <= hora_limite: # Hago que la condicion sea menor o igual a la hora limite
    print("El empleado llegó a tiempo.") # Realizo el print mostrando que el empleado llego a tiempo
else: # Si no se cumple la condicion anterior
    print("El empleado llegó tarde.") # Realizo el print mostrando que el empleado llego tarde



"""3.Operadores lógicos (and)
Situación: Solo se pueden registrar entre 0 y 12 horas de trabajo al día.
Instrucciones:
Crea una variable que represente las horas trabajadas.
Utiliza el operador lógico and para comprobar que el valor esté dentro del rango permitido y
muestra un mensaje adecuado."""

print("\n3.Operadores lógicos (and)")

horas_trabajadas = 8 # Asigno variable de horas trabajadas

if horas_trabajadas >= 0 and horas_trabajadas <= 12: # Hago que la condicion sea mayor o igual a 0 y menor o igual a 12
    print("El valor de horas trabajadas está dentro del rango permitido.") # Realizo el print mostrando que las horas trabajadas estan dentro del rango permitido



"""4.Uso de elif
Situación: La empresa clasifica el retraso según los minutos de llegada tarde.
Instrucciones:
Crea una variable que represente los minutos de retraso.
Usa if, elif y else para mostrar un mensaje diferente según el nivel de retraso del empleado."""

print("\n4.Uso de elif")

minutos_retraso = 10 # Asigno variable de minutos de retraso

if minutos_retraso == 0: # Hago que la condicion sea igual a 0
    print("El empleado llegó a tiempo.") # Realizo el print mostrando que el empleado llego a tiempo
elif minutos_retraso <= 10: # Hago que la condicion sea menor o igual a 10
    print("El empleado llegó con un retraso.") # Realizo el print mostrando que el empleado llego con un retraso leve
else: # Si no se cumple ninguna de las condiciones anteriores
    print("El empleado llegó muy tarde.") # Realizo el print mostrando que el empleado llego muy tarde



"""5.Strings en condicionales
Situación: Cuando un empleado falta, debe escribir el motivo de la ausencia.
Instrucciones:
Crea una variable de tipo texto que represente el motivo de la ausencia.
Comprueba si la cadena está vacía o no y muestra un mensaje indicando si el motivo fue
registrado."""

print("\n5.Strings en condicionales")

motivo_ausencia = "Mal de Salud" # Asigno variable de motivo de ausencia
if motivo_ausencia: # Hago que la condicion sea si la variable no esta vacia
    print("El motivo de la ausencia fue registrado.") # Realizo el print mostrando que el motivo de la ausencia fue registrado
else: # Si la variable esta vacia
    print("No se registró ningún motivo de ausencia.") # Realizo el print mostrando que no se registro ningun motivo de ausencia



"""6.Uso de not
Situación: Es obligatorio registrar la hora de salida del trabajo.
Instrucciones:
Crea una variable que represente la hora de salida.
Utiliza el operador not para comprobar si la variable está vacía y mostrar un mensaje de
aviso si no se ha registrado."""

print("\n6.Uso de not")

hora_salida = "" # Asigno variable de hora de salida vacia

if not hora_salida: # Hago que la condicion sea si la variable esta vacia
    print("No se registró la hora de salida.\n") # Realizo el print mostrando que no se registro la hora de salida