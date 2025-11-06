#Clasificador de notas (Excelente, Aprobado, Reprobado).

nota = float(input("ingresa la nota: ")) #se pide la nota

if  nota >= 8: print("Excelente") #arbitrariamente decidí que, a partir de 8, es excelente
elif nota >= 6 and nota < 8: print("Aprobado") #si está entre 6 y 8 (sin incluir el 8) es aprobado
else: print("Reprobado") #si no alcanza el 6, reprobado