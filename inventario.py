# INVENTARIO BASE

inventario = [
    {"codigo": "A01", "producto": "Arroz 1kg",
     "precio": 4800, "stock": 25, "grava_iva": False},
    {"codigo": "A02", "producto": "Aceite 1L",
     "precio": 12500, "stock": 12, "grava_iva": False},
    {"codigo": "B01", "producto": "Gaseosa 2L",
     "precio": 7200, "stock": 8, "grava_iva": True},
    {"codigo": "B02", "producto": "Cerveza six pack",
     "precio": 18900, "stock": 4, "grava_iva": True},
    {"codigo": "C01", "producto": "Jabón en polvo",
     "precio": 15400, "stock": 0, "grava_iva": True},
    {"codigo": "C02", "producto": "Papel higiénico",
     "precio": 21000, "stock": 6, "grava_iva": True},
]

#FUNCION MOSTRAR INVENTARIO

def show_inventory(inventario, carrito):
    print("INVENTARIO DE PRODUCTOS")
    print("-----------------------")

    for producto in inventario:
        reservado = 0
        for item in carrito:
            if item["codigo"] == producto["codigo"]:
                reservado = item["cantidad"]

        disponible = producto["stock"] - reservado

        if disponible <= 0:
            estado = "Agotado"
        else:
            estado = str(disponible) + " unidades disponibles"

        print(
            producto["codigo"], " | ",
            producto["producto"], " | $",
            producto["precio"], " | ", estado
        )