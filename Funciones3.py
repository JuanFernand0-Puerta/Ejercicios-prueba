warning = "\033[93m"
danger = "\033[91m"
success = "\033[92m"
reset = "\033[0m"



# Función para agregar un producto al inventario
def agregar_productos(inventario,nombre, precio, cantidad):
    inventario[nombre] = {"precio": precio, "cantidad": cantidad}
    print(success + "Has agregado el producto eficazmente" + reset)
    print(inventario)

# Función para actualizar el precio de un producto
def agregar_precio(inventario,nombre, precio_nuevo):
    inventario[nombre]['precio'] = precio_nuevo
    print(success + "Has agregado el precio nuevo" + reset)
    print(inventario)

# Función para buscar un producto en el inventario
def buscar_producto(inventario,nombre):
    # Verifica si el producto está en el inventario
    if nombre in inventario:
        # Imprime un mensaje de éxito en verde con el nombre del producto
        print(success + f"Producto encontrado: {nombre}" + reset)
        # Muestra el precio y la cantidad del producto
        print(f"Precio: {inventario[nombre]['precio']} -- Cantidad: {inventario[nombre]['cantidad']}")
    # Si el producto no está, muestra una advertencia en amarillo
    else:
        print(warning + "Ese producto no se encuentra en el inventario; agréguelo en el menú" + reset)