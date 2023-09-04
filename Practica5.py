def imprimir_info(**kwargs):
    for llave, valor in kwargs.items():
        print(f'"{valor}": "{llave}"')

imprimir_info(nombre="Juan", edad=30, ciudad="Madrid")