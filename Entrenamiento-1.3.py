from Funciones3 import *



# Códigos ANSI para colorear mensajes en la consola
warning = "\033[93m"
danger = "\033[91m"
success = "\033[92m"
reset = "\033[0m"

# Diccionario vacío para almacenar productos
inventario = {}

# Función para agregar un producto al inventario

# Bucle principal con menú
while True:
    print("=============================")
    print("    Que deseas hacer hoy     ")
    print("===============================")
    print("1.) Añadir productos")
    print("2.) Actualizar precio del producto ")
    print("3.) Buscar producto")
    print("4.) Salir del programa")

    # Valida la opción del menú
    escoger_menu = input("Escoge una de las opciones (1,4): ")
    if escoger_menu.isdigit() and 1 <= int(escoger_menu) <= 4:
        escoger_menu = int(escoger_menu)
    else:
        print(warning + "Opción inválida, intenta de nuevo" + reset)
        continue

    # Maneja las opciones del menú
    match escoger_menu:
        case 1:
            while True:
                nombre_producto = input("Escribe el nombre del producto que va a ingresar: ")
                if nombre_producto.replace(" ", "").isalpha():
                    break
                else:
                    print(warning + "Agrega un valor válido" + reset)

            while True:
                precio = input("Ingresa el precio del producto: ")
                if precio.isdigit() and float(precio) > 0.0:
                    precio = float(precio)
                    break
                else:
                    print(warning + "Agrega un valor válido" + reset)

            while True:
                cantidad = input("Ingrese la cantidad de productos que va a ingresar: ")
                if cantidad and cantidad.isdigit() and float(cantidad) > 0.0:
                    cantidad = float(cantidad)
                    break
                else:
                    print(warning + "Agregue un valor válido" + reset)

            agregar_productos(inventario,nombre_producto, precio, cantidad)

        case 2:
            while True:
                nombre_producto = input("Que producto le desea cambiar el precio: ")
                if nombre_producto in inventario:
                    agregar_precio_ = input("Cual precio va a poner: ")
                    if agregar_precio_.isdigit() and float(agregar_precio_):
                        agregar_precio_ = float(agregar_precio_)
                        agregar_precio(inventario,nombre_producto, agregar_precio_)
                        print(success + f"El precio ha sido actualizado {inventario[nombre_producto]}" + reset)
                        break
                    else:
                        print(danger + "Precio invalido. intenta de nuevo" + reset)
                else:
                    print(warning + "Agrega un producto existente o crealo desde el menu" + reset)
                    break

        case 3:
            # Solicita el nombre del producto y usa la función buscar_producto
            while True:
                buscar_producto_ = input("Qué producto desea mirar si hay: ")
                buscar_producto(inventario,buscar_producto_)
                if buscar_producto_ in inventario:
                    break  # Sale del bucle si el producto se encuentra
                # Continúa pidiendo si no se encuentra, hasta que se ingrese un producto válido

        case 4:
            print("Gracias por usar")
            break