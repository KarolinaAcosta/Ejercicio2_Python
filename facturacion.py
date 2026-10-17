from datetime import datetime

def calculate_total (carrito, afiliado, medio_pago):
    subtotal = 0
    iva = 0

    for item in carrito:
        total_linea = item["precio"] + item["cantidad"]
        subtotal += total_linea

        if item["grava_iva"]:
            iva += total_linea * 0.19


            # Descuento del 5% para afiliados

        descuento = 0

        if afiliado:
            descuento = subtotal * 0.05

            # Total antes del recargo

        total_base = subtotal + iva - descuento

            # Sumarle el recargo del 2% si paga con tarjeta

        recargo = 0

        if medio_pago == "TARJETA":
            recargo = total_base * 0.02

        total = total_base + recargo

        return subtotal, iva, descuento, recargo, total

def show_invoice (nombre, documento, afiliado, carrito, subtotal, iva, descuento, recargo, total, medio_pago, entregado, cambio):

    fecha = datetime.now().strftime("%d%m%Y%H:%M")

    print("/n========================")
    print("SUPERMERCADO - FACTURA")
    print("/n========================")

    print("Cliente",nombre)
    print("Documento", documento)

    if afiliado:
        print("Cliente afiliado: Si")
    else:
        print("Cliente afiliado: No")

    print("Fecha",fecha)
    print("-------------------------")
    print("DETALLE DE PRODUCTOS")

    for item in carrito:
        total_linea = item["precio"]*item["cantidad"]

        print("Codigo:", item["codigo"])
        print("Producto:", item["producto"])
        print("Cantidad:",item["cantidad"])
        print("Precio unitario $", round(item["precio"]))
        print("Total de linea: $", round(total_linea))
        print("-------------------------")

        print("Subtotal: $", round(subtotal))
        print("IVA: $", round(iva))
        print("Descuento: $", round(descuento))
        print("Recargo: $", round(recargo))
        print("TOTAL A PAGAR: $", round(total))
        print("Medio de pago:", medio_pago)

    if medio_pago == "EFECTIVO":
        print("Monto entregado: $", entregado)
        print("Cambio: $", cambio)

        print("/n========================")

# FUNCION PARA ACTUALIZAR INVENTARIO

def update_inventory (inventario, carrito):
    for item in carrito:
        for producto in inventario:
            if producto["codigo"] == item["codigo"]:
                producto["stock"] == item["cantidad"]

        print("INVENTARIO FINAL")

        for producto in inventario:
            if producto ["stock"] == 0:
                estado = "AGOTADO"
            else:
                estado = str(producto["stock"]) + "unidades"

            print(
                producto["codigo"], "|",
                producto["producto"], "|","$",
                producto["precio"], "|",
                estado
            )

