from inventario import show_inventory
from cliente import create_client

def main():

    print("CAJA REGISTRADORA")

    #Registrar al cliente
    nombre, documento, afiliado = create_client()

main()