#vamos a crear un prgrama usando funciones para validar si un contraeña es segura  no
#tiene mas de 8 caracteres
#tiene almenos una letra mnayuscula
#tiene almenos un numero 

#cosas que debemos tener en cuenta
#longitu de la cadena: usamos len ()
#validar si cuenta con una letra mayuscula isupper()
#validar si existe un numero un numero isumeric ()

#debemos definir la funcion primeramente 

def comprobar_contraseña (contraseña):
#ya que tenemos una funcion definida debemos realizar las instrucciones de dicha funcion 
#1 realizar condicionales para los 3 requisitos
    largo = False
    mayus = False
    numero = False
#usaremos falso y verdadero para cambiar de estados si los resultados de mis instrucciones no cumple con lo dicho
    
    if len(contraseña)>8:#les, porque recuerda que debemos leer las letras de la cadena, no los espacios 
            largo=True
    for i in range (len(contraseña)): 
            if contraseña[i].isupper(): #el issuper es para mayusculas
                 mayus=True
            if contraseña[i].isnumeric():#el isnumeric es para numeros
                numero = True
    if largo and mayus and numero: #aqui si las 3 cumplen con un true entonces retornamos true
            return True
    else:
            return False
#UNA VEZ NUESTRA FUNCION YA SE HA DEFINIDO O NUESTRAS INSTRUCCIONES SE HAN DEFINIDO, PODEMOS COMENZAR A PEDIRLE QUE HAGA SU TRABAJO INDUSIENDO VALORES

while True:
    contraseña = input("ingrese una contraseña") #pedimos contraeña y validamos
    verificacion= comprobar_contraseña(contraseña)
#TAMBIEN MAS CONDICIONALES SI ES NECESARIO
    if verificacion: 
        print("contraeña segura")
    else:
     print("no es segura")