print("\n", "* Actividad", "Diccionarios, Condicionales y Bucles *\n")

print("\nEn la parte 1 cree el diccionario con los datos de los alumnos.\n")

# --- Parte 1: Inicio ---
alumnos = {}  # Creo la variable diccionario vacía

# asgino los alumnos con sus datos
alumnos["Jc"] = {
    "edad": 34,
    "curso": "DawII",
    "lenguajes": {"Python", "Java"},
    "nota": 7.5,
}
alumnos["Ra"] = {
    "edad": 50,
    "curso": "Psicología",
    "lenguajes": {"Español", "Ingles"},
    "nota": 8.0,
}
alumnos["Za"] = {
    "edad": 7,
    "curso": "Primaria",
    "lenguajes": {"Español", "Catalan"},
    "nota": 9.0,
}


# --- Parte 2: Mostrar alumnos ---
print("\n", "* Parte 2 - Mostrar alumnos *\n")
for (
    alumno,
    info,
) in (
    alumnos.items()
):  # Recorro el diccionario principal con .items() para obtener clave y valor
    print(f"Alumno: {alumno}")  # Imprimo el nombre del alumno
    for (
        key,
        value,
    ) in info.items():  # Recorro el diccionario interno con .items() y key y value para obtener clave y valor
        print(
            f"{key.capitalize()}: {value}"
        )  # Imprimo la clave y el valor del diccionario interno
    print("")  # Línea en blanco para separar alumnos


# --- Parte 3: Condicionales sobre notas ---
print("\n", "* Parte 3 - Condicionales sobre notas *\n")
for (
    alumno,
    info,
) in (
    alumnos.items()
):  # Recorro el diccionario principal con .items() para obtener clave y valor
    nota = info["nota"]  # creo la variable nota para almacenar la nota del alumno
    if nota < 5:  # condicional para determinar el estado según la nota
        estado = "Suspenso"  # estado si la nota es menor que 5
    elif 5 <= nota < 7:  # condicional para determinar el estado según la nota
        estado = "Aprobado"  # estado si la nota es entre 5 y 7
    elif 7 <= nota < 9:  # condicional para determinar el estado según la nota
        estado = "Notable"  # estado si la nota es entre 7 y 9
    else:  # condicional para determinar el estado según la nota
        estado = "Sobresaliente"  # estado si la nota es 9 o superior

    print(
        f"Alumno: {alumno} - Nota media: {nota} ({estado})"
    )  # Imprimo el nombre del alumno, su nota y su estado uso f-string para formatear la cadena de texto


# --- Parte 4: Filtrar alumnos ---
print("\n", "* Parte 4 - Filtrar alumnos *\n")
print("Los alumnos con nota media >= a 7 son: \n")
for (
    alumno,
    info,
) in (
    alumnos.items()
):  # Recorro el diccionario principal con .items() para obtener clave y valor
    if (
        info["edad"] > 18 and info["nota"] >= 7
    ):  # condicional para filtrar alumnos mayores de 18 años y con nota media >= 7
        print(
            f"Alumno: {alumno} cumple con los requisitos (Edad: {info['edad']}, Nota: {info['nota']})"  # Imprimo el nombre del alumno, su edad y su nota
        )


# --- Parte 5 |6 | 7 | 8 : Menú Interactivo ---

# Creo un menú interactivo para mostrar, buscar y añadir alumnos y un break para salir del programa
while True:
    print("\nMenú:\n")
    print("1. Mostrar alumnos")
    print("2. Buscar alumno")
    print("3. Añadir alumno")
    print("4. Salir")

    opcion = input(
        "\nElige una opción (1-4): "
    )  # Solicito al usuario que elija una opción
    if opcion == "1":  # esta opcion es para mostrar todos los alumnos
        for (
            alumno,
            info,
        ) in (
            alumnos.items()
        ):  # Recorro el diccionario principal con .items() para obtener clave y valor
            print(f"\nAlumno: {alumno}")  # Imprimo el nombre del alumno
            for (
                key,
                value,
            ) in info.items():  # Recorro el diccionario interno con .items() y key y value para obtener clave y valor
                print(
                    f"{key.capitalize()}: {value}"
                )  # Imprimo la clave y el valor del diccionario interno
            print("")  # para separar alumnos

    elif opcion == "2":  # esta opcion es para buscar un alumno por su nombre
        buscar_alumno = (
            input("\nIntroduce el nombre del alumno a buscar: ").strip().lower()
        )  # Solicito al usuario que introduzca el nombre del alumno a buscar y lo convierto a minúsculas y elimino espacios en blanco
        encontrado = False  # variable para controlar si se ha encontrado el alumno y evitar mensajes repetidos y sino lo indico al final

        for alumno in alumnos:  # para recorrer el diccionario principal
            if (
                alumno.lower() == buscar_alumno
            ):  # para comparar el nombre del alumno en minúsculas
                info = alumnos[alumno]  # aca obtengo la información del alumno
                print(
                    f"\nAlumno: {alumno}"
                )  # este print es para mostrar el nombre del alumno encontrado
                for (
                    key,
                    value,
                ) in info.items():  # este for es para recorrer el diccionario interno del alumno encontrado
                    print(
                        f"{key.capitalize()}: {value}"
                    )  # uso f-string para formatear la cadena de texto y mostrar la clave y el valor del diccionario interno
                encontrado = (
                    True  # si se encuentra el alumno, cambio la variable a True
                )
                break  # aca salgo del bucle una vez encontrado el alumno

        if not encontrado:  # si no se ha encontrado el alumno, muestro el mensaje
            print(
                "\nNo se ha encontrado el alumno."
            )  # imprime el mensaje si no se encuentra el alumno

    elif opcion == "3":  # esta opcion es para añadir un nuevo alumno
        nuevo_nombre = input(
            "\nIntroduce el nombre del nuevo alumno (o escribe 'salir'): "
        )  # pido al usuario que introduzca el nombre del nuevo alumno o salir para regresar al menú

        if nuevo_nombre.lower() == "salir":  # si se introduce salir, regreso al menú
            print("\nRegresarás al menú...")
            continue  # este continue es para regresar al inicio del bucle y mostrar el menú nuevamente

        try:  # try para manejar posibles errores al convertir la edad y la nota a números
            nueva_edad = int(
                input("Introduce la edad: ")
            )  # pido al usuario que introduzca la edad del nuevo alumno y la convierto a entero
            nuevo_curso = input(
                "Introduce el curso: "
            )  # pido al usuario que introduzca el curso del nuevo alumno
            nuevos_lenguajes = set(
                lang.strip()
                for lang in input(
                    "Introduce los lenguajes (separados por comas): "
                ).split(
                    ","
                )  # uso split para separar los lenguajes por comas y strip para eliminar espacios en blanco y lang.strip() sirve para limpiar cada lenguaje individualmente a la hora de crear el set
            )
            nueva_nota = float(
                input("Introduce la nota media: ")
            )  # pido al usuario que introduzca la nota media del nuevo alumno y la convierto a float

            alumnos[nuevo_nombre] = {
                "edad": nueva_edad,
                "curso": nuevo_curso,
                "lenguajes": nuevos_lenguajes,
                "nota": nueva_nota,
            }  # solicito al usuario que introduzca los datos del nuevo alumno y los añado al diccionario principal
            print("\nAlumno añadido correctamente.")
        except ValueError:
            print("\nError: La edad y la nota deben ser números válidos.")

    elif opcion == "4":  # esta opcion es para salir del programa
        print("\nHas salido del programa.\n")
        break  # salgo del bucle y termino el programa

    else:
        print("\n¡Opción no válida, por favor elige nuevamente!")

# --- Reto de la actividad  ---

print("\n", "* Media de notas de todos los alumnos *\n")

suma_notas = 0  # variable para almacenar la suma de las notas
total_alumnos = len(alumnos)  # variable para almacenar el total de alumnos

for info in (
    alumnos.values()
):  # este for es para recorrer los valores del diccionario principal
    suma_notas += info["nota"]  # esta variable suma las notas de todos los alumnos

media = (
    suma_notas / total_alumnos if total_alumnos > 0 else 0
)  # aca se calcula la media de las notas, evitando la división por cero
print(
    f"La media de todos los alumnos es: {media:.2f}", "\n"
)  # imprimo la media de las notas con dos decimales usando f-string para formatear la cadena de texto
