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


    print("========================")
    print("    FICHA DEL ALUMNO")
    print("========================")

    nombre=input().strip()

    print(f"Nombre: {nombre.title()}")

    email=(input())
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombre)}")


    print(f"Iniciales: {nombre[0].upper()+ nombre[(nombre.find(' '))+1].upper()}")

    print(f"Usuario: {nombre.lower()[(nombre.find(' '))+1:]+'.'+ nombre.lower()[:(nombre.find(' '))]}")
    print(f"Email valido: { '@' in email}")
    arroba=email.find('@')
    print(f"Dominio: {email[arroba+1:].lower()}")
    print(f"Nombre para archivo: {nombre.replace(' ','_').title()}")

    cantidad_de_a=nombre.lower().count("a")
    print(f"Cantidad de a: {cantidad_de_a}")
    print(f"Codigo secreto: {nombre[::-1].upper()}")

    n1=input()
    n2=input()
    n3=input()

    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")



    nota1=int(n1)
    nota2=int(n2)
    nota3=int(n3)

    suma=nota1 + nota2 + nota3
    promedio=suma / 3
    promedio_entero=int(suma // 3)

    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")

    print("=" * 24)
