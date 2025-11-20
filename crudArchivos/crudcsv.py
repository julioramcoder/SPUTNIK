import csv

def crearCsv(nombre, encabezado):
    with open(nombre, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(encabezado)






def addRow(nombre, row):
    with open(nombre, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)
