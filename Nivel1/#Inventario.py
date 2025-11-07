#Inventario
#Se solicita al usuario la informacion correspondiente, si se equivoca con el tipo de dato se enviara un mensaje pidiendo validarlo
while True:
  nombre = input("Ingresa el nombre del producto: ")
  if nombre == "":
    print("Debes intentarlo de nuevo e ingresar un nombre valido")
  else: 
      break  
while True:
    try:
        precio = float(input("Ingresa el precio del producto: "))
        if precio <= 0:
           print("el precio debe ser mayor a 0")
        else:
           break
    except ValueError: 
       print("Ingresa un valor valido")

while True: 
   try:      
       cantidad = int(input("Cantidad del producto: "))
       if cantidad <= 0:
            print("Ingresa minimo 1 producto")  
       else: 
            break
   except ValueError:    
      print ("Ingresa un valor valido")

#se realiza la operacion 
costo_total = cantidad * precio

#se muestra en consola los resultados.
print(f"{nombre}| Precio Unitario {precio} | Cantidad {cantidad} | Precio Total {costo_total}.")


