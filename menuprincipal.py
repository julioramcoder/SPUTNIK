
#----------------------------------------------------------------------------------------------------------------------------------------------------
#                           Funciones 
#----------------------------------------------------------------------------------------------------------------------------------------------------

listaDePacientes = []

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
    else: print("El paciente actualmente se encuentra registrado")
    

#---------------------------------------------------------------------------------------------------------------------------------------------------
#            Funciones para filtrar lista de pacientes        

def filtrarPorNombre(_nombre):
    listaFiltrada = []
    for paciente in listaDePacientes:
        if paciente["nombre"] == _nombre:
            listaFiltrada.append(paciente)
    if listaFiltrada:
        return listaFiltrada
    else: print(f"No hay pacientes con el nombre: {_nombre}")
            

def filtrarPorDiagnostico(_diagnostico):
    listaFiltrada = []
    for paciente in listaDePacientes:
        if paciente["diagnostico"] == _diagnostico:
            listaFiltrada.append(paciente)
    if listaFiltrada:
        return listaFiltrada
    else: print(f"No hay pacientes con el diagnóstico de: {_diagnostico}")

#---------------------------------------------------------------------------------------------------------------------------------------------------
#        Funciones eliminar paciente

def eliminarPaciente(_id):
    pacienteEliminar = encontrarPacienteID(_id)
    if pacienteEliminar[0] == True:
        listaDePacientes.remove(pacienteEliminar[1])

#--------------------------------------------------------------------------------------------------------------------------------------------------
#       Funciones modificar paciente

#def modificarPaciente(_paciente,_cualidad):

pacientes = []  

def agregar_paciente():
    print("\n--- Registrar nuevo paciente ---")
    try:
        id_paciente = int(input("Ingrese ID del paciente: ").strip())
    except ValueError:
        print("El ID debe ser un número entero.")
        return
    
    for paciente in pacientes:
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
    
    nuevo_paciente = {
        "id": id_paciente,
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "diagnostico": diagnostico,
        "historial": historial
    }

    pacientes.append(nuevo_paciente)
    print("Paciente registrado correctamente.\n")


def mostrar_pacientes():
    print("\n--- Lista de pacientes registrados ---")
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    
    for p in pacientes:
        print(f"\nID: {p['id']}")
        print(f"Nombre: {p['nombre']}")
        print(f"Edad: {p['edad']}")
        print(f"Género: {p['genero']}")
        print(f"Diagnóstico: {p['diagnostico']}")
        print(f"Historial: {', '.join(p['historial']) if p['historial'] else 'Sin historial'}")


def modificar_paciente():
    print("\n--- Modificar datos de un paciente ---")
    if not pacientes:
        print("No hay pacientes registrados.")
        input("Presione Enter para volver al menú...")
        return

    try:
        id_paciente = int(input("Ingrese el ID del paciente a modificar: ").strip())
    except ValueError:
        print("El ID debe ser un número entero.")
        input("Presione Enter para volver al menú...")
        return

    for p in pacientes:
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
                else:
                    print("Cambio cancelado.")

            elif opcion == "2":
                nuevo_diagnostico = input("Ingrese el nuevo diagnóstico: ")
                confirmar = input(f"¿Desea cambiar el diagnóstico de '{p['diagnostico']}' a '{nuevo_diagnostico}'? (s/n): ").strip().lower()
                if confirmar == "s":
                    p["diagnostico"] = nuevo_diagnostico
                    print("Diagnóstico actualizado correctamente.")
                else:
                    print("Cambio cancelado.")

            elif opcion == "3":
                nueva_entrada = input("Ingrese la nueva entrada para el historial: ")
                confirmar = input(f"¿Desea agregar '{nueva_entrada}' al historial? (s/n): ").strip().lower()
                if confirmar == "s":
                    p["historial"].append(nueva_entrada)
                    print("Nueva entrada agregada al historial.")
                else:
                    print("Cambio cancelado.")
            else:
                print("Opción inválida.")
            input("Presione Enter para volver al menú...")
            return

    print("No se encontró ningún paciente con ese ID.")
    input("Presione Enter para volver al menú...")

def generar_reportes():
   
    print("\n--- Módulo de Reportes ---")
    if not pacientes:
        print("No hay pacientes registrados para generar reportes.")
        input("Presione Enter para volver al menú...")
        return

    print("Seleccione el reporte que desea generar:")
    print("1. Pacientes mayores de 60 años")
    print("2. Diagnósticos más frecuentes")
    print("3. Cantidad total de pacientes")
    opcion_reporte = input("Seleccione una opción: ").strip()

    if opcion_reporte == "1":
        print("\n--- Reporte: Pacientes mayores de 60 años ---")
        pacientes_mayores = []
        for p in pacientes:
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
        for p in pacientes:
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
        total_pacientes = len(pacientes)
        print(f"Actualmente hay un total de {total_pacientes} pacientes registrados en el sistema.")

    else:
        print("Opción de reporte no válida.")
    
    input("\nPresione Enter para volver al menú...")


while True:
    print("\n===== MENÚ PRINCIPAL - CLÍNICA =====")
    print("1. Registrar nuevo paciente")
    print("2. Mostrar pacientes")
    print("3. Salir")
    print("4. Modificar paciente")
    print("Generar Reportes")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_paciente()
    elif opcion == "2":
        mostrar_pacientes()
    elif opcion == "3":
        print("Saliendo del sistema... Hasta pronto.")
        break
    elif opcion == "4":
        modificar_paciente()
    else:
        print("Opción inválida. Intente nuevamente.")
#--------------------------------------------------------------------------------------------------------       
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
        
#-----------------------------------------------------------------------------------------------------------------------------------     
