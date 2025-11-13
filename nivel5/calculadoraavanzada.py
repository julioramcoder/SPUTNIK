import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a < 0:
        return "Error: Raíz de número negativo"
    return math.sqrt(a)

def logaritmo(a, base=10):
    if a <= 0:
        return "Error: Logaritmo no definido para valores ≤ 0"
    return math.log(a, base)

def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def menu():
    while True:
        print("\n--- CALCULADORA AVANZADA ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Logaritmo")
        print("8. Seno")
        print("9. Coseno")
        print("10. Tangente")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        match opcion:
            case "0":
                print("Saliendo de la calculadora.")
                break
            case "1" | "2" | "3" | "4" | "5":
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
                match opcion:
                    case "1":
                        print("Resultado:", sumar(a, b))
                    case "2":
                        print("Resultado:", restar(a, b))
                    case "3":
                        print("Resultado:", multiplicar(a, b))
                    case "4":
                        print("Resultado:", dividir(a, b))
                    case "5":
                        print("Resultado:", potencia(a, b))
            case "6":
                a = float(input("Ingresa el número: "))
                print("Resultado:", raiz_cuadrada(a))
            case "7":
                a = float(input("Ingresa el número: "))
                base = input("Ingresa la base (por defecto 10): ")
                base = float(base) if base else 10
                print("Resultado:", logaritmo(a, base))
            case "8":
                a = float(input("Ingresa el ángulo en grados: "))
                print("Resultado:", seno(a))
            case "9":
                a = float(input("Ingresa el ángulo en grados: "))
                print("Resultado:", coseno(a))
            case "10":
                a = float(input("Ingresa el ángulo en grados: "))
                print("Resultado:", tangente(a))
            case _:
                print("Opción inválida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
