import json
import os
from datetime import datetime

DATA_FILE = "cajero_data.json"
DEFAULT_DATA = {
    "pin": "1234",
    "balance": 1000.00,
    "history": []  # list of {"type":"retiro"/"deposito"/"pin","amount":x,"date":...,"desc":...}
}

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return DEFAULT_DATA.copy()

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def format_money(x):
    return f"${x:,.2f}"

def add_history(data, tipo, amount=0.0, desc=""):
    data["history"].append({
        "type": tipo,
        "amount": round(float(amount), 2),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "desc": desc
    })
    # keep last 50
    data["history"] = data["history"][-50:]

def input_amount(prompt):
    while True:
        s = input(prompt).strip()
        try:
            val = float(s.replace(",", "."))
            if val <= 0:
                print("Ingresa un monto mayor que 0.")
                continue
            return round(val, 2)
        except ValueError:
            print("Entrada inválida. Intenta de nuevo (ej: 150.50).")

def authenticate(data, max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        pin = input("Ingresa tu PIN: ").strip()
        if pin == data["pin"]:
            return True
        attempts += 1
        print(f"PIN incorrecto. Intentos restantes: {max_attempts - attempts}")
    print("Número máximo de intentos alcanzado. Sesión bloqueada.")
    return False

def consultar_saldo(data):
    print(f"Saldo disponible: {format_money(data['balance'])}")

def retirar(data):
    if data["balance"] <= 0:
        print("Saldo insuficiente.")
        return
    monto = input_amount("Monto a retirar: ")
    if monto > data["balance"]:
        print("No tienes suficiente saldo para retirar esa cantidad.")
        return
    # Opcional: limites por transacción
    limite = 1000.00
    if monto > limite:
        print(f"El límite por transacción es {format_money(limite)}.")
        return
    data["balance"] = round(data["balance"] - monto, 2)
    add_history(data, "retiro", monto, f"Retiro cajero")
    save_data(data)
    print(f"Retiro exitoso. Nuevo saldo: {format_money(data['balance'])}")

def depositar(data):
    monto = input_amount("Monto a depositar: ")
    data["balance"] = round(data["balance"] + monto, 2)
    add_history(data, "deposito", monto, "Depósito en cuenta")
    save_data(data)
    print(f"Depósito realizado. Nuevo saldo: {format_money(data['balance'])}")

def cambiar_pin(data):
    actual = input("Ingresa tu PIN actual: ").strip()
    if actual != data["pin"]:
        print("PIN actual incorrecto.")
        return
    nuevo = input("Nuevo PIN (4 dígitos): ").strip()
    if not (nuevo.isdigit() and 4 <= len(nuevo) <= 6):
        print("PIN inválido. Debe ser numérico (4-6 dígitos).")
        return
    confirmar = input("Confirma el nuevo PIN: ").strip()
    if nuevo != confirmar:
        print("Los PIN no coinciden.")
        return
    data["pin"] = nuevo
    add_history(data, "pin", 0.0, "Cambio de PIN")
    save_data(data)
    print("PIN actualizado correctamente.")

def mini_extracto(data, n=10):
    if not data["history"]:
        print("No hay movimientos registrados.")
        return
    print(f"\nÚltimos {n} movimientos:")
    for h in reversed(data["history"][-n:]):
        tipo = h["type"].capitalize()
        amt = format_money(h["amount"]) if h["amount"] else ""
        print(f"{h['date']} | {tipo:8} | {amt:10} | {h['desc']}")
    print()

def main_menu():
    data = load_data()
    print("==== Bienvenido al Cajero Automático ====")
    if not authenticate(data):
        return
    while True:
        print("\n--- Menú ---")
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Cambiar PIN")
        print("5. Mini extracto")
        print("0. Salir")
        opt = input("Elige una opción: ").strip()
        if opt == "1":
            consultar_saldo(data)
        elif opt == "2":
            retirar(data)
        elif opt == "3":
            depositar(data)
        elif opt == "4":
            cambiar_pin(data)
        elif opt == "5":
            mini_extracto(data)
        elif opt == "0":
            print("Gracias por usar el cajero. Hasta luego.")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main_menu()
