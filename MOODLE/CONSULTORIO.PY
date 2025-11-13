#Vamos a buscar el paciente 

print("\n=========Bienvenido a la clinica traumas y fracturas========\n") 


    
print ("Señor usuario, a continuacion podra observar las ocpciones para buscar a un paciente.\n")
    
"==============DISPONIBILIDAD================"
    
print("1. Nombre parcial del paciente.\n ")   
    
print("2. Nombre completo del paciente.\n   ") 
    
print("3. ID del paciente.\n ")
    
print("4. Diagnostico del paciente.\n  ")
    
while True:
    
    opcion = int(input("Teniendo en cuenta las ocpciones anteriores, ¿Con cual desea realizar la busqueda del paciente?: "))
    
    if opcion > 4 or opcion < 1:
        print("\n=======ERROR!!!, El sistena no reconoce este valor,por favor vuelva a ingresar=======\n")
        
    elif opcion == 1:
        nombre_parcial= input("\nPor favor ingrese su numbre parcial: ")
        print (f"\nBuscando paciente que con nombre parcial{nombre_parcial}...Espere un momento por favor.\n")
        print (f"El paciente {nombre_parcial} ha sido encontrado en la base de datos, procederemos con su consulta...")
    
    
    elif opcion == 2:
        nombre_completo= input("\nPor favor ingrese su numbre completo: ")
        print (f"\nBuscando paciente que con el nombre {nombre_completo}....Espere un momento por favor.\n")
        print (f"El paciente {nombre_completo} ha sido encontrado en la base de datos, procederemos con su consulta...")
 
    elif opcion == 3:
        ID= int(input("\nPor favor ingrese su numbre parcial: "))
        print (f"\nBuscando paciente que con el ID {ID}...Espere un momento por favor.\n")
        print (f"El paciente {ID} ha sido encontrado en la base de datos, procederemos con su consulta...")
            
     
    elif opcion == 4:
        Diagnostico= input("\nPor favor ingrese su diagnostico para realizar un filtro entre todos los registrados: ")
        print (f"\nBuscando paciente que con diagnostico coincidente con {Diagnostico}...Espere un momento por favor.\n")
        print (f"El paciente {Diagnostico} ha sido encontrado en la base de datos, procederemos con su consulta...\n")
        
    break