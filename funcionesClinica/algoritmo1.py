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
    
    if not encontrarPacienteID(_id):
        nuevoPaciente = crearNuevoPaciente(_id, _nombre, _edad,_genero,_diagnostico, _historial)
        listaDePacientes.append(nuevoPaciente)
    else: print("El paciente actualmente se encuentra registrado")
    

#---------------------------------------------------------------------------------------------------------------------------------------------------
#            Funciones para filtrar lista de pacientes        

def filtrarPorNombre(_nombre):
    listaFiltrada = []
    for paciente in listaDePacientes:
        if paciente["nombre"] == _nombre:
            listaFiltrada.append[paciente]
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

def modificarPaciente(_paciente,_cualidad):
    


        




