 #vamos a calcular el nuevo salario de un trabajador que obtuvo un aumento del salario delx%
 
 #necesitamos el salario aactual y el aumento del porcentaje
 
def consultarincremento (salario,x):
    nuevosalario= salario + (salario*(x/100))
    return nuevosalario
salarioactual = float(input("cuanto ganas actualemnte"))
incremento = float(input("cuanto aunemta el salario"))

nuevoSALARIO = consultarincremento(salarioactual,incremento)
print(nuevoSALARIO)