'''Descripción del problema:

Vas a simular un cajero automático. El sistema debe permitir al usuario:

Ver el saldo de su cuenta.

Retirar dinero.

Depositar dinero.

Ver el historial de movimientos.

Salir del programa.
'''
movimientos=[]
saldo=0
usuario={
1025764147:{
    "nombre":"Juanfernando",
"apellido":"Puerta"
}
}


print("==================================================")
print("             Que desea hacer hoy                  ")
print("==================================================")


while True:
    
    print("1.Depositar dinero.")
    print("2.Ver el saldo de su cuenta.")
    print("3.Retirar dinero.")
    print("4.Ver el historial de movimientos.")
    print("5.Salir del programa")


    escoger=input("escoge una de las opciones (1,5)")



    if escoger=="1":
        while True:
            deposito=float (input("Cuanto dinero desea depositar hoy: "))
            if deposito > 0:
                saldo= saldo + deposito
                movimientos.append(deposito)
                print ("usted ha depositado", deposito)
                break
            else:
                print("ingrese un valor valido")
                

        
        print(saldo)


    elif escoger == "2":
         
        print("El saldo que usted tiene acumulado es: ",saldo)
        movimientos.append(saldo)
        break

    elif escoger =="3":
        retirar=(input("Cuanto dinero desea retirar"))
        if  retirar <= saldo:
           movimientos.append(retirar)
           saldo = saldo-float(retirar)
           print("Retiro con exito su saldo actual es ", saldo)
        else:
            print("saldo insuficiente")
    
    elif escoger =="4":
        print ("Los movimientos realizado fueron: ", movimientos)
        if movimientos:
            for i in movimientos:
                print("-",i)
            else:
                print("aun no se han registrado movimientos")


    
    elif escoger =="5":
        print("Gracias por usar el programa")

        break
    else:
        print("Opcion no valida. intente de nuevo")

            

        

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    '''
    for depositos in deposito:
        try:
            depositos = float(depositos)
            if depositos >=0:
                deposito.append (depositos)
                break  # Agregar deposito a la lista
            else:
                print(f"{deposito}: El deposito debe estar entre 0 y infinito")
        except ValueError:
            print(f"{depositos}: No es un número válido")  # Si no es un número válido    
    '''
            
            





