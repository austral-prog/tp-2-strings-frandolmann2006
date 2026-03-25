def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base = int(input())
    print(f"Base: {base}")
    altura = int(input())
    print(f"Altura: {altura}")

    print(f"Area: {base * altura}")
    print(f"Perimetro: {2*(base+altura)}")
