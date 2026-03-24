# Examen Python - Joel Otoya

# Lista de cursos (tupla)
cursos_disponibles = ("Python", "Redes", "Linux", "Seguridad", "BasesDatos")
alumnos = {}  # creo el diccionario para almacenar los alumnos.


# creo la clase alumno, con los atributos pedidos
class Alumno:
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.cursos = (
            set()
        )  # este set almacena los cursos matriculados, evitando duplicados

    def matricular(self, curso):
        self.cursos.add(curso)

    def __str__(self):
        if len(self.cursos) == 0:
            return f"DNI: {self.dni} | Nombre: {self.nombre} | Edad: {self.edad} | (Sin cursos)"
        else:
            # convierto el set de los cursos a un string para que se vea como curso1, curso2 y asi
            cursos_texto = ", ".join(self.cursos)
            return f"DNI: {self.dni} | Nombre: {self.nombre} | Edad: {self.edad} | Cursos: {cursos_texto}"


# funciones del menú


def mostrar_menu():
    print("\n *** Menú *** \n")
    print("1) Añadir alumno")
    print("2) Matricular alumno en curso")
    print("3) Mostrar ficha de un alumno")
    print("4) Listar alumnos")
    print("5) Estadísticas")
    print("6) Salir")


def pedir_opcion(mensaje):
    """pido la edad como entero y valido que sea un número, si no lo es, muestro un mensaje de error y vuelvo a pedirlo."""
    while True:
        try:
            dato = int(input(mensaje))
        except ValueError:
            print("Edad invalida, desbes escribir un número.")
        else:
            # Si no hay error, devuelce el dato como entero.
            return dato
        finally:
            # acá podría poner un mensaje o algo, por ahora lo dejo vacío, pero se ejecuta haya error o no.
            pass  # este pass es para que no de error por no tener nada en el finally.


def pedir_curso():
    print("Cursos:", cursos_disponibles)
    curso = input("Escribe el nombre del curso: ")
    return curso


# este es el bucle principal del programa, pues, del menú, hasta que el usr elija salir.

while True:
    mostrar_menu()
    opcion = pedir_opcion("Elige una opción: ")

    # 1) Añadir alumno
    if opcion == 1:
        dni = input("DNI: ")
        if dni in alumnos:
            print("Ya existe un alumno con ese DNI.")
        else:
            nombre = input("Nombre: ")
            edad = pedir_opcion(
                "Edad: "
            )  # pido la edad usando la función que valida que sea un número entero, si no lo es, vuelve a pedirlo.

            # creo el objeto alumno y lo guardo en el diccionario usando el DNI como clave.
            nuevo_alumno = Alumno(dni, nombre, edad)
            alumnos[dni] = nuevo_alumno
            print("Alumno Añadido.")

    # 2) Matricular alumno
    elif opcion == 2:
        dni = input("Introduce DNI del alumno: ")
        if dni not in alumnos:
            print("Alumno no encontrado.")
        else:
            curso = pedir_curso()

            # veo si el curso esta en la tupla que se creó
            if curso in cursos_disponibles:
                alumno_obj = alumnos[
                    dni
                ]  # obtengo el objeto alumno del diccionario usando el DNI
                alumno_obj.matricular(
                    curso
                )  # uso el metodo matricular del objeto alumno para agregar el curso al set de cursos matriculados
                print("Curso Matriculado.")
            else:
                print("Curso inválido.")

    # 3) Mostrar ficha
    elif opcion == 3:
        dni = input("Introduce DNI: ")
        if dni in alumnos:
            print(alumnos[dni])  # Esto llama automáticamente al __str__
        else:
            print("Alumno no encontrado.")

    # 4) Listar alumnos
    elif opcion == 4:
        print("\n ** Lista ** ")
        for alumno in alumnos.values():
            print(f"{alumno.dni} - {alumno.nombre} - {len(alumno.cursos)} cursos")

    # 5) Estadísticas
    elif opcion == 5:
        print("\n ** Estadísticas ** \n")
        print(f"Total de alumnos: {len(alumnos)}")
        print(f"Total de cursos disponibles: {len(cursos_disponibles)}")

        # esto es para contar cuantas veces se matriculo un curso
        conteo = {}
        total_matriculas = 0

        for alumno in alumnos.values():
            for curso in alumno.cursos:
                total_matriculas += 1
                if curso in conteo:
                    conteo[curso] += 1
                else:
                    conteo[curso] = 1

        if total_matriculas == 0:
            print("No hay matrículas.")
        else:
            # Buscamos el curso con más matriculacion
            curso_repetido = ""
            maximo = 0
            for nombre_curso, cantidad in conteo.items():
                if cantidad > maximo:
                    maximo = cantidad
                    curso_repetido = nombre_curso

            print(f"Curso más repetido: {curso_repetido} ({maximo} alumnos)")

    # 6) Salir
    elif opcion == 6:
        print("Adiós.!")
        break  # termina el bucle y sale del programa

    else:
        print("Opción incorrecta.")
