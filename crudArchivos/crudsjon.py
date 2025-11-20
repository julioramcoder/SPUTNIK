import json

def crearJsono(nombre, dato):
    with open(nombre, "w") as file:
        json.dump(dato, file, indent=4)
crearJsono("jsono.json", [{"nombre" : "hola", "edad" : 4 }])