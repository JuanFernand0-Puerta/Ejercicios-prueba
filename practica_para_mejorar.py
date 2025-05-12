lista=[]

print("==================================")
print("        Que deseas hacer          ")
print("==================================")

while True:
    print("1.)Ingresar temperaturas registradas (separadas por comas)")
    print("2.)Calcular la temperatura promedio ")
    print("3.)Ver temperaturas superiores a un valor ingresado")
    print("4.)Buscar cuántas veces se repite una temperatura específica")
    print("5.)Salir")

    escoger=(input("Esoge una de las opciones(1,5)"))
    
    if escoger=="1":
        while True:
            temperatura=input("Que temperaturas en rando de (-30,50) quieres agregar separadas por comas")
            temperatura_separada= temperatura.split(',') 
            
            for temp in temperatura_separada:
                try:
                    temp=float(temp.strip())
                    if temp >=- 30 and temp <= 50:
                        lista.append(temp)
                    else:
                        print(f"la temperatura debe estar dentro del rango (-30,50){temp}")
                except ValueError:
                        print(f"Debes ingresar un valor valido{temp}")
            seguir=input("Quieres agregar mas temperaturas (1=si  2=no)")
            if seguir =="2":
                break
            elif seguir == "1":
                continue
            else:
                print("seleccione una opcion valida")
    

    elif escoger=="2":
        while True:
                if len in (lista) ==0:
                     print("No hay temperaturas ingresadas")
                else:
                     suma= 0
                     for temperaturas in lista:
                          suma += temperaturas
                promedio= suma /len(lista)
                print(f"el promedio de las calificaciones es:{promedio}")                
                     
            
        


            


