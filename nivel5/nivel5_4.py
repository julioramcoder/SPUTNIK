#Gestión de estudiantes (mini base de datos)

import json  #libreria json, para poder abrir y modificar arhivos json (lla mini base de datos)

# Abrir y leer el archivo JSON
with open("nivel5/estudiantes.json", "r") as archivo: 
    estudiantes = json.load(archivo)


for estudiante in estudiantes:
    print(estudiante["nombre"])