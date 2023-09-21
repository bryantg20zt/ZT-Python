#EJ. 5 Equipo 4: Mostrar de n cadenas, las palabras utilizadas en la cadena en órden alfabético y los numeros hasta el final
def MostrarPalabras(lista):
    arrCadena = ''
    for x in lista:
        arrCadena += x + ' '
    listaOrd = sorted(arrCadena.lower().split(' '))
    palabras = ''
    numeros = ''
    #arrCadena = cadena.lower().split(' ')
    for i in listaOrd:
        if i.isnumeric():
            numeros += i + ' '
        else:
            palabras += i + ' '
    print(palabras + numeros)
cadena = []
cantCadenas = 0
while True:
    cadena.append(input(f'Ingrese la cadena num {cantCadenas + 1}: '))
    cantCadenas += 1
    if cantCadenas != 1:
        while True:
            resp = input("¿Desea mostrar las todas las palabras utilizadas hasta ahora? (y/n): ")
            if resp.lower() != 'y' and resp.lower() != 'n':
                print('Error, respuesta inválida, ingrese su respuesta de nuevo.')
            else:
                break
        if resp.lower() == 'y':
            if cantCadenas == 1:
                print('Favor de ingresar una cadena más.')
            else:
                MostrarPalabras(cadena)
                break
