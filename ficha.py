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
    nombre_completo = input("Ingrese el nombre completo del alumno : ").strip().title()
    email = input("Ingrese el email del alumno: ")
    nota_1 = input("Ingrese nota : ")
    nota_2 = input("Ingrese nota : ")
    nota_3 = input("Ingrese nota : ")

    encabezado = "    FICHA DEL ALUMNO"

    index_mail = int(email.find("@"))+1
    dominio = email[index_mail:].lower()


    index_nombre = nombre_completo.find(" ")
    nombre = nombre_completo[0:index_nombre].strip()
    apellido = nombre_completo[index_nombre:].strip()
    iniciales = nombre.upper()[0] + apellido.upper()[0]
    usuario = apellido.lower() + "." + nombre.lower()

    codigo_secreto =  nombre_completo.upper()[::-1]

    suma_notas = int(nota_1) + int(nota_2) + int(nota_3)
    promedio = suma_notas / 3
    promedio_entero = suma_notas // 3


    print("=" * 24)
    print(encabezado)
    print("=" * 24)

    print(f"Nombre: { nombre_completo}")
    print(f"Email: {email.strip().lower()}")
    print(f"Caracteres en nombre: {len(nombre_completo)}")
    print(f"Iniciales: {iniciales   }")
    print(f"Usuario: {usuario}")
    print(f"Email valido: {"@" in email}")
    print(f"Dominio: {dominio}")
    print(f"Nombre para archivo: { nombre_completo.strip().title().replace(" ", "_")}")
    print(f"Cantidad de a: { nombre_completo.count("a")}")
    print(f"Codigo secreto: {codigo_secreto}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {suma_notas}")
    print(f"Promedio: {promedio}")
    print(f"Promedio entero: {promedio_entero}")

    print("=" * 24)
