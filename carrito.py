from inventario import show_inventory

def buy_products(inventario):
    carrito = []  #carrito vacio

    while True:
        show_inventory(inventario, carrito) #mostrar el inventario antes

        codigo= input("Codigo del producto o Fin para terminar")

        if codigo == "FIN": #termina la seleccion del producto
            break

        producto_encontrado = None #Buscar el producto

        for producto in inventario:
            if producto["codigo"] == codigo: 
                producto_encontrado = producto

            #Comprobar si el producto existe

        if producto_encontrado is None:
            print ("Error: el codigo no existe.")
            continue

            # Buscar si el item ya esta en el carrito
        item_encontrado = None

        for item in carrito:
            if item["codigo"] == codigo:
                item_encontrado = item

            # Calcular las unidades reservadas
        
        reservado = 0

        if item_encontrado is not None:
            reservado=item_encontrado["cantidad"]

        disponible = producto_encontrado["stock"] - reservado

            # Comprobar si hay stock

        if disponible <= 0:
            print("Producto Agotado")
            continue

            #Solicitar cantidad y validar contra stock disponible
        
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

            #  Acomular o agregar el producto

        if item_encontrado is not None:
            item_encontrado["cantidad"] += cantidad
            print("Cantidad actualizada en carrito")
        else:
            nuevo_item = {
                "codigo": producto_encontrado["codigo"],
                "producto":producto_encontrado["producto"],
                "precio": producto_encontrado["precio"],
                "cantidad":cantidad,
                "grava IVA": producto_encontrado["grava IVA"]
            }

            carrito.append(nuevo_item)
            print("Producto agregado al carrito")

        return carrito