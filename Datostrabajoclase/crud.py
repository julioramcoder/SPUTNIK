import csv
import os

class CRUD:

    def crear_archivo(self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "nombre", "edad"])

    def obtener_nuevo_id(self, archivo):
        with open(archivo, "r") as f:
            filas = list(csv.reader(f))

        if len(filas) == 1:
            return 1

        ultimo_id = int(filas[-1][0])
        return ultimo_id + 1

    def crear(self, archivo, nombre, edad):
        id_nuevo = self.obtener_nuevo_id(archivo)
        with open(archivo, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id_nuevo, nombre, edad])
        return id_nuevo

    def listar(self, archivo):
        with open(archivo, "r") as f:
            reader = csv.reader(f)
            next(reader)
            return list(reader)
        
    def editar(self, archivo, id_persona, nuevo_nombre, nueva_edad):
        filas_actualizadas = []
        encontrado = False  
        with open(archivo, "r") as f:
            reader = csv.reader(f)
            for fila in reader:
                if fila[0] == str(id_persona):
                    filas_actualizadas.append([id_persona, nuevo_nombre, nueva_edad])
                    encontrado = True
                else:
                    filas_actualizadas.append(fila)
        if not encontrado:
            return False    
    #Guardaer los cambios en el archivo
        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(filas_actualizadas)
        return True 
    #eliminar registro
    def eliminar(self, archivo, id_persona):
        filas_actualizadas = []
        encontrado = False  
        with open(archivo, "r") as f:
            reader = csv.reader(f)
            for fila in reader:
                if fila[0] == str(id_persona):
                    encontrado = True
                else:
                    filas_actualizadas.append(fila)
        if not encontrado:
            return False        
        with open(archivo, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(filas_actualizadas)    
        return True 
        
