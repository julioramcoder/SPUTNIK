import csv
import os

class CRUD:

    def crearArchivo(self,archivo):
        if not os.path.exists(archivo):
            with open(archivo, "w",newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["id","nombre","edad"])
    
    def obtenerNuevoId(self,archivo):
        with open(archivo, "r") as file:
            filas = list(csv.reader(file))

        if len(filas) == 1:
            return 1
        
        ultimoId = int(filas[-1][0])
        return ultimoId + 1
        
    
    def agregarRegistro(self, archivo, nombre, edad):
        _id = self.obtenerNuevoId(archivo)
        with open(archivo, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([_id,nombre,edad])
            return _id
    
    def mostrarRegistro(self, archivo):
        with open(archivo, "r") as file:
            reader = csv.reader(file)
            next(reader)
            return list(reader)
        
        
    def guardarRegistro(self, archivo, lista):
        with open(archivo, "w" ,newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["id","nombre","edad"])
        with open(archivo,"a",newline="") as file:
            writer = csv.writer(file)
            for row in lista:

                writer.writerow(row)

    def modificarRegistro(self,_id, archivo, nombre=None, edad=None):
        with open(archivo, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            lista = list(reader)
            for registro in lista:
                if registro[0] == _id:
                    if nombre:
                        registro[1] = nombre
                    if edad:
                        registro[2] = edad
        self.guardarRegistro(archivo,lista)
    
  

        


    

