import json
import csv
import os
from datetime import datetime

CATALOG = {
    1: {"name": "Camiseta", "price": 25.00},
    2: {"name": "Pantalón", "price": 40.50},
    3: {"name": "Zapatillas", "price": 79.90},
    4: {"name": "Gorra", "price": 15.00},
    5: {"name": "Mochila", "price": 55.75},
}

CART = {}
TAX_RATE = 0.19
DEFAULT_CART_FILE = "carrito.json"

def format_money(amount):
    return f"${amount:,.2f}"

def input_int(prompt, min_val=None, max_val=None):
    while True:
        s = input(prompt).strip()
        if s == "":
            return None
        try:
            v = int(s)
            if (min_val is not None and v < min_val) or (max_val is not None and v > max_val):
                print(f"Ingresa un número entre {min_val} y {max_val}.")
                continue
            return v
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

def input_float(prompt, min_val=None, max_val=None):
    while True:
        s = input(prompt).strip()
        if s == "":
            return None
        try:
            v = float(s.replace(",", "."))
            if (min_val is not None and v < min_val) or (max_val is not None and v > max_val):
                print(f"Ingresa un número entre {min_val} y {max_val}.")
                continue
            return v
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")

def mostrar_catalogo():
    print("\n--- CATÁLOGO ---")
    for pid, info in CATALOG.items():
        print(f"{pid}. {info['name']} - {format_money(info['price'])}")
    print()

def agregar_al_carrito():
    mostrar_catalogo()
    pid = input_int("Id del producto a añadir (enter para cancelar): ")
    if pid is None:
        return
    if pid not in CATALOG:
        print("Producto no existe.")
        return
    qty = input_int("Cantidad: ", 1, 1000)
    if qty is None:
        return
    CART[pid] = CART.get(pid, 0) + qty
    print(f"Añadido {qty} x {CATALOG[pid]['name']} al carrito.")

def actualizar_cantidad():
    if not CART:
        print("Carrito vacío.")
        return
    ver_carrito()
    pid = input_int("Id del producto a actualizar (enter para cancelar): ")
    if pid is None:
        return
    if pid not in CART:
        print("Ese producto no está en el carrito.")
        return
    qty = input_int("Nueva cantidad (0 para eliminar): ", 0, 1000)
    if qty is None:
        return
    if qty == 0:
        del CART[pid]
        print("Producto eliminado del carrito.")
    else:
        CART[pid] = qty
        print(f"Cantidad actualizada: {qty} x {CATALOG[pid]['name']}")

def eliminar_producto():
    if not CART:
        print("Carrito vacío.")
        return
    ver_carrito()
    pid = input_int("Id del producto a eliminar (enter para cancelar): ")
    if pid is None:
        return
    if pid in CART:
        del CART[pid]
        print("Producto eliminado.")
    else:
        print("Producto no encontrado en el carrito.")

def ver_carrito():
    if not CART:
        print("\nEl carrito está vacío.\n")
        return
    print("\n--- CARRITO ---")
    subtotal = 0.0
    for pid, qty in CART.items():
        prod = CATALOG.get(pid, {"name": "Desconocido", "price": 0.0})
        line_total = prod["price"] * qty
        subtotal += line_total
        print(f"{pid}. {prod['name']} | {qty} x {format_money(prod['price'])} = {format_money(line_total)}")
    print(f"SUBTOTAL: {format_money(subtotal)}")
    print()

def calcular_totales(desc_porcentaje=0.0, aplicar_iva=True):
    subtotal = 0.0
    for pid, qty in CART.items():
        price = CATALOG.get(pid, {"price": 0.0})["price"]
        subtotal += price * qty
    descuento = subtotal * (desc_porcentaje / 100.0)
    subtotal_desc = subtotal - descuento
    iva = subtotal_desc * TAX_RATE if aplicar_iva else 0.0
    total = subtotal_desc + iva
    return {
        "subtotal": subtotal,
        "descuento": descuento,
        "subtotal_desc": subtotal_desc,
        "iva": iva,
        "total": total
    }

def checkout():
    if not CART:
        print("Carrito vacío. Nada que cobrar.")
        return
    print("\n--- CHECKOUT ---")
    ver_carrito()
    desc = input_float("Descuento porcentual a aplicar (ej: 10) o enter para 0: ", 0, 100) or 0.0
    aplicar_iva = input("Aplicar IVA (s/n, default s): ").strip().lower() != "n"
    tot = calcular_totales(desc_porcentaje=desc, aplicar_iva=aplicar_iva)
    print(f"Subtotal: {format_money(tot['subtotal'])}")
    print(f"Descuento ({desc}%): -{format_money(tot['descuento'])}")
    print(f"Subtotal con descuento: {format_money(tot['subtotal_desc'])}")
    print(f"IVA ({'sí' if aplicar_iva else 'no'}): {format_money(tot['iva'])}")
    print(f"TOTAL A PAGAR: {format_money(tot['total'])}")
    confirmar = input("Confirmar compra? (s/n): ").strip().lower()
    if confirmar == "s":
        guardar_ticket(tot)
        CART.clear()
        print("Compra realizada. Carrito vaciado.")
    else:
        print("Compra cancelada.")

def guardar_ticket(totales):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"ticket_{now}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("TICKET DE COMPRA\n")
        f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("-" * 40 + "\n")
        for pid, qty in CART.items():
            prod = CATALOG.get(pid, {"name": "Desconocido", "price": 0.0})
            f.write(f"{prod['name']} x{qty} @ {format_money(prod['price'])} = {format_money(prod['price']*qty)}\n")
        f.write("-" * 40 + "\n")
        f.write(f"Subtotal: {format_money(totales['subtotal'])}\n")
        f.write(f"Descuento: -{format_money(totales['descuento'])}\n")
        f.write(f"IVA: {format_money(totales['iva'])}\n")
        f.write(f"TOTAL: {format_money(totales['total'])}\n")
    print(f"Ticket guardado en '{filename}'.")

def exportar_csv(ruta=None):
    if not CART:
        print("Nada para exportar.")
        return
    ruta = ruta or f"carrito_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(ruta, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Id", "Nombre", "Cantidad", "Precio unitario", "Total"])
        for pid, qty in CART.items():
            prod = CATALOG.get(pid, {"name": "Desconocido", "price": 0.0})
            writer.writerow([pid, prod["name"], qty, f"{prod['price']:.2f}", f"{prod['price']*qty:.2f}"])
    print(f"Exportado a CSV: {ruta}")

def guardar_carrito_json(path=DEFAULT_CART_FILE):
    data = {"cart": CART, "timestamp": datetime.now().isoformat()}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Carrito guardado en '{path}'.")

def cargar_carrito_json(path=DEFAULT_CART_FILE):
    if not os.path.exists(path):
        print("No existe archivo de carrito guardado.")
        return
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    loaded = data.get("cart", {})
    CART.clear()
    for k, v in loaded.items():
        try:
            CART[int(k)] = int(v)
        except Exception:
            pass
    print(f"Carrito cargado desde '{path}'.")

def menu():
    opciones = {
        "1": ("Mostrar catálogo", mostrar_catalogo),
        "2": ("Añadir producto al carrito", agregar_al_carrito),
        "3": ("Actualizar cantidad / Eliminar", actualizar_cantidad),
        "4": ("Eliminar producto (por id)", eliminar_producto),
        "5": ("Ver carrito", ver_carrito),
        "6": ("Checkout / Pagar", checkout),
        "7": ("Exportar carrito a CSV", exportar_csv),
        "8": ("Guardar carrito (JSON)", guardar_carrito_json),
        "9": ("Cargar carrito (JSON)", cargar_carrito_json),
        "0": ("Salir", None),
    }
    while True:
        print("\n=== CARRITO DE COMPRAS ===")
        for k, (desc, _) in opciones.items():
            print(f"{k}. {desc}")
        elec = input("Elige una opción: ").strip()
        if elec == "0":
            print("Saliendo. ¡Hasta luego!")
            break
        if elec in opciones:
            func = opciones[elec][1]
            if func:
                func()
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
