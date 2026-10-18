from inventario import inventario
from cliente import create_client
from carrito import buy_products
from facturacion import calculate_total, show_invoice, update_inventory
from pagos import (process_payment, request_payment)


def main():
    print("CAJA REGISTRADORA")
    print("==========================")

    # Registrar al cliente
    nombre, documento, afiliado = create_client()

    # Construir el carrito
    carrito = buy_products(inventario)

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