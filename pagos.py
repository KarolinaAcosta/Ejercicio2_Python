#FUNCION DE PAGOS

def request_payment():
    medio_pago = input(
        "Medio de pago (EFECTIVO/TARJETA):"
    ).strip().upper()

    while medio_pago not in ["EFECTIVO" , "TARJETA"]:
        print("ERROR: Elija un medio de pago EFECTIVO o TARJETA")

        medio_pago = input(
            "Medio de pago (EFECTIVO / TARJETA):"
        ).strip().upper()

        return medio_pago

def process_payment (total, medio_pago):
    entregado = 0
    cambio = 0

    if medio_pago == "EFECTIVO":
        monto_texto = input("Monto entregado: $:").strip()

        while not monto_texto.isdigit():
            print("Error: ingrese un monto entrero valido")
            monto_texto = input("Monto entregado $:").strip()

            entregado = int(monto_texto)

            while entregado < total:
                faltante = total - entregado

                print("El dinero no es suficiente")
                print("Falta $",round(faltante))

                monto_texto = input("Ingrese elmonto total entregado $:").strip()

                while not monto_texto.isdigit():
                    print("Error:Ingrese un monto entero valido")

                    monto_texto= input("Ingrese el monto total entregado: $").strip()

                    entregado = int(monto_texto)

                    cambio = entregado- total
                    
                    return entregado, cambio
