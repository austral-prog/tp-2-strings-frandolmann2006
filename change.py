def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto=float(input("Ingresar gasto: "))
    print(gasto)
    recibido=int(input("Dinero recibido: "))
    print(recibido)

    vuelto=recibido - gasto
    pesos=int(vuelto//1)
    centavos=round((vuelto - pesos) * 100)

    print("Vuelto")
    print(f"Pesos: {pesos}")
    print(f"Centavos: {centavos}")
