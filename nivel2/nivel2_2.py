#Número positivo, negativo o cero

numero = float(input("ingresa un número: ")) #se pide el número

if numero > 0: print(f"el número {numero} es positivo") #condición 1, si el número es mayor a cero se muestra que es positivo
elif numero == 0: print(f"el número {numero} es igual a cero") #condición 2, si no se cumple la primera condición, se verifica
                                                             #la segunda condición, si se cumple, se muesta que es cero
else: print(f"el número {numero} es negativo")               #si no se cumple ni la primera ni la segunda condicón, por tricotomia en los reales
                                                             #no es necesario verificar una tercera condición, se muestra que es negativo