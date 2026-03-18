def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""

    print(nombre.strip())
    print(nombre.lstrip())
    print(nombre.rstrip())

    print(frase.upper())
    print(frase.lower())
    print(frase.title())

    print(f"find: {frase.find('gran')}")
    print(f"replace: {frase.replace('programacion', 'desarrollo')}")

    print(f"count: {frase.count('a')}")

    print(f"contiene Python: {'Python' in frase}")
    print(f"contiene Java: {'Java' in frase}")

    python = frase[0:6]
    print(f"slice: {python}")

    print(f"paso: {python[::2]}")

    print(python[::-1])

    print(f"Formato: {nombre.strip()} sabe Python")

    print(multilinea)
