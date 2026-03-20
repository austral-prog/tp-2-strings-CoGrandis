def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    pass
    gasto = float(input("Ingresar el gasto: "))
    dinero_recibido = int(input("Dinero recibido: "))

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)


    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = round((vuelto - pesos)* 100)
    
    print("\nVuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
