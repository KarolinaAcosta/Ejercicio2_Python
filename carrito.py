from inventario import show_inventory

def buy_products(inventario):
    carrito = []

    while True:
        show_inventory(inventario, carrito)

        codigo = input("Codigo del producto o FIN para terminar: ").strip().upper()

        if codigo == "FIN":
            break

        producto_encontrado = None

        for producto in inventario:
            if producto["codigo"] == codigo:
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("Error: el codigo no existe.")
            continue

        item_encontrado = None

        for item in carrito:
            if item["codigo"] == codigo:
                item_encontrado = item
                break

        reservado = item_encontrado["cantidad"] if item_encontrado else 0
        disponible = producto_encontrado["stock"] - reservado

        if disponible <= 0:
            print("Producto Agotado")
            continue

        while True:
            try:
                cantidad = int(input("Cantidad que deseas comprar: ").strip())

                if cantidad <= 0:
                    print("Error: ingresa un entero mayor que cero.")
                elif cantidad > disponible:
                    print(f"Error: solo hay {disponible} unidades disponibles.")
                else:
                    break
            except ValueError:
                print("Error: ingresa un número entero.")

        if item_encontrado is not None:
            item_encontrado["cantidad"] += cantidad
            print("Cantidad actualizada en el carrito.")
        else:
            nuevo_item = {
                "codigo": producto_encontrado["codigo"],
                "producto": producto_encontrado["producto"],
                "precio": producto_encontrado["precio"],
                "cantidad": cantidad,
                "grava_iva": producto_encontrado["grava_iva"],
            }

            carrito.append(nuevo_item)
            print("Producto agregado al carrito.")

    return carrito