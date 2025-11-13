import json
import os

DATA_FILE = "estudiantes.json"

def cargar_datos():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def guardar_datos(estudiantes):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, ensure_ascii=False, indent=2)

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.")
        return
    print("\n--- LISTA DE ESTUDIANTES ---")
    for id_est, datos in estudiantes.items():
        print(f"ID: {id_est}")
        print(f"  Nombre: {datos['nombre']}")
        print(f"  Edad: {datos['edad']}")
        print(f"  Grado: {datos['grado']}")
        print(f"  Promedio: {datos['promedio']}")
        print("-" * 30)

def agregar_estudiante(estudiantes):
    id_est = input("ID del estudiante: ").strip()
    if id_est in estudiantes:
        print("Ya existe un estudiante con ese ID.")
        return
    nombre = input("Nombre: ").strip()
    edad = input("Edad: ").strip()
    grado = input("Grado: ").strip()
    promedio = input("Promedio: ").strip()
    estudiantes[id_est] = {
        "nombre": nombre,
        "edad": edad,
        "grado": grado,
        "promedio": promedio
    }
    guardar_datos(estudiantes)
    print("Estudiante agregado correctamente.")

def buscar_estudiante(estudiantes):
    id_est = input("Ingrese el ID del estudiante: ").strip()
    if id_est not in estudiantes:
        print("No se encontró el estudiante.")
        return
    datos = estudiantes[id_est]
    print(f"Nombre: {datos['nombre']}")
    print(f"Edad: {datos['edad']}")
    print(f"Grado: {datos['grado']}")
    print(f"Promedio: {datos['promedio']}")

def actualizar_estudiante(estudiantes):
    id_est = input("ID del estudiante a actualizar: ").strip()
    if id_est not in estudiantes:
        print("No se encontró el estudiante.")
        return
    print("Deja en blanco si no deseas cambiar el campo.")
    nombre = input(f"Nuevo nombre ({estudiantes[id_est]['nombre']}): ").strip()
    edad = input(f"Nueva edad ({estudiantes[id_est]['edad']}): ").strip()
    grado = input(f"Nuevo grado ({estudiantes[id_est]['grado']}): ").strip()
    promedio = input(f"Nuevo promedio ({estudiantes[id_est]['promedio']}): ").strip()

    if nombre:
        estudiantes[id_est]["nombre"] = nombre
    if edad:
        estudiantes[id_est]["edad"] = edad
    if grado:
        estudiantes[id_est]["grado"] = grado
    if promedio:
        estudiantes[id_est]["promedio"] = promedio

    guardar_datos(estudiantes)
    print("Datos del estudiante actualizados.")

def eliminar_estudiante(estudiantes):
    id_est = input("ID del estudiante a eliminar: ").strip()
    if id_est in estudiantes:
        del estudiantes[id_est]
        guardar_datos(estudiantes)
        print("Estudiante eliminado.")
    else:
        print("No se encontró el estudiante.")

def menu():
    estudiantes = cargar_datos()
    while True:
        print("\n--- GESTIÓN DE ESTUDIANTES ---")
        print("1. Agregar estudiante")
        print("2. Mostrar todos")
        print("3. Buscar estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        match opcion:
            case "1":
                agregar_estudiante(estudiantes)
            case "2":
                mostrar_estudiantes(estudiantes)
            case "3":
                buscar_estudiante(estudiantes)
            case "4":
                actualizar_estudiante(estudiantes)
            case "5":
                eliminar_estudiante(estudiantes)
            case "0":
                print("Saliendo del sistema.")
                break
            case _:
                print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
