#Cajero automático.

saldoActual = 5123421.0                                           

print("bienvenido a Riwibank\n ¿qué te gustaría hacer hoy?\n")
while True:
    print("1: Consultar saldo  ")
    print("2: Retirar saldo ")
    print("3: Enviar saldo ")
    print("4: Depositar saldo ")
    print("5: Salir ")
    
    option = int(input("\n"))

    match option:
        case 1:
            print(f"Saldo actual: {saldoActual}")
        case 2:
            saldoPorRetirar = int(input("¿cuanto saldo quieres retirar? " ))
            if saldoActual >= saldoPorRetirar:
                saldoActual -= saldoPorRetirar
                print("Retiro efectivo")
                print(f"Saldo actual: {saldoActual}")
            else: print("Error: No tienes suficientes fondos")
        case 3:
            saldoPorEnviar = int(input("¿Cuanto saldo quieres enviar? "))
            cuenta = int(input("Número de cuenta: "))
            if saldoActual >= saldoPorEnviar:
                saldoActual -= saldoPorEnviar
                print("Transferencia efectiva")
                print(f"Saldo actual: {saldoActual}")
            else: print("Error: No tienes suficientes fondos")

        case 4:
            saldoPorDepositar = int(input("¿cuanto saldo quieres depositar? " ))
            saldoActual += saldoPorDepositar
            print("Depósito efectivo")
            print(f"Saldo actual: {saldoActual}")
             
        case 5:
            print("Gracias por usar nuestro servicio "); break
        case _:
            print("Opción inválida")
    print("\nRiwibank\n")


            
    