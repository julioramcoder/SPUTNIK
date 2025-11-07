#Sistema de calificaciones.

class nota:                                           #clase llamada nota (debí cambiar el nombre por sistemaDeNotas o algo similar)
    def __init__(self,estudiante,nota1,nota2):        #el constructor recibe nombre, y 2 notas
        self.estudiante = estudiante                  #calcula el promedio de las dos notas y lo guarda en la propiedad prom
        self.nota1 = nota1
        self.nota2 = nota2
        self.prom = (nota1 + nota2)/2

lista = []                                           #en esta lista voy a guardar las instancias/objetos de la clase nota
while True:                                          #bucle while para hacer el menu
    option = int(input("1: Para agregar nueva nota \n2: para salir\n"))

    if option == 1:                                          #toma los datos
        newEstudiante = input("Nombre del estudiante: ")
        newNota1 = float(input("Nota 1: "))
        newNota2 = float(input("Nota 2: "))
        nuevoNota = nota(newEstudiante,newNota1,newNota2)   #con los datos construye un objeto de tipo nota
        lista.append(nuevoNota)                             #una vez construido, lo agrega a lista
    elif option == 2:                                       #esta opción sale del bucle
        break
    else:print("opcion incorrecta")

for el in lista: #al finalizar, se muestra la info del estudiante
    print(f"Estudiante {el.estudiante} tiene las siguientes notas: {el.nota1} | {el.nota2}| promedio: {el.prom}")

