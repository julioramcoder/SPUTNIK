#Mayor de edad

edad = int(input("ingresa tu edad actual: ")) #pide la edad del usuario
mensaje = "mayor" if edad >= 18 else "menor" #mensaje puede ser "mayor" o "menor" depende del resultado del operador ternario
print(f"eres {mensaje} de edad") #muestra al usuario es o no mayor de edad