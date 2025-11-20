#Cajero automático
saldo = 1000
while True:
    print("\n1. Consultar saldo\n2. Depositar\n3. Retirar\n4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        print("Saldo actual:", saldo)
    elif opcion == "2":
        monto = float(input("Monto a depositar: "))
        saldo += monto
    elif opcion == "3":
        monto = float(input("Monto a retirar: "))
        if monto <= saldo:
            saldo -= monto
        else:
            print("Saldo insuficiente.")
    elif opcion == "4":
        print("Gracias por usar el cajero.")
        break
    else:
        print("Opción no válida.")