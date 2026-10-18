from inventario import inventario
from cliente import create_client
from carrito import buy_products
from facturacion import calculate_total, show_invoice, update_inventory
from pagos import (process_payment, request_payment)


def main():
    print("CAJA REGISTRADORA")
    print("==========================")

    while True:
        modo = input(
            "Modo (1: compra normal, 2: demostracion de error): "
        ).strip()
        if modo in ("1", "2"):
            break
        print("Opcion no valida. Escribe 1 o 2.")

    # Registrar al cliente
    nombre, documento, afiliado = create_client()

    # Construir el carrito. En el modo demo, el error ocurre despues de
    # ingresar correctamente un codigo de producto y una cantidad disponible.
    try:
        carrito = buy_products(inventario, demo_error=(modo == "2"))
    except RuntimeError as error:
        print(f"ERROR INTERNO DE DEMOSTRACION: {error}")
        return

    if not carrito:
        print("El carrito esta vacio. No se generara factura al cliente")
        return

    # Solicitar medio de pago
    medio_pago = request_payment()

    subtotal, iva, descuento, recargo, total = calculate_total(
        carrito, afiliado, medio_pago
    )
    entregado, cambio = process_payment(total, medio_pago)

    # Mostrar la factura
    show_invoice(
        nombre, documento, afiliado, carrito, subtotal, iva, descuento,
        recargo, total, medio_pago, entregado, cambio
    )

    # Actualizar el inventario
    update_inventory(inventario, carrito)

if __name__ == "__main__":
    main()