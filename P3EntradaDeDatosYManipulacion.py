#3 Entrada de datos y manipulación - Equipo 4
nombre = input("Ingrese su nombre completo: ")
while str(type(nombre)) != "<class 'str'>":     #Si el valor ingresado no es una cadena, pide el nombre de nuevo
    nombre = input("Error! Ingrese su nombre completo: ")
nombre = nombre[::-1]   #Invierte el orden de la cadena
b = 0
for a in nombre:
    if (b % 2 == 0):
        print(a.upper(),end=' ')    #Si es par, imprime el caracter en mayúscula
    else:
        print(a.lower(),end=' ')    #Si es impar, imprime el caracter en minúscula
    b += 1      #Posición del caracter
    