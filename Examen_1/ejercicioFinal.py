#Jolman & Joel

nombre = input("Ingrese su nombre: ") #pedimos al usuario su nombre
edad = input("Ingrese su edad: ")#pedimos al usuario su edad
ciudad = input("Ingrese su ciudad: ")#pedimos al usuario su ciudad

edad = int(edad) #convertimos la edad a entero
datos_usuario = [nombre, edad, ciudad] #creamos una lista con los datos del usuario
print("Datos del usuario: ", datos_usuario)#mostramos los datos del usuario

print(f"Me llamo {nombre} tengo {edad} años y vivo en {ciudad}.")#mostramos los datos del usuario con f string
print("Cantidad de datos del usuario: ", len(datos_usuario))#mostramos la cantidad de datos del usuario

hobbies = input("Ingrese su hobbie: ")#pedimos al usuario su hobbie

lista_hobbies = [] #creamos una lista para almacenar los hobbies
lista_hobbies.append(hobbies) #agregamos el hobbie a la lista


hobbies = input("Ingrese su hobbie: ")#pedimos al usuario su hobbie
lista_hobbies.append(hobbies) #agregamos el hobbie a la lista

informacion_completa = [datos_usuario,lista_hobbies]#creamos una lista con los datos del usuario y sus hobbies
print("Información completa del usuario: ", informacion_completa)   #mostramos la información completa del usuario
print(f"Me llamo {nombre} tengo {edad} años y vivo en {ciudad} y uno de mis hobbies es {lista_hobbies[0]}.")#mostramos los datos del usuario con f string y su primer hobbie