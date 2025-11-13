#crewar una tabla  que multiplique cualquier numero entero dado por el usuario,
#la tabla debe calcular desde el 0 hasta el 12

#cremos nuestra fucnion 
#cabe mencior que debemos definir nuestro argumento, la informacion  que por defecto deb
#la informacion que por defecto se necesita para que el codigo fucnione

def tablademultiplicar (n1 , n2): #¿que se necesita paara multiplicar? pues 2 numeros solamente asi funciona la multiplicacion 
    resultado = str(n1) +"*"+ str(n2)+ "="+ str (n1*n2) # todo queremos que nos muestre como texto por ende ponemos el rresultado como texto y no solamente como numero 
    return resultado 
numero = int(input("danos el numero a multiplicar"))

for i in range (0,21): #usamos de nuevo un for porque si o si necesitamos irmprimir numeros en forma de columna
    print(tablademultiplicar(numero,i)) 

