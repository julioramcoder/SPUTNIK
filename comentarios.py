#----------------------------------------------------------------------------------------------------------------------------------------------------
#
#                         Funciones para leer y actualizar json

import json

try:
    with open("pacientes.json", "r") as archivo:
        listaDePacientes = json.load(archivo)
except (json.JSONDecodeError, FileNotFoundError):
    listaDePacientes = []


def actializarListaDePacientes():
    with open("pacientes.json", "w") as archivo:
        json.dump(listaDePacientes,archivo,indent=4)

#----------------------------------------------------------------------------------------------------------------------------------------------------
#                           Funciones 
#----------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------------------------------------------------------------------
#                   Funciones para agregar a un paciente, verificando que la id sea única

# Acontinuacion vamos a definir las funciones que nos ayudaran a crear, encontrar y agregar un nuevo paciente

# En este caso comenzamos definiendo la funcion crear nuevo paciente
# Dejamos estipulados los argumentos; esto para que python tenga claridad con que informacion ejecutara las instrucciones que se daran en esta funcion.
def crearNuevoPaciente(_id, _nombre, _edad,_genero,_diagnostico, _historial):  
    nuevoPaciente = {"id": _id ,"nombre" : _nombre, "edad" : _edad, "genero" : _genero, "diagnostico" : _diagnostico, "historial" : _historial} # La informacion del nuevo paciente se guardara en un diccionario, queda claro porque lo encerramos en llaves.
    return nuevoPaciente # Esta al ser informacion primordial debe ser vista por el usuario, por ende dejamos la orden con el comando return para que se pueda ver.

# Con la funcion encontrar paciente dejamos estipuladas ciertas reglas:
def encontrarPacienteID(_id): #  La funcion se deja argumentada tambien con el id, que es la informacion mas relevante para que nuestras instrucciones tengan sentido.
    for paciente in listaDePacientes: # Con el comando for le pedimos a un iterador que busque el id de los pacientes en una lista.
        if paciente["id"] == _id: # Con if sabremos si se encuentra, y si es asi;
            return True , paciente # Nos retorna al paciente encontrado y dicha condicion es verdadera
            
    return False , None # Si no es asi, entonces es falsa la condicion y con return nos muestra un none

# Con la funcion agregar un paciente nuevo, lo que hacemos es guardar en forma de diccionario informacion de un nuevo paciente.
def addNuevoPaciente(_id, _nombre, _edad,_genero,_diagnostico, _historial):
    encontrado = encontrarPacienteID(_id) # Aqui llamamos a la funcion encontrar paciente para validar que este ya no este en nuesta base de datos.
    encontrado = encontrado[0] 
    if not encontrado: # Con if dejamos un condicion y es; 
        nuevoPaciente = crearNuevoPaciente(_id, _nombre, _edad,_genero,_diagnostico, _historial) # Si no se encuentra el id, entonces creamos al nuevo paciente 
        listaDePacientes.append(nuevoPaciente) # Y lo agg a nuestra nuestra base de datos, usando append
        actializarListaDePacientes() # Aqui llamamos a la funcion actualziar lista para que este ya aparezca en json 
    else: print("El paciente actualmente se encuentra registrado") #Con print mostramos el mensaje: 



#---------------------------------------------------------------------------------------------------------------------------------------------------
#            Funciones para filtrar lista de pacientes        
def filtrarPorID(_id): # Creamos la funcion filtrar y argumentamos con el id 
    encontrado = encontrarPacienteID(_id) # se llama la funciona ya conocida para validar que no exista
    if encontrado[0]: # si se encuentra el id, se despliega toda la infomacion del paciente 
       
       #[0] y [1] son condiciones que vienen de la funcion encontrar al paciente   el cual nos devulve una tupla 
        print(f"Nombre: {encontrado[1]['nombre']}")
        print(f"Identificación: {encontrado[1]['id']}")
        print(f"Edad: {encontrado[1]['edad']}")
        print(f"Genero: {encontrado[1]['genero']}")
        print(f"Diagnostico: {encontrado[1]['diagnostico']}")
        print(f"Historial: {encontrado[1]['historial']}")

        
        
# Dado lo contrario simplemente con print mostramos el mensaje correspondiente 
    else: print("No encontrado! Por favor ingresa ID correcto")


# Aqui se filtrara por nombres y a diferencia de filtrar por id aqui pueden haber varias coincidencias por ende...
def filtrarPorNombre(_nombre):
    listaFiltrada = [] # Se crea una lista temporal que nos mostrara los resultados encontardos por...
    for paciente in listaDePacientes: # La funcion for que le dice al iterador que busque en la lista de pacientes.
        if paciente["nombre"] == _nombre: # Aqui es "SI EL NOMBRE QUE ENCUENTRAS COINCIDE CON EL QUE ESTOY BUSCANDO VA A LA LISTA"
            listaFiltrada.append(paciente) # Y como ya dije iran a la lista temporal 
    if listaFiltrada: # Aqui basicamente es si lista filtrada existe entonces...
        for paciente in listaFiltrada: # Con for viajamos por la lista ya creada con los nombres coincidentes y ... 
            print(paciente) # Las mostramos con print
        
    else: print(f"No hay pacientes con el nombre: {_nombre}") # Clarsmente si no hay coincidencia pues se muestra el mensaje
            
# Igual en la funcion de filtrado anterior, el proceso es el mismo, creamos nuestra funcion de filtrar por diagnostico 
def filtrarPorDiagnostico(_diagnostico):
    listaFiltrada = [] # Se crea la lista vacia que gurdara la informacion temporal
    for paciente in listaDePacientes:
        if paciente["diagnostico"] == _diagnostico:
            listaFiltrada.append(paciente)
    if listaFiltrada:
        for paciente in listaFiltrada:
            print(paciente)
    else: print(f"No hay pacientes con el diagnóstico de: {_diagnostico}")

#---------------------------------------------------------------------------------------------------------------------------------------------------
#        Funciones eliminar paciente

# creamos la funcion eliminar paciente y argumentamos con id que es la informacion mas directa del paciente 
def eliminarPaciente(_id):
    pacienteEliminar = encontrarPacienteID(_id) #claramente para eliminar algo es porque esta registrado por ende llamamos la funcion para que realice la busqueda 
    if pacienteEliminar[0] == True: # si el paciente se encuentra entonces...
        print(f"paciente: {pacienteEliminar[1]['nombre']} eliminado correctamente ") # se elimina y se muestra el respectivo mensaje.
        listaDePacientes.remove(pacienteEliminar[1]) #con  remove se elimina de la lista
        
        actializarListaDePacientes() # se llama esta funcion para que se actualice la informacion 

def eliminarPacienteMenu(): #Con la funcion eliminardel menu se dan las instrucciones y pasos para que el usario sepa usarlo
    
    _id = ""
    while True: # Aqui se genera un bucle pidiendo el numero a eliminar 
        try:
            _id = int(input("ID del paciente a eliminar: "))
            break
        except ValueError: # se deja claro que el valor ingresado debe ser correcto
            print("Ingrese una ID correcta")
    eliminarPaciente(_id) # y se llama la funcion que realmente elimina la informacion con la logica ya programada


#--------------------------------------------------------------------------------------------------------------------------------------------------
#       Funciones modificar paciente

# se crea una funcion que modificara un paciente, no se deja ningun argumento debdio a que no es necesario, la funcion pedira toda la informacion 
def modificar_paciente():
    print("\n--- Modificar datos de un paciente ---")
    if not listaDePacientes: # si no existe informacion en lista de paciente...
        print("No hay pacientes registrados.") # se mostrara este mensaje y...
        input("Presione Enter para volver al menú...") # se le pedira al usuario que se salga.
        return

    try: # se intentara convertir lo que se introduzca en un numero 
        id_paciente = int(input("Ingrese el ID del paciente a modificar: ").strip())
    except ValueError: # si no le es posible entonces se le indicara que...
        print("El ID debe ser un número entero.")
        input("Presione Enter para volver al menú...") # y nuevamente se le pedira salir al menu 
        return
# si el iterador ze va a la lista de pacientes y...
    for p in listaDePacientes:
        if p["id"] == id_paciente: #encuentrar el id del paciente y mostrar toda informacion del paciente 
            print(f"\nPaciente encontrado: {p['nombre']}")
            print(f"Edad actual: {p['edad']}")
            print(f"Diagnóstico actual: {p['diagnostico']}")
            print(f"Historial actual: {', '.join(p['historial']) if p['historial'] else 'Sin historial'}")
# una vez identificado el paciente podemos preguntarle al usuario que quiere hacer, que modificacion 
            print("\n¿Qué desea modificar?")
            print("1. Edad")
            print("2. Diagnóstico")
            print("3. Agregar entrada al historial")
            opcion = input("Seleccione una opción: ").strip()
            

            if opcion == "1":
    # si este escoje 1 etonces con un bucle debera ingresar la nueva edad del paciente 
                while True:
                    try: # se intentara convertir los valores escritos a numero
                        nueva_edad = int(input("Ingrese la nueva edad: "))
                        nueva_edad = abs(nueva_edad)
                        break
                    except ValueError: print(f"La edad debe ser un número entero")
    # es necesario que el usuario confirme esta accion 
                confirmar = input(f"¿Desea cambiar la edad de {p['edad']} a {nueva_edad}? (s/n): ").strip().lower()
                if confirmar == "s": # al haber luz verde se genera el cambio de edad 
                    p["edad"] = nueva_edad
                    print("Edad actualizada correctamente.")
                    actializarListaDePacientes() # se llama a lafuncion de actualizacion para que tambien se muestre en json 
                else:
                    print("Cambio cancelado.")
# los pasos en este caso son iguales al anterior 
            elif opcion == "2":
                nuevo_diagnostico = input("Ingrese el nuevo diagnóstico: ")
                confirmar = input(f"¿Desea cambiar el diagnóstico de '{p['diagnostico']}' a '{nuevo_diagnostico}'? (s/n): ").strip().lower()
                if confirmar == "s":
                    p["diagnostico"] = nuevo_diagnostico
                    print("Diagnóstico actualizado correctamente.")
                    actializarListaDePacientes()
                else:
                    print("Cambio cancelado.")
# por otra parte en el caso del historial lo que se pregunta es si agg algo diferengte al historial 
            elif opcion == "3":
                nueva_entrada = input("Ingrese la nueva entrada para el historial: ")
                confirmar = input(f"¿Desea agregar '{nueva_entrada}' al historial? (s/n): ").strip().lower()
                if confirmar == "s": # esto debido a que el historial del paciente debe ser inborrable e inmutable, se puede actualizar pero no borrar ni cambiar nada. 
                    p["historial"].append(nueva_entrada) # por ende en vez de cambiar lo que se hace es actualizar la lista ya conocida con append
                    print("Nueva entrada agregada al historial.")
                    actializarListaDePacientes() # se llama la funcion de actualizacion y se guarda en json 
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
# con la funcion mostrar pacientes el proceso es simple, mostrar toda la informacion del paciente cuando sea requerido
def mostrar_pacientes():
    print("\n--- Lista de pacientes registrados ---")
    if not listaDePacientes: # si no existiera un banco de informacion se mostraria la siguiente advertencia.
        print("No hay pacientes registrados.")
        return
    
    for p in listaDePacientes: # se usa el comando for para pasear por toda la lista de pacientes.
        print(f"\nID: {p['id']}")
        print(f"Nombre: {p['nombre']}")
        print(f"Edad: {p['edad']}")
        print(f"Género: {p['genero']}")
        print(f"Diagnóstico: {p['diagnostico']}")
        print(f"Historial: {', '.join(p['historial']) if p['historial'] else 'Sin historial'}")
#----------------------------------------------------------------------------------------------------------------------------
#         Funcion moduloBusqueda
# se crea una funcion de busqueda de paciente
def menuBusqueda():
    print ("Señor usuario, a continuacion podra observar las opciones para buscar a un paciente.\n")
    
    "==============DISPONIBILIDAD================"
# dicha funcion se filtrara por nombre, id o diagnostico       
    print("1. Nombre completo del paciente.\n   ") 
        
    print("2. ID del paciente.\n ")
        
    print("3. Diagnostico del paciente.\n  ")
        
    while True: # se crea un bucle con while para que las opciones y los resultados de dichas opciones puedan ser vistas cuantas veces quiera el usuario
        
        opcion = (input("Elige una opción: "))
        
    # como se habia mencionado esta busqueda es por filtros 
    # en este caso se escoge la opcion 1 por nombres, se pide que se ingrese el nombre y    
        if opcion == "1":
            nombre_completo= input("\nPor favor ingrese nombre completo del paciente: ")
            print (f"\nBuscando paciente que con el nombre {nombre_completo}....Espere un momento por favor.\n")
            filtrarPorNombre(nombre_completo) # se llama la funcion filtrar por nombres para que realice el trabajo y nos muestre las coincidencias
            break
            
    # si escohe la opcion 2 filtar por id, el proceso es mas rapido y preciso porque el id es informacion unica
        elif opcion == "2":
            try:
                ID = int(input("Ingrese el ID del paciente: ").strip())
            except ValueError:
                print("El ID debe ser un número entero.")
                return
        
            print (f"\nBuscando paciente que con el ID {ID}...Espere un momento por favor.\n")
            filtrarPorID(ID)
            break
            
            
                
        # al igual que la primera opcion, se filtra por diagnostico, nos mostrara todas las coincidencias
        elif opcion == "3":
            Diagnostico= input("\nPor favor ingrese su diagnostico para realizar un filtro entre todos los registrados: ")
            print (f"\nBuscando pacientes que con diagnostico coincidente con {Diagnostico}...Espere un momento por favor.\n")
            filtrarPorDiagnostico(Diagnostico) # y se llamara a la funcion para que nos muestre los resultados 
            break


        # si el usuario ingresa un valor de busqueda no mencionado en el menu simplemente se le mostrara el siguiente error 
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

# el primer reporte que se desea generar es para pacientes mayores de 60 años 
    if opcion_reporte == "1":
        print("\n--- Reporte: Pacientes mayores de 60 años ---") 
        pacientes_mayores = [] # aqui al igual que en otras funnciones se crea una lista vacia temporal
        for p in listaDePacientes: # con el iterador se busca en toda la lista de pacientes que hayan pacientes mayores de 60
            try:
                # si los hay se agg en la lista 
                if int(p["edad"]) > 60:
                    pacientes_mayores.append(p)
            except ValueError:
                print(f"Advertencia: El paciente ID {p['id']} tiene una edad no numérica ('{p['edad']}') y no será incluido.")

        if not pacientes_mayores: # Si no exiten pacientes con este rango de edad simplemnte se muestra el mensaje 
            print("No se encontraron pacientes mayores de 60 años.")
        else: # si en caso tal se llegase a encontrar los pacientes mayores entonces se deja el mensaje 
            print(f"Se encontraron {len(pacientes_mayores)} pacientes mayores de 60 años:")
            for p in pacientes_mayores: # se iteran y se muestra toda la informacion en forma de diccionario. 
                print(f"  - ID: {p['id']}, Nombre: {p['nombre']}, Edad: {p['edad']}, Diagnóstico: {p['diagnostico']}")
# por otro lado si el usuario escogio la opcion 2, reporte por diagnosticos mas recientes entonces 
    elif opcion_reporte == "2":
        print("\n--- Reporte: Diagnósticos más frecuentes ---")
        contador_diagnosticos = {} # se crea un diccionario vacio 
        for p in listaDePacientes: # se itera la informacion de los diagnosticos con for dentro de la lista de los pacientes 
            diagnostico = p["diagnostico"].strip().title() # y los diagnosticos que se encuentren los organizamos sin espacios y que la letra de cada palabra comience por mayuscula
            if diagnostico: # si los dianosticos existen entonces...
                contador_diagnosticos[diagnostico] = contador_diagnosticos.get(diagnostico, 0) + 1 #con el contador de diagnosticos los vamos contando y get nos permite obtener el valor de una clave porque esta informacion esta en un diccionario 
        
        if not contador_diagnosticos: # si no hay no hay. 
            print("No hay diagnósticos registrados para mostrar.")
        else: # aqui vamos a organizar toda la informacion de los diagnosticos 
            # basicamente aqui lo que hacemos primero es que se tome el valor numerico de cada item y con esos valores se organice la informacion pero de mayor a menos usando reserve tru 
            diagnosticos_ordenados = sorted(contador_diagnosticos.items(), key=lambda item: item[1], reverse=True)
            print("Frecuencia de diagnósticos:") # aqui finalmente se imprime la frecuencia de los diagnosticos 
            for diagnostico, cantidad in diagnosticos_ordenados:
                print(f"  - {diagnostico}: {cantidad} paciente(s)")
                
# aqui simplkenete contamos cuantos pacientes tenemos, usando solamente len y pidiendo que se imprima 
    elif opcion_reporte == "3":
        print("\n--- Reporte: Cantidad total de pacientes ---")
        total_pacientes = len(listaDePacientes)
        print(f"Actualmente hay un total de {total_pacientes} pacientes registrados en el sistema.")
# recuerden que ya tenemos una funcion que me imprime todos los usarios registrados
    elif opcion_reporte == "4":
        print("\n--- Reporte: Informacion de Pacientes ---")
        mostrar_pacientes() # no es mas que llamnar a dicha funcion 
# y si el usario se equivoca ingresando un valor se le dira que se esta equivocando que no sea tonto
    else:
        print("Opción de reporte no válida.")
    
    input("\nPresione Enter para volver al menú...")

#--------------------------------------------------------------------------------------------------------------

#VALIDACIONES 

def agregar_paciente():
    print("\n--- Registrar nuevo paciente ---")
    try:
        id_paciente = int(input("Ingrese documento de identidad del paciente: ").strip())
        id_paciente = abs(id_paciente)
    except ValueError:
        print("El documento de identidad debe ser un número entero.")
        return
    
    for paciente in listaDePacientes:
        if paciente["id"] == id_paciente:
            print("Este documento ya existe. No se puede registrar un duplicado.")
            return
    

    while True:
        nombre = input("Ingrese nombre del paciente: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("El nombre solo debe contener letras, sin números.")
    while True:
        try:
            edad = int(input("Ingrese edad del paciente: "))
            edad = abs(edad)
            break
        except ValueError:print("La edad debe ser un número entero")
    genero = ""
    while not(genero == "f" or genero == "m"):
        genero = input("Ingrese género del paciente\n (f) para femenino | (m) para masculino: ")
    genero = "femenino" if genero == "f" else  "masculino"
    diagnostico = input("Ingrese diagnóstico: ")
    historial = []

    while True:
        entrada = input("Agregar entrada al historial (o presione Enter para terminar): ")
        if entrada == "":
            break
        historial.append(entrada)
    
    addNuevoPaciente(id_paciente,nombre,edad,genero,diagnostico,historial)
    print("Paciente registrado correctamente.\n")


# aqui tenemos el menu principal, desde aqui podemos llamar todas las funciones ya definidas al mismo tiempo 

while True:
    print("\n===== MENÚ PRINCIPAL - CLÍNICA =====")
    print("1. Registrar nuevo paciente")
    print("2. Buscar paciente")
    print("3. Modificar paciente")
    print("4. Eliminar Paciente")
    print("5. Generar Reportes")
    print("6. Salir")

    opcion = input("Seleccione una opción: ").strip()
# tan facio como escoger una opcion, para el usuario claro, para el programador hay toda una maquinaria de condiciones y reglas detras de una simple interfaz 
# si escoge opcion 1 se agregara el paciente
    if opcion == "1":
        agregar_paciente()
        
# si escoge la opcion se busca el paciente
    elif opcion == "2":
        print("Buscar paciente")
        menuBusqueda()
        
# si escoge la 3 se modifica informacion del paciente    
    elif opcion == "3":
        print("Modificando pacientes")
        modificar_paciente()
# aqui la 4 elimina completamente al paciente       
    elif opcion == "4":
        print("Eliminar pacientes")
        
        eliminarPacienteMenu()
# la opcion 5 genera un reporte    
    elif opcion == "5":
        print("Generar reportes")
        generar_reportes()
# y finalmente la opcion 6 solo agradece al usario de preferir a SPUTNIK para solucionarles la vida.
    elif opcion == "6":
        print("Gracias por visitarnos");break

    else:
        print("Opción inválida")
#--------------------------------------------------------------------------------------------------------       

        
#-----------------------------------------------------------------------------------------------------------------------------------     
