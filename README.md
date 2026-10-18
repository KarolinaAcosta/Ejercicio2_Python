# Sistema de supermercado

Aplicacion de consola en Python para registrar clientes, agregar productos a un carrito, procesar pagos y generar una factura. El inventario se actualiza al terminar una compra normal.

## Requisitos

- Python 3 instalado.
- No requiere instalar paquetes externos.

## Como ejecutar

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python principal.py
```

Al iniciar, elige uno de estos modos:

- **1 - Compra normal:** realiza el proceso completo y genera la factura.
- **2 - Demostracion de error:** permite ingresar datos validos del cliente, un producto disponible y una cantidad valida; despues muestra una excepcion provocada intencionalmente. Este modo es solo para demostrar el manejo del error y no modifica el inventario.

## Flujo de una compra normal

1. Ingresa el nombre y apellido, el documento y responde si el cliente esta afiliado.
2. Escribe el codigo de un producto y la cantidad que deseas comprar.
3. Repite para agregar mas productos. Si agregas de nuevo el mismo codigo, las cantidades se suman.
4. Escribe `FIN` cuando termines de elegir productos.
5. Selecciona `EFECTIVO` o `TARJETA`.
6. Si pagas en efectivo, puedes ingresar el pago en varios montos. El programa indica cuanto falta y calcula el cambio si entregas de mas.
7. Revisa la factura y el inventario actualizado.

El sistema valida los datos del cliente, los codigos de producto, las cantidades disponibles y el medio de pago. Si el carrito queda vacio, no solicita el pago ni genera factura.

## Inventario inicial

| Codigo | Producto | Precio | Existencias |
|---|---|---:|---:|
| A01 | Arroz 1 kg | $4.800 | 25 |
| A02 | Aceite 1 L | $12.500 | 12 |
| B01 | Gaseosa 2 L | $7.200 | 8 |
| B02 | Cerveza six pack | $18.900 | 4 |
| C01 | Jabon en polvo | $15.400 | 0 (agotado) |
| C02 | Papel higienico | $21.000 | 6 |

## Reglas de facturacion

- Se calcula un IVA del 19 % para los productos marcados como gravados.
- Los clientes afiliados reciben un descuento del 5 % sobre el subtotal.
- Los pagos con tarjeta tienen un recargo del 2 %.
- El pago en efectivo acepta varios montos y muestra el cambio correspondiente.
