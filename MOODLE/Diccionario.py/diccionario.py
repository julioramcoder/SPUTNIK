#diccionario

paciente1 = {
"nombre" : "Juan carlos p",
"id" : 12345,
"genero" : "Masculino",
"edad" : 24,
"diagnostico" : "covid",
"historial" : ["reservado"]
}

paciente2 = {
"nombre" : "Dayana francisca",
"id" : 123456,
"genero" : "femenino",
"edad" : 25,
"diagnostico" : "fiebre",
"historial" : ["reservado"]
}

paciente3 = {
"nombre" : "esteban",
"id" : 1234567,
"genero" : "Masculino",
"edad" : 67,
"diagnostico" : "urselas",
"historial" : ["reservado"]
}

paciente4={
"nombre" : "jhonatan fernandez",
"id" : 123456789,
"genero" : "Masculino",
"edad" : 54,
"diagnostico" : "fiebre",
"historial" : ["reservado"]
}

paciente5 = {
"nombre" : "natalia dallas",
"id" : 1234567890,
"genero" : "femenino",
"edad" : 28,
"diagnostico" : "dolor de amores",
"historial" : ["reservado"]
}

listaDePacientes = [paciente1,paciente2,paciente3,paciente4,paciente5]

def agregarautomatico():

    for item in listaDePacientes:
        nombre = item["nombre"]
        id = item["id"]
        genero = item["genero"]
        edad = item["edad"]
        diagnostico = item["diagnostico"]
        historial = item["historial"]
        addNuevoPaciente(id,nombre,genero,edad,diagnostico,historial)