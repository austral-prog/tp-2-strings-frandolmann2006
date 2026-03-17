def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = int(input("ponga el precio: "))
    descuento = float(input("ponga el descuento: "))
    cantidad = int(input("cuantos queres?: "))

    precio_con_descuento = float(precio-descuento)
    print(precio_con_descuento)
    total = precio_con_descuento*cantidad
    print(total)
