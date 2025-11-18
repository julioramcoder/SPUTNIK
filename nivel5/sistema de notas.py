import csv

SCALE = {
    "A": 90,
    "B": 80,
    "C": 70,
    "D": 60,
    "F": 0
}

students = {}

def validar_numero(prompt, min_val=0.0, max_val=100.0):
    while True:
        s = input(prompt).strip()
        try:
            val = float(s.replace(",", "."))
            if val < min_val or val > max_val:
                print(f"Ingresa un número entre {min_val} y {max_val}.")
                continue
            return val
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

def obtener_literal(porcentaje):
    for letra, min_pct in sorted(SCALE.items(), key=lambda x: -x[1]):
        if porcentaje >= min_pct:
            return letra
    return "F"

def agregar_alumno():
    nombre = input("Nombre del alumno: ").strip()
    if not nombre:
        print("Nombre vacío. Cancelado.")
        return
    n_notas = int(validar_numero("¿Cuántas notas vas a ingresar? (ej: 3): ", 1, 100))
    notas = []
    for i in range(1, n_notas + 1):
        nota = validar_numero(f"  Nota {i} (0-100): ", 0, 100)
        notas.append(nota)
    students[nombre] = notas
    print(f"Alumno '{nombre}' agregado con {len(notas)} nota(s).")

def mostrar_alumnos():
    if not students:
        print("No hay alumnos registrados.")
        return
    print("\nAlumnos registrados:")
    for nombre, notas in students.items():
        promedio = sum(notas) / len(notas)
        literal = obtener_literal(promedio)
        estado = "APROBADO" if promedio >= SCALE.get("D", 60) else "REPROBADO"
        notas_str = ", ".join(f"{n:.1f}" for n in notas)
        print(f"- {nombre}: Notas [{notas_str}] → Promedio: {promedio:.2f} → {literal} ({estado})")
    print()

def ver_reporte_detallado():
    if not students:
        print("No hay alumnos registrados.")
        return
    print("\nREPORTE DETALLADO")
    print("-" * 40)
    for nombre, notas in students.items():
        promedio = sum(notas) / len(notas)
        literal = obtener_literal(promedio)
        mayor = max(notas)
        menor = min(notas)
        print(f"Alumno: {nombre}")
        print(f"  Notas: {', '.join(f'{n:.1f}' for n in notas)}")
        print(f"  Promedio: {promedio:.2f}")
        print(f"  Mayor/Menor: {mayor:.1f} / {menor:.1f}")
        print(f"  Literal: {literal}")
        print("-" * 40)
    print()

def exportar_csv(ruta="reporte_calificaciones.csv"):
    if not students:
        print("No hay alumnos para exportar.")
        return
    with open(ruta, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Notas (separadas por |)", "Promedio", "Literal", "Estado"])
        for nombre, notas in students.items():
            promedio = sum(notas) / len(notas)
            literal = obtener_literal(promedio)
            estado = "APROBADO" if promedio >= SCALE.get("D", 60) else "REPROBADO"
            notas_join = "|".join(f"{n:.1f}" for n in notas)
            writer.writerow([nombre, notas_join, f"{promedio:.2f}", literal, estado])
    print(f"Exportado a '{ruta}' exitosamente.")

def cambiar_escala():
    print("Escala actual (letra: mínimo %):")
    for letra, pct in sorted(SCALE.items(), key=lambda x: -x[1]):
        print(f"  {letra}: {pct}")
    print("Introduce nuevas mínimas (deja en blanco para mantener):")
    for letra in list(SCALE.keys()):
        entrada = input(f"  Mínimo para {letra} (actual {SCALE[letra]}): ").strip()
        if entrada == "":
            continue
        try:
            val = int(entrada)
            if 0 <= val <= 100:
                SCALE[letra] = val
            else:
                print("Valor fuera de rango, ignorado.")
        except ValueError:
            print("Entrada inválida, ignorado.")
    print("Escala actualizada:", SCALE)

def menu():
    opciones = {
        "1": ("Agregar/Actualizar alumno", agregar_alumno),
        "2": ("Mostrar alumnos (resumen)", mostrar_alumnos),
        "3": ("Ver reporte detallado", ver_reporte_detallado),
        "4": ("Exportar a CSV", exportar_csv),
        "5": ("Cambiar escala de letras (A-F)", cambiar_escala),
        "6": ("Vaciar lista de alumnos", lambda: (students.clear(), print("Lista vaciada."))),
        "0": ("Salir", None)
    }
    while True:
        print("\n--- SISTEMA DE CALIFICACIONES ---")
        for k, (desc, _) in opciones.items():
            print(f"{k}. {desc}")
        elec = input("Elige una opción: ").strip()
        if elec == "0":
            print("Saliendo. ¡Hasta luego!")
            break
        if elec in opciones:
            func = opciones[elec][1]
            if func:
                func()
        else:
            print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
