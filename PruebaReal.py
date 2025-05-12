# Códigos ANSI para colorear mensajes en la consola
warning = "\033[93m"
danger = "\033[91m"
success = "\033[92m"
reset = "\033[0m"

#Diccionario sin nada para agregar productos
inventary={}
productos=[]


#funcion para agregar producto al inventario (5 minimo)
def add_products(inventary,name_product,price,amount):
    if amount <5:
        print(danger+"Debe agregar al menos 5 productos")
        return
    

    if name_product in inventary:
        inventary[name_product]["cantidad"] += amount
        inventary[name_product][price] = price
    else:
        inventary[name_product]={"precio": price, "cantidad": amount}
    print(success+f"producto{name_product} agregado correctamente con {amount} unidades."+ reset)

#funcion para actualizar el precio
def add_price (inventary, name_product_, add_new_price):
    inventary[name_product]["price"]= add_new_price

def search_product(inventary,name_product):
    if name_product in inventary:
       info= inventary[name_product]
       print(success + f"producto encontrado:{name_product}, price:{info['price']}, amount{info['amount']}"+ reset)


#bucle principal con el menu
while True:
    print("=============================")
    print("    Que deseas hacer hoy     ")
    print("\n=============================")

    print("1.)Añadir productos al inventario (minimo 5) : ")
    print("2.)Consultar productos en inventario : ")
    print("3.)Actualizar precios de productos :") 
    print("4.)Eliminar productos del inventario :")
    print("5.)Calcular el valor total del inventario :")
    print("6.)Salir del programa")


    #Hace que la opcion del menú funcione
    choose_menu =input("Escoge una de las opciones (1,6)")
    if choose_menu.isdigit() and 1 <= int (choose_menu) <=6:
        choose_menu = int (choose_menu)
    else:
        print(warning +"Opcion invalida, intenta de nuevo"+ reset)
        continue
    
    match choose_menu:
        case 1:
            while True:
                name_product=input("Nombre de el producto")
                if name_product.replace("","").isalpha():
                    
                    inventary.update(name_product)
                    if len(inventary) <5:
                        print("debes ingresar al menos 5 productos")
                    else:
                        productos.extend(inventary)
                        print(success+"Productos agregados correctamente"+reset)

                while True:
                    price=input("Precio del producto")
                    price=float(price)
                    if price >0:
                        break
                    else:
                        print(warning+ "el precio debe ser mayor que 0" +reset)
            
                    print (warning +"ingresa un valor valido para el precio"+ reset)
                while True:
                        amount=input("Cantidad del producto")

                        if amount and amount.isdigit() and float(amount) > 0.0:
                            amount=float(amount)
                            break
                        else:
                            print(danger+"debe ingresar mas de 0 cantidades"+ reset)
                        
        case 2:
            search_product= input("Nombre del producto a buscar")
            if name_product in inventary:
                info= inventary[name_product]
                print(success + f"producto encontrado:{name_product}, price:{info['price']}, amount{info['amount']}"+ reset)

        
        case 3:
            name_product=input("Nombre del producto al que desea cambiar el precio: ")
            if name_product in inventary:
                while True:
                    add_new_price=input("Dame el precio nuevo")
                    if add_new_price > 0:
                        add_new_price(inventary,name_product,price)
                        print(success+f"precio actualizado correctamente: {inventary[name_product]}"+ reset )
                        break
                    else:
                        print(danger+"el precio debe ser mayor que 0."+reset)
            else:
                print(warning+"ese producto no existe, debes agregarlo desde la opcion 1"+ reset)


        case 4:
            while True:
                delete_product=input("Escriba el nombre del producto que desea eliminar")
                if delete_product not in name_product:
                    break
                index=input("ingrese el nombre del producto que desea eliminar")
                if index in inventary[name_product]:
                    delete_product=name_product.pop(index)
                    print(f"producto'{delete_product}'eliminado")  
                else:
                    print("indice invalido")
                
        case 5:
                calculate_total=
                total=print("el total acumulado es ", calculate_total)
            
        case 6:
            print("Gracias por usar el programa")
            break