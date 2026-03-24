def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    pass

    multilinea="""    ========================
    FICHA DEL ALUMNO
    ========================"""
    print(multilinea)

    nombre=input("ingrese su nombre completo: ")

    print(nombre.title())

    email=(input("ingrese su email: "))
    print(email.lower())
    print(f"caracteres en nombre: {len(nombre)}")

    lugar=int(nombre.find(" "))
    print(f"iniciales : {nombre[0].upper()+ nombre[lugar+1].upper()}")

    print(f"usuario: {nombre.lower()[lugar+1:]+"."+ nombre.lower()[:lugar]}")
    print(f"Email valido:{ '@' in email}")
    arroba=email.find('@')
    print(f"Dominio: {email[arroba+1:].lower()}")
    print(f"Nombre para archivo: {nombre.replace(' ','_').title()}")

    cantidad_de_a=nombre.lower().count("a")
    print(f"Cantidad de a: {cantidad_de_a}")
    print(f"codigo secreto: {nombre[::-1]}.".upper())

    n1=input("Nota 1: ")
    n2=input("Nota 2: ")
    n3=input("Nota 3: ")


    nota1=int(n1)
    nota2=int(n2)
    nota3=int(n3)

    suma=nota1 + nota2 + nota3
    promedio=suma / 3
    promedio_entero=int(suma // 3)

    print(suma)
    print(promedio)
    print(promedio_entero)

    
    print("=" * 24)
