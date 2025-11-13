# tomamos primero la nota del estudiante para poder almacenar ese dato

nota = float(input("Ingresa tu nota (0 a 5): "))

match nota: # aca procedemos a utilizar el swicht match con 3 casos que funciona con la variable indicada

    case 1 if 4.5 <= 1 <= 5:
        print("Excelente ")
    case 2 if 3 <= 2 < 4.5:
        print("Aprobado ")
    case 3 if 0 <= 3 < 3:
        print("Reprobado ")
    case _:
        print("Nota fuera de rango  (Debe ser entre 0 y 5)")
    