# 2- Se requiere hacer un programa que indique cual es mayor de 2 numeros con 3 digitos(cada uno) pero hay un problema con la interfaz y esta toma los numeros al reves
# casos: n1 = 734, n2 = 893 salida = 437


def determinarMayor(n1, n2):
    try:
        if determine3DigitsNumber(n1) and determine3DigitsNumber(n2):
            correctDigit1 = reverseDigits(n1)
            correctDigit2 = reverseDigits(n2)
            return correctDigit1 if correctDigit1 > correctDigit2 else correctDigit2
        else:
            print("Los numeros ingresados deben de ser de 3 digitos")
    except:
        print("Debe ingresar un numero como parametros")


def reverseDigits(n):
    negativeFlag = False
    auxN = str(abs(n))
    if n < 0:
        negativeFlag = True
    contador = len(auxN) - 1
    reversedString = ""
    for digit in auxN:
        reversedString += auxN[contador]
        contador = contador - 1
    return int(reversedString) * -1 if negativeFlag else int(reversedString)

def determine3DigitsNumber(num):
    return len(str(abs(num))) == 3


n1 = int(input("Ingrese n1: \n"))
n2 = int(input("Ingrese n2: \n"))
print(determinarMayor(n1, n2))
