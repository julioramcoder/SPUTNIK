#----------------------------------------------------------------------------------------------------------------------------------------------------
#
#                         Funciones para inicializar una lista de pacientes

import json


with open("pacientes.json", "r") as archivo:
    listaDePacientes  = json.load(archivo)

def actializarListaDePacientes():
    with open("pacientes.json", "w") as archivo:
        json.dump(listaDePacientes,archivo,indent=4)

#----------------------------------------------------------------------------------------------------------------------------------------------------
#                           Funciones 
#----------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------
#                   Funciones para agregar a un paciente, verificando que la id sea única

def crearNuevoPaciente(_id, _nombre, _edad,_genero,_diagnostico, _historial):
    nuevoPaciente = {"id": _id ,"nombre" : _nombre, "edad" : _edad, "genero" : _genero, "diagnostico" : _diagnostico, "historial" : _historial}
    return nuevoPaciente

def encontrarPacienteID(_id):
    for paciente in listaDePacientes:
        if paciente["id"] == _id:
            return True , paciente
            
    return False , None

def addNuevoPaciente(_id, _nombre, _edad,_genero,_diagnostico, _historial):
    encontrado = encontrarPacienteID(_id)
    encontrado = encontrado[0]
    if not encontrado:
        nuevoPaciente = crearNuevoPaciente(_id, _nombre, _edad,_genero,_diagnostico, _historial)
        listaDePacientes.append(nuevoPaciente)
        actializarListaDePacientes()
    else: print("El paciente actualmente se encuentra registrado")



#---------------------------------------------------------------------------------------------------------------------------------------------------
#            Funciones para filtrar lista de pacientes        
def filtrarPorID(_id):
    encontrado = encontrarPacienteID(_id)
    if encontrado[0]:
       
        print(f"Nombre: {encontrado[1]['nombre']}")
        print(f"Identificación: {encontrado[1]['id']}")
        print(f"Edad: {encontrado[1]['edad']}")
        print(f"Genero: {encontrado[1]['genero']}")
        print(f"Diagnostico: {encontrado[1]['diagnostico']}")
        print(f"Historial: {encontrado[1]['historial']}")

        
        

    else: print("No encontrado! Por favor ingresa ID correcto")



def filtrarPorNombre(_nombre):
    listaFiltrada = []
    for paciente in listaDePacientes:
        if paciente["nombre"] == _nombre:
            listaFiltrada.append(paciente)
    if listaFiltrada:
        for paciente in listaFiltrada:
            print(paciente)
        
    else: print(f"No hay pacientes con el nombre: {_nombre}")
            

def filtrarPorDiagnostico(_diagnostico):
    listaFiltrada = []
    for paciente in listaDePacientes:
        if paciente["diagnostico"] == _diagnostico:
            listaFiltrada.append(paciente)
    if listaFiltrada:
        
        for paciente in listaFiltrada:
            print(paciente)
    else: print(f"No hay pacientes con el diagnóstico de: {_diagnostico}")

#---------------------------------------------------------------------------------------------------------------------------------------------------
#        Funciones eliminar paciente

def eliminarPaciente(_id):
    pacienteEliminar = encontrarPacienteID(_id)
    if pacienteEliminar[0] == True:
        print(f"paciente: {pacienteEliminar[1]['nombre']} eliminado correctamente ")
        listaDePacientes.remove(pacienteEliminar[1])
        
        actializarListaDePacientes()

def eliminarPacienteMenu():
    
    _id = ""
    while True:
        try:
            _id = int(input("ID del paciente a eliminar: "))
            break
        except ValueError:
            print("Ingrese una ID correcta")
    eliminarPaciente(_id)


#--------------------------------------------------------------------------------------------------------------------------------------------------
#       Funciones modificar paciente


def modificar_paciente():
    print("\n--- Modificar datos de un paciente ---")
    if not listaDePacientes:
        print("No hay pacientes registrados.")
        input("Presione Enter para volver al menú...")
        return

    try:
        id_paciente = int(input("Ingrese el ID del paciente a modificar: ").strip())
    except ValueError:
        print("El ID debe ser un número entero.")
        input("Presione Enter para volver al menú...")
        return

    for p in listaDePacientes:
        if p["id"] == id_paciente:
            print(f"\nPaciente encontrado: {p['nombre']}")
            print(f"Edad actual: {p['edad']}")
            print(f"Diagnóstico actual: {p['diagnostico']}")
            print(f"Historial actual: {', '.join(p['historial']) if p['historial'] else 'Sin historial'}")

            print("\n¿Qué desea modificar?")
            print("1. Edad")
            print("2. Diagnóstico")
            print("3. Agregar entrada al historial")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                nueva_edad = input("Ingrese la nueva edad: ")
                confirmar = input(f"¿Desea cambiar la edad de {p['edad']} a {nueva_edad}? (s/n): ").strip().lower()
                if confirmar == "s":
                    p["edad"] = nueva_edad
                    print("Edad actualizada correctamente.")
                    actializarListaDePacientes()
                else:
                    print("Cambio cancelado.")

            elif opcion == "2":
                nuevo_diagnostico = input("Ingrese el nuevo diagnóstico: ")
                confirmar = input(f"¿Desea cambiar el diagnóstico de '{p['diagnostico']}' a '{nuevo_diagnostico}'? (s/n): ").strip().lower()
                if confirmar == "s":
                    p["diagnostico"] = nuevo_diagnostico
                    print("Diagnóstico actualizado correctamente.")
                    actializarListaDePacientes()
                else:
                    print("Cambio cancelado.")

            elif opcion == "3":
                nueva_entrada = input("Ingrese la nueva entrada para el historial: ")
                confirmar = input(f"¿Desea agregar '{nueva_entrada}' al historial? (s/n): ").strip().lower()
                if confirmar == "s":
                    p["historial"].append(nueva_entrada)
                    print("Nueva entrada agregada al historial.")
                    actializarListaDePacientes()
                else:
                    print("Cambio cancelado.")
            else:
                print("Opción inválida.")
            input("Presione Enter para volver al menú...")
            return

    print("No se encontró ningún paciente con ese ID.")
    input("Presione Enter para volver al menú...")

#def modificarPaciente(_paciente,_cualidad):

#------------------------------------------------------------------------------------------------------------------------------------------------
#      Función imprimir lista de pacientes

def mostrar_pacientes():
    print("\n--- Lista de pacientes registrados ---")
    if not listaDePacientes:
        print("No hay pacientes registrados.")
        return
    
    for p in listaDePacientes:
        print(f"\nID: {p['id']}")
        print(f"Nombre: {p['nombre']}")
        print(f"Edad: {p['edad']}")
        print(f"Género: {p['genero']}")
        print(f"Diagnóstico: {p['diagnostico']}")
        print(f"Historial: {', '.join(p['historial']) if p['historial'] else 'Sin historial'}")
#----------------------------------------------------------------------------------------------------------------------------
#         Funcion moduloBusqueda

def menuBusqueda():
    print ("Señor usuario, a continuacion podra observar las opciones para buscar a un paciente.\n")
    
    "==============DISPONIBILIDAD================"
        
    print("1. Nombre completo del paciente.\n   ") 
        
    print("2. ID del paciente.\n ")
        
    print("3. Diagnostico del paciente.\n  ")
        
    while True:
        
        opcion = (input("Elige una opción: "))
        
        
          
        if opcion == "1":
            nombre_completo= input("\nPor favor ingrese su numbre completo: ")
            print (f"\nBuscando paciente que con el nombre {nombre_completo}....Espere un momento por favor.\n")
            filtrarPorNombre(nombre_completo)
            break
            
    
        elif opcion == "2":
            try:
                ID = int(input("Ingrese el ID del paciente a modificar: ").strip())
            except ValueError:
                print("El ID debe ser un número entero.")
                return
        
            print (f"\nBuscando paciente que con el ID {ID}...Espere un momento por favor.\n")
            filtrarPorID(ID)
            break
            
            
                
        
        elif opcion == "3":
            Diagnostico= input("\nPor favor ingrese su diagnostico para realizar un filtro entre todos los registrados: ")
            print (f"\nBuscando pacientes que con diagnostico coincidente con {Diagnostico}...Espere un momento por favor.\n")
            filtrarPorDiagnostico(Diagnostico)
            break

        
        else:
            print("\n=======ERROR!!!, El sistena no reconoce este valor,por favor vuelva a ingresar=======\n")

#-------------------------------------------------------------------------------------------------------------------------
#           Menu funciones registros
#Inicio de la función crear y mostrar los reportes del sistema 
def generar_reportes():
#Si en la lista de pacientes no se encuentra nada nos avisara que no hay ningun reporte.   
    print("\n--- Módulo de Reportes ---")
    if not listaDePacientes:
        print("No hay pacientes registrados para generar reportes.")
        input("Presione Enter para volver al menú...")
        return
#Se muestra el submenu de reportes
    print("Seleccione el reporte que desea generar:")
    print("1. Pacientes mayores de 60 años")
    print("2. Diagnósticos más frecuentes")
    print("3. Cantidad total de pacientes")
    print("4. Mostras pacientes")
#el metodo strip() nos elimina los espacios si se ingresan erroneamente
    opcion_reporte = input("Seleccione una opción: ").strip()

    if opcion_reporte == "1":
        print("\n--- Reporte: Pacientes mayores de 60 años ---")
        pacientes_mayores = []
        for p in listaDePacientes:
            try:
                
                if int(p["edad"]) > 60:
                    pacientes_mayores.append(p)
            except ValueError:
                
                print(f"Advertencia: El paciente ID {p['id']} tiene una edad no numérica ('{p['edad']}') y no será incluido.")

        if not pacientes_mayores:
            print("No se encontraron pacientes mayores de 60 años.")
        else:
            print(f"Se encontraron {len(pacientes_mayores)} pacientes mayores de 60 años:")
            for p in pacientes_mayores:
                print(f"  - ID: {p['id']}, Nombre: {p['nombre']}, Edad: {p['edad']}, Diagnóstico: {p['diagnostico']}")

    elif opcion_reporte == "2":
        print("\n--- Reporte: Diagnósticos más frecuentes ---")
        contador_diagnosticos = {}
        for p in listaDePacientes:
            diagnostico = p["diagnostico"].strip().title()
            if diagnostico: 
                contador_diagnosticos[diagnostico] = contador_diagnosticos.get(diagnostico, 0) + 1
        
        if not contador_diagnosticos:
            print("No hay diagnósticos registrados para mostrar.")
        else:
            diagnosticos_ordenados = sorted(contador_diagnosticos.items(), key=lambda item: item[1], reverse=True)
            print("Frecuencia de diagnósticos:")
            for diagnostico, cantidad in diagnosticos_ordenados:
                print(f"  - {diagnostico}: {cantidad} paciente(s)")

    elif opcion_reporte == "3":
        print("\n--- Reporte: Cantidad total de pacientes ---")
        total_pacientes = len(listaDePacientes)
        print(f"Actualmente hay un total de {total_pacientes} pacientes registrados en el sistema.")

    elif opcion_reporte == "4":
        print("\n--- Reporte: Informacion de Pacientes ---")
        mostrar_pacientes() 

    else:
        print("Opción de reporte no válida.")
    
    input("\nPresione Enter para volver al menú...")

#--------------------------------------------------------------------------------------------------------------
def agregar_paciente():
    print("\n--- Registrar nuevo paciente ---")
    try:
        id_paciente = int(input("Ingrese ID del paciente: ").strip())
    except ValueError:
        print("El ID debe ser un número entero.")
        return
    
    for paciente in listaDePacientes:
        if paciente["id"] == id_paciente:
            print("Este ID ya existe. No se puede registrar un duplicado.")
            return
    
    nombre = input("Ingrese nombre del paciente: ")
    edad = input("Ingrese edad del paciente: ")
    genero = input("Ingrese género del paciente: ")
    diagnostico = input("Ingrese diagnóstico: ")
    historial = []

    while True:
        entrada = input("Agregar entrada al historial (o presione Enter para terminar): ")
        if entrada == "":
            break
        historial.append(entrada)
    
    addNuevoPaciente(id_paciente,nombre,edad,genero,diagnostico,historial)
    print("Paciente registrado correctamente.\n")









while True:
    print("\n===== MENÚ PRINCIPAL - CLÍNICA =====")
    print("1. Registrar nuevo paciente")
    print("2. Buscar paciente")
    print("3. Modificar paciente")
    print("4. Eliminar Paciente")
    print("5. Generar Reportes")
    print("6. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_paciente()
    elif opcion == "2":
        print("Buscar paciente")
        menuBusqueda()
        
        
    elif opcion == "3":
        print("Modificando pacientes")
        modificar_paciente()
        
    elif opcion == "4":
        print("Eliminar pacientes")
        
        eliminarPacienteMenu()
        
    elif opcion == "5":
        print("Generar reportes")
        generar_reportes()

    elif opcion == "6":
        print("Gracias por visitarnos");break

    else:
        print("Opción inválida")
#--------------------------------------------------------------------------------------------------------       

        
#-----------------------------------------------------------------------------------------------------------------------------------     
