# 2- Se requiere hacer un programa que indique cual es mayor de 2 numeros con 3 digitos(cada uno) pero hay un problema con la interfaz y esta toma los numeros al reves
# casos: n1 = 734, n2 = 893 salida = 437


def determinarMayor(n1, n2):
    try:
        if determine3DigitsNumber(n1) and determine3DigitsNumber(n2):
          correctDigit1 = int(reverseDigits(str(n1)))
          correctDigit2 = int(reverseDigits(str(n2)))
          return correctDigit1 if correctDigit1 > correctDigit2 else correctDigit2
        else:
            print('Los numeros ingresados deben de ser de 3 digitos')
    except:
        print("Debe ingresar un numero como parametros")


def reverseDigits(n):
    contador = len(n) - 1
    reversedString = ""
    for digit in n:
        reversedString += n[contador]
        contador = contador - 1
    return reversedString


def determine3DigitsNumber(num):
    return len(str(num)) == 3


print(determinarMayor(734, 893))
print(determinarMayor(221, 231))
