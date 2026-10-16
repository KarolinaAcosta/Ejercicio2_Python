# FUNCION PARA CREAR CLIENTE

def create_client():

    #Solicitar nombre y apellido al cliente
    nombre = input("Ingrese el nombre y apellido del cliente: ").strip()
    while len(nombre.split()) < 2:
        print("Ingrese al menos dos palabras: nombre y apellido.")
        nombre = input("Ingrese el nombre y apellido del cliente: ").strip()
    nombre = nombre.title()

#Solicitar documento del cliente
    documento = input("Ingrese el documento del cliente: ").strip()
    while not documento.isdigit() or not 6 <= len(documento) <= 10:
        print("Error: el documento debe tener entre 6 y 10 dígitos.")
        documento = input("Ingrese el documento del cliente: ").strip()

#Preguntar si es afiliado o no?
    afiliado = input("¿El cliente ya está afiliado? (si/no): ").strip().lower()
    while afiliado not in ("si", "sí", "no"):
        print("Error: responda 'si' o 'no'.")
        afiliado = input("¿El cliente ya está afiliado? (si/no): ").strip().lower()

    if afiliado in ("si", "sí"):
        afiliado = True
        print("Cliente afiliado.")
    else:
        respuesta = input("¿Desea afiliarse ahora? (si/no): ").strip().lower()
        while respuesta not in ("si", "sí", "no"):
            print("Error: responda 'si' o 'no'.")
            respuesta = input("¿Desea afiliarse ahora? (si/no): ").strip().lower()

        afiliado = respuesta in ("si", "sí")
        if afiliado:
            print("Cliente nuevo afiliado.")
        else:
            print("Cliente no afiliado.")

    return nombre, documento, afiliado

create_client()