
import csv

def guardar_csv(inventario, ruta):
    if len(inventario) == 0:
        print("--- El inventario está vacío, no se guardó nada ---")
        return

    try:
        # 'w' significa write (escribir). newline='' evita líneas en blanco extra en Windows.
        with open(ruta, 'w', newline='') as archivo:
            escritor = csv.writer(archivo)
            # Escribimos el encabezado
            escritor.writerow(["nombre", "precio", "cantidad"])
            
            # Escribimos los datos fila por fila
            for producto in inventario:
                escritor.writerow([producto["nombre"], producto["precio"], producto["cantidad"]])
                
        print(f"--- Inventario guardado en {ruta} ---")
        
    except Exception as error:
        print(f"--- Error al guardar: {error} ---")

def cargar_csv(ruta):
    """
    Lee el archivo CSV y devuelve una lista de productos.
    """
    lista_nueva = []
    filas_error = 0
    
    try:
        # 'r' significa read (leer)
        with open(ruta, 'r') as archivo:
            lector = csv.reader(archivo)
            
            # Saltamos el encabezado (la primera línea)
            next(lector) 
            
            for fila in lector:
                # Validamos que la fila tenga 3 columnas
                if len(fila) == 3:
                    try:
                        nombre = fila[0]
                        precio = float(fila[1])
                        cantidad = int(fila[2])
                        
                        # Validación: no negativos
                        if precio >= 0 and cantidad >= 0:
                            nuevo_prod = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
                            lista_nueva.append(nuevo_prod)
                        else:
                            filas_error += 1
                    except ValueError:
                        # Si falla la conversión a número
                        filas_error += 1
                else:
                    filas_error += 1
                    
        if filas_error > 0:
            print(f"--- Se omitieron {filas_error} filas por errores de datos ---")
            
        return lista_nueva

    except FileNotFoundError:
        print("--- El archivo no existe ---")
        return []
    except Exception as error:
        print(f"--- Error leyendo archivo: {error} ---")
        return []