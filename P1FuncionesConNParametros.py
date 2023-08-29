def nParametros(*nParameters):
    sumaTotal = 0
    productoTotal = 1
    for number in nParameters:
        sumaTotal += number
        productoTotal *= number
    return { sumaTotal, productoTotal}

print(nParametros(1,2,3,4,5,6))