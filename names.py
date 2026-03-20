def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """

    name = input("Ingrese un nombre: ")
    surname = input("Ingrese un apellido: ")

    name_surname = f"{name} {surname}"

    print(name_surname.lower())
    print(name_surname.title())
    print(name_surname.upper())
    print(f"\t{name_surname.lower()}")
