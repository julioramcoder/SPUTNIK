

def crearArchivo(nombre):
    with open(nombre, "w") as file:
        file.write(f"Primera linea de {nombre}")

        return f"creado el archivo {nombre}"
    
def agregarLinea(nombre, texto):
    with open(nombre, "a") as file:
        file.write(f"\n{texto}")

        return f"agregada linea {texto} al archivo {nombre}"

def leerArchivo(nombre):
    with open(nombre, "r") as file:
        return file.read()
    
