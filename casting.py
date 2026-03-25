def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""


    precio=int(input())
    print(f"Precio: {precio}")
    descuento=float(input())
    print(f"Descuento: {descuento}")
    cantidad=int(input())

    precio_con_descuento=float(precio-descuento)
    print(f"Precio con descuento: {precio_con_descuento}")
    total=precio_con_descuento*cantidad
    print(f"Total: {total}")
