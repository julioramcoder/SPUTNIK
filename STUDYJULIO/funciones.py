#vamos a crear funciones para el iva de un producto 

#primero debemos comenzar definiendo la variable y nombrandola

def calculariva (p): #aqui creamos la funcion llamada calcu... definimos el arguemnto debido a que es la informacion necesaria para que el codigo fuencione
    iva = p*0.19 #generamos el calculo y como ya vimos el argumento hace parte del codigo en este caso la multiplicacionn
    return iva#como aqui estamos generando un codigo base la forma en como dejamos definido que se nos debe mostrar algo es con return en vez de print, 
#si nosotros no definimos esta accion de mostrar dentro de la funcion entonces cuando lo volvamos a usar para otro calculo entonces no nos mostrara nada
preciodecompra = float(input("hey cuanto te costo?: ")) #aqui pedimos otro argumento o informacion necesaria para el culculo
iva = calculariva(preciodecompra) #aqui usamos la fucnion ya definida para que nos de el resultado 
print(iva)  #y aqui ya mostramos el resultado, dentro de esa funcion caculariva ya existe un calculo previo por ende no volveremos a crear un codigo de calculo