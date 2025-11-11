#Sistema de calificaciones.

class Estudiante:                                          #Clase EStudiante, el construcor resive un str con el nombre del estudiante                  
    def __init__(self,estudiante):       
        self.nombre = estudiante                  
        self.notas = []                                    #notas es una lista, almacena las notas del estudiante

    def addNota(self,nota):                                #metodo addNota recibe un float, agrega la entra a la lista de notas
        self.notas.append(nota)

    def getInfo(self):                                     #metodo getInfo, muestra el nombre del estudiante, si tiene notas tambien las imprime con su promedio
        print(f"Estudiante: {self.nombre}")
        if len(self.notas) > 0:
           
            print("Notas: " , self.notas)

            print(f"Promedio: {sum(self.notas)/(len(self.notas))}")
        else:
            print("Aun no hay notas en el sistema")
   
class ListaEstudiante:                                   #clase ListaEstudiante, se podría considerar como la estrucura de datos y la clase Estudiante el "nodo"
    def __init__(self):                                  #o dato que almacene, al crear un objeto de esta clase se genera una lista que almacena los estudiantes
        self.lista = []

    def existeEstudiante(self,estudiante):               #Metodo existeEstudiante, recibe una cadena y retorna un booleano, su valor depende de si encuentra o no
        existe = False                                   #al estudiante en la lista. inicia con una bandera falsa, si en algun momento encuentra una coincidencia
        for el in self.lista:                            #la bandera se vuelve verdadera y termina el ciclo
            if el.nombre == estudiante:
                existe = True
                break
        return existe



    def addEstudiante(self,estudiante):                 #metodo addEstudiante recibe una cadena, se apoya del metodo existeEstudiante para saber si ya se agregó
        if not self.existeEstudiante(estudiante):       #el estudiante, si no está, crea un objeto de la clase Estudiante y lo agrega a la lista (pd: debería)
            self.lista.append(Estudiante(estudiante))   #(cambiar el nombre de "lista" por algo mas descriptivo)
        else: print(f"{estudiante} ya se encuentra en la lista")

    def addNotaL(self,estudiante,nota):                 #metodo addnotaL recibe una cadena y un float/int, si encuentra un elemento que coincida con la cadena
        for el in self.lista:                           #usa el método de Estudiante.addNota (hubiera querido usar el método de existe, pero como solo devuelve un booleano, realmente no puedo usar el elemento como tal y me tocó repetir código)
            if el.nombre == estudiante:
                el.addNota(nota);break
            
    def getEstudiante(self,estudiante):                #metodo getEstudiante recibe una cadena, si encuentra al estudiante, usa el método de Estudiante.getInfo()
        for el in self.lista:
            if el.nombre == estudiante:
                el.getInfo()
                break
        print(f"No se encontró el estudiante: {estudiante} ")
            

    
    def getLista(self):                                #metodo getLista, imprime a todos los estudiantes, en el orden en el que fueron agregados a la lista
        
        for i, estudiante in enumerate(self.lista):
            print(f"{i+1}. {estudiante.nombre}")



listaE = ListaEstudiante()


while True:
    print("Gestión de notas, \nElige una opción")

    print("1: Agregar estudiante: ")
    print("2: Información de Estudiante ")
    print("3: Agregar nota a estudiante ")
    print("4: Mostrar estudiantes ")
    print("5: Salir\n ")

    opcion = int(input())

    match opcion:
        case 1:
            nombre = input("Introduce el nombre del estudiante: ")
            listaE.addEstudiante(nombre)
        
        case 2:
            nombre = input("Buscar estudiante: ")
            listaE.getEstudiante(nombre)
        
        case 3:
            nombre = input("Introduce el nombre del estudiante: ")
            nota = float(input("Nota: "))

            listaE.addNotaL(nombre,nota)
        
        case 4:
            listaE.getLista()
        
        case 5:
            break

        case _: print("Opción inválida")



