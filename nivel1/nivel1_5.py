#Tipo de dato: usar type() para mostrar el tipo de cada variable.

dato = input("ingresa un dato: ") #se pide el dato al usuario

print(type(dato)) #se muestra qué tipo de dato es... (La verdad no entiendo bien el ejercicio, ya que las entradas siempre son tipo str,
                    # podría usar los métodos que tiene str como isalpha o isnumber, pero ya no estaría usando type())

def tipoDeDato(data): #como input siempre es str, mejor hice una función
    print(type(data))

tipoDeDato(2) #ejemplo  con argumento 2, salida esperada int
tipoDeDato(2.4) #ejemplo  con argumento 2.4, salida esperada float
tipoDeDato("hola") #ejemplo  con argumento "hola", salida esperada str