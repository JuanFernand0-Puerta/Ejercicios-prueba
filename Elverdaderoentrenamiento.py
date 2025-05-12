# Códigos ANSI para colorear mensajes en la consola
warning = "\033[93m"
danger = "\033[91m"
success = "\033[92m"
reset = "\033[0m"

# Diccionario vacío para agregar productos
inventary = {}

# Función para agregar producto al inventario (mínimo 5)
def add_products(inventary, name_product, price, amount):
    if amount < 5:
        print(danger + "❌ Debe agregar al menos 5 productos" + reset)
        return

    if name_product in inventary:
        inventary[name_product]["cantidad"] += amount
        inventary[name_product]["precio"] = price  # Corrige la clave 'price'
    else:
        inventary[name_product] = {"precio": price, "cantidad": amount}
    print(success + f"✅ Producto '{name_product}' agregado correctamente con {amount} unidades." + reset)

# Función para actualizar el precio
def add_price(inventary, name_product, new_price):
    inventary[name_product]["precio"] = new_price

# Función para buscar un producto
def search_product(inventary, name_product):
    if name_product in inventary:
        info = inventary[name_product]
        print(success + f"✅ Producto encontrado: {name_product}, Precio: {info['precio']}, Cantidad: {info['cantidad']}" + reset)
    else:
        print(danger + "❌ Producto no encontrado." + reset)

# Función para eliminar un producto
def delete_product(inventary, name_product):
    if name_product in inventary:
        del inventary[name_product]
        print(success + f"✅ Producto '{name_product}' eliminado del inventario." + reset)
    else:
        print(danger + "❌ Producto no encontrado." + reset)

# Función para calcular el valor total del inventario
def calculate_total_value(inventary):
    total = 0
    for producto in inventary.values():
        total += producto["precio"] * producto["cantidad"]
    return total

# Bucle principal con menú
while True:
    print("\n=============================")
    print("    ¿Qué deseas hacer hoy?   ")
    print("=============================")
    print("1.) Añadir productos (mínimo 5)")
    print("2.) Consultar productos")
    print("3.) Actualizar precio de un producto")
    print("4.) Eliminar producto del inventario")
    print("5.) Calcular el valor total del inventario")
    print("6.) Salir del programa")

    choose_menu = input("Escoge una de las opciones (1-6): ")

    if choose_menu.isdigit() and 1 <= int(choose_menu) <= 6:
        choose_menu = int(choose_menu)
    else:
        print(warning + "⚠ Opción inválida, intenta de nuevo" + reset)
        continue

    match choose_menu:
        case 1:
            name_product = input("Nombre del producto: ").strip()
            if not name_product.isalpha():
                print(warning + "⚠ Nombre inválido." + reset)
                continue

            try:
                price = float(input("Precio del producto: "))
                if price <= 0:
                    print(warning + "⚠ El precio debe ser mayor a 0." + reset)
                    continue
            except:
                print(warning + "⚠ Precio inválido." + reset)
                continue

            try:
                amount = int(input("Cantidad del producto (mínimo 5): "))
            except:
                print(warning + "⚠ Cantidad inválida." + reset)
                continue

            add_products(inventary, name_product, price, amount)

        case 2:
            name_product = input("Nombre del producto a buscar: ").strip()
            search_product(inventary, name_product)

        case 3:
            name_product = input("Nombre del producto a cambiar el precio: ").strip()
            if name_product in inventary:
                try:
                    new_price = float(input("Nuevo precio: "))
                    if new_price > 0:
                        add_price(inventary, name_product, new_price)
                        print(success + "✅ Precio actualizado." + reset)
                    else:
                        print(danger + "❌ El precio debe ser mayor que 0." + reset)
                except:
                    print(warning + "⚠ Precio inválido." + reset)
            else:
                print(danger + "❌ Producto no encontrado." + reset)

        case 4:
            name_product = input("Nombre del producto a eliminar: ").strip()
            delete_product(inventary, name_product)

        case 5:
            total = calculate_total_value(inventary)
            print(success + f"💰 El valor total del inventario es: ${total:.2f}" + reset)

        case 6:
            print(success + "Gracias por usar el programa. ¡Hasta pronto!" + reset)
            break