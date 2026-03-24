def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio=int(input())
    descuento=float(input())
    cantidad=int(input())

    precio_con_descuento=float(precio-descuento)
    print(precio_con_descuento)
    total=precio_con_descuento*cantidad
    print(total)
