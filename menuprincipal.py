
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


while True:
    print("\n===== MENÚ PRINCIPAL - CLÍNICA =====")
    print("1. Registrar nuevo paciente")
    print("2. Mostrar pacientes")
    print("3. Salir")
    print("4. Modificar paciente")

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