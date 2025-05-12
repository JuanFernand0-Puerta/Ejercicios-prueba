almacenar los productos:

python
Copiar
Editar
# CRUD de productos con restricción mínima de 5 productos

productos = []

def crear_productos():
    print("\n--- Agregar productos ---")
    nuevos = []
    while True:
        nombre = input("Ingrese el nombre del producto (o escriba 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        nuevos.append(nombre)

    if len(nuevos) < 5:
        print("❌ Debe ingresar al menos 5 productos.")
    else:
        productos.extend(nuevos)
        print("✅ Productos agregados correctamente.")

def listar_productos():
    print("\n--- Lista de productos ---")
    if not productos:
        print("No hay productos registrados.")
    else:
        for i, prod in enumerate(productos, 1):
            print(f"{i}. {prod}")

def actualizar_producto():
    listar_productos()
    if not productos:
        return
    try:
        index = int(input("Ingrese el número del producto a actualizar: ")) - 1
        if 0 <= index < len(productos):
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            productos[index] = nuevo_nombre
            print("✅ Producto actualizado.")
        else:
            print("❌ Índice inválido.")
    except ValueError:
        print("❌ Entrada no válida.")

def eliminar_producto():
    listar_productos()
    if not productos:
        return
    try:
        index = int(input("Ingrese el número del producto a eliminar: ")) - 1
        if 0 <= index < len(productos):
            eliminado = productos.pop(index)
            print(f"✅ Producto '{eliminado}' eliminado.")
        else:
            print("❌ Índice inválido.")
    except ValueError:
        print("❌ Entrada no válida.")

def menu():
    while True:
        print("\n--- Menú CRUD ---")
        print("1. Agregar productos (mínimo 5)")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_productos()
        elif opcion == '2':
            listar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion