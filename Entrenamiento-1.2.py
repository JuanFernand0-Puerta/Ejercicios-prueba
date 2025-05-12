# Lista para almacenar las calificaciones
lista = []

# Mostrar el menú principal
print("========================================================")
print("            Bienvenido, ¿qué desea hacer?               ")
print("========================================================")

# Iniciar el bucle para mostrar el menú
while True:
    # Mostrar opciones del menú
    print("\nMenú de opciones:")
    print("1.) Ingresar calificaciones")
    print("2.) Calcular promedio")
    print("3.) Ver calificaciones mayores")
    print("4.) Verificar calificaciones repetidas")
    print("5.) Salir")

    # Solicitar que el usuario elija una opción
    opcion = input("Escoge una opción (1-5): ")

    if opcion == "1":
        # Si elige 1, ingresar calificaciones
        while True:
            calificaciones = input("Ingresa las calificaciones separadas por coma: ")
            calificaciones_separadas = calificaciones.split(",")  # Separar calificaciones

            # Procesar cada calificación
            for calificacion in calificaciones_separadas:
                try:
                    calificacion = int(calificacion.strip())  # Convertir a entero
                    if calificacion >= 0 and calificacion <= 100:
                        lista.append(calificacion)  # Agregar calificación a la lista
                    else:
                        print(f"{calificacion}: La calificación debe estar entre 0 y 100")
                except ValueError:
                    print(f"{calificacion}: No es un número válido")  # Si no es un número válido

            seguir = input("¿Quieres agregar más calificaciones? (1 = sí, 2 = no): ")
            if seguir == "2":
                break  # Salir del bucle de ingresar calificaciones
            elif seguir == "1":
                continue  # Continuar ingresando más calificaciones
            else:
                print("Opción no válida, volviendo al menú principal.")
                break

    elif opcion == "2":
        # Si elige 2, calcular el promedio
        if len(lista) == 0:
            print("Aún no hay calificaciones ingresadas.")
        else:
            suma = 0
            for calificacion in lista:
                suma += calificacion  # Sumar todas las calificaciones
            promedio = suma / len(lista)  # Calcular promedio
            print(f"El promedio de las calificaciones es: {promedio}")

    elif opcion == "3":
        # Si elige 3, contar calificaciones mayores a un valor
        if len(lista) == 0:
            print("Aún no hay calificaciones ingresadas.")
        else:
            try:
                valor = int(input("Ingresa un valor para comparar: "))
                contador = 0
                for calificacion in lista:
                    if calificacion > valor:
                        contador += 1  # Contar las calificaciones mayores al valor
                print(f"Hay {contador} calificaciones mayores que {valor}.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    elif opcion == "4":
        # Si elige 4, verificar cuántas veces se repite una calificación
        if len(lista) == 0:
            print("Aún no hay calificaciones ingresadas.")
        else:
            try:
                valor = int(input("Ingresa la calificación a buscar: "))
                contador = 0
                for calificacion in lista:
                    if calificacion == valor:
                        contador += 1  # Contar cuántas veces aparece la calificación
                if contador > 0:
                    print(f"La calificación {valor} aparece {contador} veces.")
                else:
                    print(f"La calificación {valor} no está en la lista.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

    elif opcion == "5":
        # Si elige 5, salir del programa
        print(" Hasta luego.")
        break

    else:
        # Si elige una opción no válida
        print("Opción no válida. Intenta de nuevo.")