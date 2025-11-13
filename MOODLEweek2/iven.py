#we are goona to do a inventory platform

print("=============== GOOD HOME COOKING ==============")

#we need to  beging asking to the user basic information usign the command while
name = input("HEY!, it's a pleasure to meet you, Please type your username: ")

print("Que deseas hacer hoy\n   1- agregar un producto\n   2- revisar productos\n   3- Ver estadisticas\n   4- salir")
actividad = 2
    
inventarios=[] #CREAREMOS UNA LISTA VACIA INMUTABLE FUERA DEL BUCLE PARA QUE SE GUARDE TODOO AQUI
#agregar_producto

def agregar_productos():
    
    while True: 
       print(".\nNUEVO INVENTARIO INICIADO.\n")
       
       nombre = input ("por favor ingrese el nombre del nuevo producto: ")
       precio = float(input("por favor ingresa el valor del producto por unidad: "))
       cantidad = int(input("por favor ingrese la cantidad de productos: "))
       total = precio * cantidad 

       diccionario ={'nombre':nombre, 'precio' :precio, 'cantidad':cantidad, 'total':total}
       inventarios.append(diccionario)
        
       continuar = input(name + "Quieres continuar con el inventario?(si/no): ").lower()
       if continuar == "no":
           print(name + "vamos a salir del inventario en este momento")
           
       




def showInventory (inventario):  
#mostrar el invnetario      
        for i in inventarios: 
         print (i,"\n")
         
        if len(inventarios) == 0:
            print("Aun no has ingresado nada a tu inventario")
              
def estadistica (inventarios):      
#mostrar estadisticas 
    
        for iterador in inventarios:
            print (f'TOTAL:{iterador["nombre"]}={iterador["total"]}.\n')
        Total_de_inventario = sum(iterador["total"] for iterador in inventarios) 
        print(f'total del inventario:${Total_de_inventario}')
        
        if len(inventarios) == 0:
            print("Aun no has ingresado nada a tu inventario")
              
    





while actividad != 4:
    
    actividad = int(input(name+ "Por favor indicame que quieres hacer hoy: "))

    if actividad < 1 or actividad > 4:
        print(name + "Lo siento esa opcion no es valida por favor vuelve a ingresar")
        continue
    
    elif actividad == 1:
        agregar_productos()
                
    elif actividad == 2:
        showInventory(inventarios)
                
    elif actividad == 3:
        estadistica(inventarios)
    print("1- add    2- show    3- stadistics    4- out")
    
