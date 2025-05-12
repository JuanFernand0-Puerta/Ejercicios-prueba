# Códigos ANSI para colorear mensajes en la consola
warning = "\033[93m"
danger = "\033[91m"
success = "\033[92m"
reset = "\033[0m"

# Diccionario vacío para almacenar productos
inventario = {}

# Función para agregar un producto al inventario (mínimo 5)
def agregar_productos(inventario, nombre_producto, precio, cantidad):
    if cantidad < 5:
        print(danger + "❌ Debe agregar al menos 5 unidades del producto." + reset)
        return

    if nombre_producto in inventario:
        inventario[nombre_producto]["cantidad"] += cantidad
        inventario[nombre_producto]["precio"] = precio
    else:
        inventario[nombre_producto] = {"precio": precio, "cantidad": cantidad}
    print(success + f"✅ Producto '{nombre_producto}' agregado correctamente con {cantidad} unidades." + reset)

# Función para actualizar el precio
def agregar_precio(inventario, nombre_producto, nuevo_precio):
    inventario[nombre_producto]["precio"] = nuevo_precio

# Función para buscar un producto
def buscar_producto(inventario, nombre_producto):
    if nombre_producto in inventario:
        info = inventario[nombre_producto]
        print(success + f"✅ Producto encontrado: {nombre_producto}, Precio: {info['precio']}, Cantidad: {info['cantidad']}" + reset)
    else:
        print(danger + "❌ Producto no encontrado." + reset)

# Bucle principal con menú
while True:
    print("\n=============================")
    print("    ¿Qué deseas hacer hoy?     ")
    print("===============================")
    print("1.) Añadir productos")
    print("2.) Actualizar precio del producto")
    print("3.) Buscar producto")
    print("4.) Salir del programa")

    escoger_menu = input("Escoge una de las opciones (1-4): ")
    if escoger_menu.isdigit() and 1 <= int(escoger_menu) <= 4:
        escoger_menu = int(escoger_menu)
    else:
        print(warning + "Opción inválida, intenta de nuevo." + reset)
        continue

    match escoger_menu:
        case 1:
            while True:
                nombre_producto = input("Nombre del producto: ")
                if nombre_producto.replace(" ", "").isalpha():
                    break
                else:
                    print(warning + "Nombre inválido, intenta de nuevo." + reset)

            while True:
                precio = input("Precio del producto: ")
                try:
                    precio = float(precio)
                    if precio > 0:
                        break
                    else:
                        print(warning + "El precio debe ser mayor que 0." + reset)
                except:
                    print(warning + "Ingresa un número válido para el precio." + reset)

            while True:
                cantidad = input("Cantidad del producto (mínimo 5): ")
                try:
                    cantidad = float(cantidad)
                    if cantidad >= 5:
                        break
                    else:
                        print(danger + "Debe ingresar al menos 5 unidades." + reset)
                except:
                    print(warning + "Ingresa un número válido para la cantidad." + reset)

            agregar_productos(inventario, nombre_producto, precio, cantidad)

        case 2:
            nombre_producto = input("Nombre del producto a cambiar precio: ")
            if nombre_producto in inventario:
                while True:
                    agregar_precio_ = input("Nuevo precio: ")
                    try:
                        agregar_precio_ = float(agregar_precio_)
                        if agregar_precio_ > 0:
                            agregar_precio(inventario, nombre_producto, agregar_precio_)
                            print(success + f"Precio actualizado correctamente: {inventario[nombre_producto]}" + reset)
                            break
                        else:
                            print(danger + "El precio debe ser mayor que 0." + reset)
                    except:
                        print(warning + "Ingresa un número válido." + reset)
            else:
                print(warning + "Ese producto no existe. Agrégalo desde el menú." + reset)

        case 3:
            buscar_producto_ = input("Nombre del producto a buscar: ")
            buscar_producto(inventario, buscar_producto_)

        case 4:
            print(success + "Gracias por usar el sistema. ¡Hasta pronto!" + reset)
            break
