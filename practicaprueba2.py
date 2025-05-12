dict_students_={
101 : {"nombre": "Miguel Angel Arias Marin","edad": "17","nota": "2,5"},
102 : {"nombre": "Cristian Perez Lopez","edad": "32","nota": "5.0"},
103 : {"nombre": "Juan Fernando Puerta Vasquez","edad": "53","nota": "4.3"},
104 : {"nombre": "Sebastian Restrepo Garcia","edad": "17","nota": "2.9"},
105 : {"nombre": "Esteban Cordoba Puerta","edad": "16","nota": "3,2"}
     
}
     


print("==================================")
print("       Estudiantes Universidad     ")
print("==================================")

while True:
    print("1.)Añadir estudiantes")
    print("2. Buscar estudiantes")
    print("3. Subir información del estudiante")
    print("4. Eliminar estudiantes")
    print("5. Calcular promedio")

    escoger_menu=(input(" Elige la opcion que vayas a hacer "))
    if escoger_menu.isdigit() and 1<= int(escoger_menu) <=5:
            escoger_menu=int(escoger_menu)
    else:
        print("\nSelecciona las opciones recomendadas\n")
        
            
    
    match escoger_menu:
         
        case 1:

            while True:
                nombre_estudiante=input("Agregue nombre del estudiante: ")  
                if nombre_estudiante.replace(" ", "").isalpha():
                     break
                else:
                     print("Invalido")
        
            while True:
                    edad_estudiante=input("Digita edad del estudiante")
                    if edad_estudiante.isdigit() and  int(edad_estudiante) > 0:
                        edad_estudiante=int(edad_estudiante)
                        break
                    else:
                         print("Ingrese edad valida ")
                
            while True:
                id_estudiante = input("Agrega la cédula o ID del estudiante: ")
                if id_estudiante.isdigit():
                    break
                else: 
                    print("Inválido")
            while True: 
                 nota_estudiante=(input("Digite la nota del estudiante"))
                 if nota_estudiante and float(nota_estudiante) >0:
                      nota_estudiante=float(nota_estudiante)
                      break
                 else:
                      print("Ingrese una nota valida")
           


            dict_students_[int(id_estudiante)]={"nombre":nombre_estudiante,"edad":edad_estudiante,"nombre":nombre_estudiante,"nota":nota_estudiante}
            print("Has agregado el estudiante eficazmente")
            print(dict_students_)
    

        case 2:
              while True:
                buscar_estudiantes=input("ingrese el id que desea buscar")
                if buscar_estudiantes.isdigit():
                   buscar_estudiantes=int(buscar_estudiantes)
                
                   if buscar_estudiantes in dict_students_:
                        id_estudiante= dict_students_[buscar_estudiantes]
                        print("\n Estudiante encontrado:")

                        print ("identificacion encontrada es: ", id_estudiante)
                        print(f"Nombre: {id_estudiante['nombre']}")
                        print(f"Edad: {id_estudiante['edad']}")
                        print(f"Nota: {id_estudiante['nota']}")
                        break
                   else:
                        print("El estudiante no esta en la lista, si quiere agregarlo en el menu puede hacerlo")
                else:
                     print("ID invalido. Debe ser numero")
    