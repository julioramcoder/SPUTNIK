import json
import os

DATA_FILE = "contactos.json"

def cargar_contactos():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return []

def guardar_contactos(contactos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(contactos, f, ensure_ascii=False, indent=2)

def mostrar_contactos(contactos):
    if not contactos:
        print("No hay contactos registrados.")
        return
    print("\n--- LISTA DE CONTACTOS ---")
    for i, c in enumerate(contactos, start=1):
        print(f"{i}. {c['nombre']} - {c['telefono']} - {c['email']}")
    print()

def agregar_contacto(contactos):
    nombre = input("Nombre: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
    guardar_contactos(contactos)
    print("Contacto agregado correctamente.")

def buscar_contacto(contactos):
    nombre = input("Nombre a buscar: ").strip().lower()
    resultados = [c for c in contactos if nombre in c["nombre"].lower()]
    if resultados:
        print("\n--- RESULTADOS ---")
        for c in resultados:
            print(f"{c['nombre']} - {c['telefono']} - {c['email']}")
    else:
        print("No se encontraron coincidencias.")

def actualizar_contacto(contactos):
    mostrar_contactos(contactos)
    if not contactos:
        return
    try:
        index = int(input("Número de contacto a actualizar: ")) - 1
        if index < 0 or index >= len(contactos):
            print("Número inválido.")
            return
        contacto = contactos[index]
        print("Deja en blanco si no deseas cambiar un campo.")
        nombre = input(f"Nuevo nombre ({contacto['nombre']}): ").strip()
        telefono = input(f"Nuevo teléfono ({contacto['telefono']}): ").strip()
        email = input(f"Nuevo email ({contacto['email']}): ").strip()
        if nombre:
            contacto["nombre"] = nombre
        if telefono:
            contacto["telefono"] = telefono
        if email:
            contacto["email"] = email
        guardar_contactos(contactos)
        print("Contacto actualizado correctamente.")
    except ValueError:
        print("Entrada inválida.")

def eliminar_contacto(contactos):
    mostrar_contactos(contactos)
    if not contactos:
        return
    try:
        index = int(input("Número de contacto a eliminar: ")) - 1
        if index < 0 or index >= len(contactos):
            print("Número inválido.")
            return
        eliminado = contactos.pop(index)
        guardar_contactos(contactos)
        print(f"Contacto '{eliminado['nombre']}' eliminado.")
    except ValueError:
        print("Entrada inválida.")

def menu():
    contactos = cargar_contactos()
    while True:
        print("\n--- AGENDA DE CONTACTOS ---")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Actualizar contacto")
        print("5. Eliminar contacto")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        match opcion:
            case "1":
                agregar_contacto(contactos)
            case "2":
                mostrar_contactos(contactos)
            case "3":
                buscar_contacto(contactos)
            case "4":
                actualizar_contacto(contactos)
            case "5":
                eliminar_contacto(contactos)
            case "0":
                print("Saliendo de la agenda.")
                break
            case _:
                print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
