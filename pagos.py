#FUNCION DE PAGOS

def request_payment():
    while True:
        medio_pago = input(
            "Medio de pago (EFECTIVO/TARJETA): "
        ).strip().upper()

        if medio_pago in ("EFECTIVO", "TARJETA"):
            return medio_pago

        print("ERROR: Elija un medio de pago EFECTIVO o TARJETA.")

def process_payment (total, medio_pago):
    if medio_pago != "EFECTIVO":
        return 0, 0

    entregado = 0

    while True:
        if entregado == 0:
            monto_texto = input("Monto entregado: $").strip()
        else:
            monto_texto = input("Ingrese otro monto para completar el pago: $").strip()

        if not monto_texto.isdigit():
            print("Error: ingrese un monto entero valido.")
            continue

        monto = int(monto_texto)
        if monto <= 0:
            print("Error: ingrese un monto mayor que cero.")
            continue

        entregado += monto
        if entregado < total:
            print("El dinero no es suficiente.")
            print("Falta $", round(total - entregado))
            continue

        return entregado, round(entregado - total)
