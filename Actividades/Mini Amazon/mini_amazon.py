# mini_amazon.py

# Datos iniciales de productos y promociones que estarán en el catálogo
CATALOGO = {
    "A001": {
        "nombre": "Teclado Mecánico",
        "precio": 49.99,
        "stock": 10,
        "peso_kg": 0.9,
    },
    "A002": {"nombre": "Ratón Gaming", "precio": 25.50, "stock": 5, "peso_kg": 0.2},
    "A003": {"nombre": 'Monitor 24"', "precio": 149.00, "stock": 3, "peso_kg": 3.5},
    "A004": {"nombre": "Auriculares", "precio": 35.99, "stock": 0, "peso_kg": 0.4},
    "A005": {"nombre": "Webcam HD", "precio": 39.90, "stock": 7, "peso_kg": 0.3},
}

CODIGOS_PROMO = {
    "ENVIOFREE": {"tipo": "envio", "descuento": 1.0},
    "DESC10": {"tipo": "total", "descuento": 0.10},
}

# Variables globales para pedidos confirmados y cancelados, lo creo para usarlas en varias funciones y así llevar el control de los pedidos a tarves de la lista

pedidos_confirmados = []  # Lista de pedidos confirmados
pedidos_cancelados = []  # Lista de pedidos cancelados


# Funcion para mostrar el catálogo de productos
def mostrar_catalogo(catalogo):
    print("\n* Catalógo de Productos *\n")  # hago el print del catálogo más visual
    for codigo, producto in catalogo.items():  # Itero sobre los productos del catálogo
        print(
            f"{codigo}: {producto['nombre']} - {producto['precio']}€ (Stock: {producto['stock']}, Peso: {producto['peso_kg']}kg)"
        )  # con este print muestro el código, nombre, precio, stock y peso de cada producto
    print()  # Línea en blanco al final del catálogo para que tengan espaciado


# Función para validar el código de producto
def validar_codigo_producto(
    catalogo, codigo
):  # valido si el código del producto existe en el catálogo
    for cod in catalogo:  # itero sobre los códigos del catálogo
        if cod == codigo:  # si el código existe devuelvo True
            return True
    else:  # si no existe devuelvo False
        return False


# Función para agregar un producto al carrito
def agregar_al_carrito(
    carrito, catalogo, codigo, cantidad
):  # agrego un producto al carrito
    if not validar_codigo_producto(
        catalogo, codigo
    ):  # valido si el código del producto es válido
        print("Error: Código de producto no válido")  # si no es válido muestro un error
        return  # salgo de la función

    if catalogo[codigo]["stock"] < cantidad:  # verifico si hay stock suficiente
        print(
            f"Error: Stock insuficiente. Disponible: {catalogo[codigo]['stock']}"
        )  # si no hay stock suficiente muestro un error
        return  # salgo de la función

    # Descuento del stock del catálogo al agregar al carrito
    catalogo[codigo]["stock"] -= cantidad

    # Devuelvo al carrito la cantidad agregada del producto
    if codigo in carrito:
        carrito[codigo] += (
            cantidad  # si el producto ya está en el carrito sumo la cantidad
        )
    else:
        carrito[codigo] = cantidad  # si no está en el carrito lo agrego con la cantidad

    print(
        f"{cantidad} x {catalogo[codigo]['nombre']} añadido al carrito"
    )  # confirmo que se ha añadido el producto al carrito


# Función para calcular totales del carrito
def calcular_totales(carrito, catalogo, iva=0.21):  # calculo los totales del carrito
    subtotal = 0  # inicializo el subtotal
    peso_total = 0  # inicializo el peso total

    for codigo, cantidad in carrito.items():  # itero sobre los productos del carrito
        subtotal += catalogo[codigo]["precio"] * cantidad  # calculo el subtotal
        peso_total += catalogo[codigo]["peso_kg"] * cantidad  # calculo el peso total

    importe_iva = subtotal * iva  # calculo el importe del IVA
    total = subtotal + importe_iva  # calculo el total

    return {
        "subtotal": subtotal,  # devuelvo el subtotal
        "iva": importe_iva,  # devuelvo el importe del IVA
        "total": total,  # devuelvo el total
        "peso_total": peso_total,  # devuelvo el peso total
    }


# Función para calcular el coste de envío
def calcular_envio(peso_total, zona="PENINSULA"):  # calculo el coste de envío
    if zona == "PENINSULA":  # si la zona es península
        if peso_total < 1:  # si el peso es menor a 1kg
            return 3.00  # coste de envío 3€
        elif peso_total < 5:  # si el peso es menor a 5kg
            return 5.00  # coste de envío 5€
        else:
            return 8.00  # coste de envío 8€
    else:
        return 10.00  # coste de envío para otras zonas


# Función para aplicar códigos promocionales
def aplicar_promos(total, envio, *codigos):  # aplico códigos promocionales al pedido
    descuento_total = 0  # inicializo el descuento total
    descuento_envio = 0  # inicializo el descuento de envío

    for codigo in codigos:  # itero sobre los códigos promocionales
        if codigo in CODIGOS_PROMO:  # si el código está en los códigos promocionales
            promo = CODIGOS_PROMO[
                codigo
            ]  # obtengo la promoción correspondiente al código
            if promo["tipo"] == "envio":  # si la promoción es de envío
                descuento_envio = (
                    envio * promo["descuento"]
                )  # aplico el descuento de envío
            elif promo["tipo"] == "total":  # si la promoción es de total
                descuento_total = (
                    total * promo["descuento"]
                )  # aplico el descuento total

    return descuento_total, descuento_envio  # devuelvo los descuentos aplicados


# Función para quitar un producto del carrito
def quitar_producto_carrito(carrito, catalogo):  # quito un producto del carrito
    if not carrito:  # si el carrito está vacío
        print("El carrito está vacío")  # muestro un mensaje
        return  # salgo de la función

    codigo = input(
        "Introduce el código del producto a quitar: "
    ).upper()  # pido el código del producto a quitar

    if codigo in carrito:  # si el producto está en el carrito
        cantidad = carrito[codigo]  # obtengo la cantidad del producto en el carrito
        # Devolver el stock al catálogo al quitar del carrito
        catalogo[codigo]["stock"] += (
            cantidad  # devuelvo la cantidad al stock del catálogo
        )
        # Eliminar del carrito el producto completamente
        del carrito[codigo]  # elimino el producto del carrito
        print(
            f"Producto {codigo} eliminado del carrito ({cantidad} unidades devueltas al stock)"
        )  # confirmo que se ha eliminado el producto del carrito
    else:
        print(
            "Ese producto no está en el carrito"
        )  # si el producto no está en el carrito muestro un mensaje


# Función para ver el contenido del carrito
def ver_carrito(carrito, catalogo):  # muestro el contenido actual del carrito
    if not carrito:  # si el carrito está vacío
        print("\nEl carrito está vacío\n")  # muestro un mensaje
        return  # salgo de la función

    print("\n* Carrito * ")
    for codigo, cantidad in carrito.items():  # itero sobre los productos del carrito
        producto = catalogo[codigo]  # obtengo el producto correspondiente al código
        print(
            f"{codigo}: {producto['nombre']} x{cantidad} - {producto['precio'] * cantidad}€"
        )  # muestro el código, nombre, cantidad y precio total del producto en el carrito
    print()  # línea en blanco al final del carrito para que tenga espaciado


# Función para confirmar el pedido
def confirmar_pedido(carrito, catalogo):  # proceso la confirmación del pedido
    if not carrito:  # si el carrito está vacío
        print("El carrito está vacío")  # muestro un mensaje
        return  # salgo de la función

    # Calcular totales y envío
    totales = calcular_totales(carrito, catalogo)  # calculo los totales del carrito
    envio = calcular_envio(totales["peso_total"])  # calculo el coste de envío

    # Mostrar resumen del pedido
    print("\n* Resumen del pedido *")
    for codigo, cantidad in carrito.items():  # itero sobre los productos del carrito
        producto = catalogo[codigo]  # obtengo el producto correspondiente al código
        print(
            f"{producto['nombre']} x{cantidad} - {producto['precio'] * cantidad}€"
        )  # muestro el nombre, cantidad y precio total del producto en el carrito

    print(f"\nSubtotal: {totales['subtotal']:.2f}€")  # muestro el subtotal
    print(f"IVA (21%): {totales['iva']:.2f}€")  # muestro el importe del IVA
    print(f"Envío: {envio:.2f}€")  # muestro el coste de envío

    # Aplicar promociones si hay códigos promocionales
    codigos_promo = (
        input(
            "\n¿Tienes códigos promocionales? (separados por comas, o Enter para continuar): "
        )  # pido los códigos promocionales al usuario
        .upper()  # convierto a mayúsculas
        .split(",")  # separo los códigos por comas
    )  # guardo los códigos promocionales en una lista
    codigos_promo = [
        c.strip() for c in codigos_promo if c.strip()
    ]  # limpio los códigos promocionales de espacios en blanco y vacíos

    desc_total, desc_envio = aplicar_promos(
        totales["total"], envio, *codigos_promo
    )  # aplico los códigos promocionales al pedido

    total_final = (
        totales["total"] + envio - desc_total - desc_envio
    )  # calculo el total final del pedido

    if desc_total > 0:  # si hay descuento total muestro el descuento aplicado
        print(
            f"Descuento aplicado: -{desc_total:.2f}€"
        )  # muestro el descuento aplicado
    if desc_envio > 0:  # si hay descuento en envío muestro el descuento aplicado
        print(
            f"Descuento en envío: -{desc_envio:.2f}€"
        )  # muestro el descuento aplicado en envío

    print(f"\nTOTAL A PAGAR: {total_final:.2f}€")  # muestro el total a pagar del pedido

    # Confirmación del pedido por parte del usuario
    confirmacion = input(
        "\n¿Confirmar pedido? (S/N): "
    ).upper()  # pido la confirmación del pedido al usuario y convierto a mayúsculas

    if confirmacion == "S":  # si el usuario confirma el pedido
        # El stock ya fue descontado al agregar al carrito
        pedidos_confirmados.append(
            carrito.copy()
        )  # añado el pedido a la lista de pedidos confirmados
        print("\nPedido CONFIRMADO")  # confirmo que el pedido ha sido confirmado
        carrito.clear()  # limpio el carrito
    else:  # si el usuario cancela el pedido
        # Devolver el stock si se cancela
        for (
            codigo,
            cantidad,
        ) in carrito.items():  # itero sobre los productos del carrito
            catalogo[codigo]["stock"] += (
                cantidad  # devuelvo la cantidad al stock del catálogo
            )

        pedidos_cancelados.append(
            carrito.copy()
        )  # añado el pedido a la lista de pedidos cancelados
        print("\nPedido CANCELADO")  # confirmo que el pedido ha sido cancelado
        carrito.clear()  # limpio el carrito


# Función para mostrar el informe final
def mostrar_informe_final():  #
    print("\n* Informe Final *\n")  # muestro el informe final
    print(
        f"Pedidos confirmados: {len(pedidos_confirmados)}"
    )  # muestro el número de pedidos confirmados
    print(
        f"Pedidos cancelados: {len(pedidos_cancelados)}"
    )  # muestro el número de pedidos cancelados

    # Calcular producto más vendido usando diccionario
    ventas = {}  # inicializo el diccionario de ventas

    for pedido in pedidos_confirmados:  # itero sobre los pedidos confirmados
        for codigo, cantidad in pedido.items():  # itero sobre los productos del pedido
            if codigo in ventas:  # si el producto ya está en el diccionario de ventas
                ventas[codigo] += cantidad  # sumo la cantidad vendida
            else:  # si el producto no está en el diccionario de ventas
                ventas[codigo] = cantidad  # inicializo la cantidad vendida

    for codigo in ventas:  # itero sobre los productos vendidos
        # Si hay al menos un producto vendido muestro el más vendido
        mas_vendido = max(
            ventas, key=ventas.get
        )  # obtengo el producto más vendido usando max con key y ventas.get para obtener la cantidad vendida
        print(
            f"\nProducto más vendido: {CATALOGO[mas_vendido]['nombre']} ({ventas[mas_vendido]} unidades)"
        )  # muestro el nombre del producto más vendido y la cantidad vendida
        break  # salgo del bucle después de mostrar el más vendido
    else:  # si no hay productos vendidos
        print(
            "No hubo ventas realizadas.!"
        )  # muestro un mensaje indicando que no hubo ventas

    print()


def main():
    """Función principal que ejecuta el programa"""
    carrito = {}  # Carrito de compras inicial vacío

    # Menú principal con while True y opciones
    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Ver catálogo")
        print("2. Añadir producto al carrito")
        print("3. Quitar producto del carrito")
        print("4. Ver carrito")
        print("5. Confirmar pedido")
        print("0. Salir")

        opcion = input(
            "\nSelecciona una opción: "
        )  # Pido al usuario que seleccione una opción

        if opcion == "1":  # Opción para ver el catálogo
            mostrar_catalogo(CATALOGO)  # Muestro el catálogo de productos

        elif opcion == "2":  # Opción para añadir producto al carrito
            mostrar_catalogo(CATALOGO)  # Muestro el catálogo de productos
            codigo = input(
                "Introduce el código del producto: "
            ).upper()  # Pido el código del producto y lo convierto a mayúsculas

            # Validar código usando while-else con un máximo de 3 intentos
            intentos = 0  # Inicializo el contador de intentos
            while intentos < 3:  # Mientras el número de intentos sea menor a 3
                if validar_codigo_producto(CATALOGO, codigo):  # Si el código es válido
                    cantidad = int(
                        input("Introduce la cantidad: ")
                    )  # Pido la cantidad del producto
                    agregar_al_carrito(
                        carrito, CATALOGO, codigo, cantidad
                    )  # Agrego el producto al carrito
                    break  # Salgo del bucle
                else:  # Si el código no es válido
                    intentos += 1  # Incremento el contador de intentos
                    if intentos < 3:  # Si aún quedan intentos
                        codigo = input(
                            "Código no válido. Intenta de nuevo: "
                        ).upper()  # Pido el código nuevamente
            else:  # Si se alcanzan los 3 intentos sin éxito
                print("Máximo de intentos alcanzado")  # Muestro un mensaje de error

        elif opcion == "3":  # Opción para quitar producto del carrito
            quitar_producto_carrito(carrito, CATALOGO)  # Quito un producto del carrito

        elif opcion == "4":  # Opción para ver el carrito
            ver_carrito(carrito, CATALOGO)  # Muestro el contenido del carrito

        elif opcion == "5":  # Opción para confirmar pedido
            confirmar_pedido(carrito, CATALOGO)  # Confirmo el pedido

        elif opcion == "0":  # Opción para salir del programa
            print("\nSaliste del programa\n")  # Mensaje de salida
            break  # Salgo del bucle principal y termino el programa

        else:  # Opción no válida
            print("Opción no válida")  # Muestro un mensaje de error

    # Mostrar informe final al salir del programa
    mostrar_informe_final()  # Muestro el informe final de pedidos confirmados y cancelados


# Ejecuto el programa main principal para iniciar la aplicación
if __name__ == "__main__":
    main()
