#Sistema de calificaciones
n = int(input("¿Cuántas notas vas a ingresar?: "))
notas = []
for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)
promedio = sum(notas) / n
print("Promedio:", promedio)
if promedio >= 3.0:
    print("Aprobado ✅")
else:
    print("Reprobado ❌")