try:
    def CreaMatriz() -> list:
        M = []
        x = 1
        i = 0
        while i < dim:      #Crea la matriz
            a = 0
            lista = []
            while a < dim:
                lista.append(x)
                a += 1
                x += 1
            M.append(lista)
            i += 1
        return M
    
    def LlenaMatrizCaracol(Mat) -> list:
        cont = 1
        a = 0
        while a < (dim // 2):
            x = a
            while x < (dim - a - 1):
                Mat[a][x] = cont
                cont += 1
                x += 1
            y = a
            while y < (dim - a - 1): 
                Mat[y][dim - a - 1] = cont
                cont += 1
                y += 1
            z = dim - a - 1
            while z > a:
                Mat[dim - a - 1][z] = cont
                cont += 1
                z -= 1
            w = dim - a - 1
            while w > a:
                Mat[w][a] = cont
                w -= 1
                cont += 1
            a += 1
        if (dim % 2 == 1):
            Mat[dim//2][dim//2] = cont
        return Mat
    
    dim = int(input("Ingrese el número de las dimensiones de la matriz(N): "))
    if dim >= 2 and dim <= 10:
        Matriz = CreaMatriz()
        print("Matriz Automática: ")
        for a in Matriz:
            print(a)
        Caracol = LlenaMatrizCaracol(Matriz)
        print("Matriz en forma de caracol: ")
        for b in Caracol:
            print(b)
    else:
        print("El valor ingresado no se encuentra en el rango de las dimensiones válidas (2 y 10)")
except Exception:
    print("Error, valor no válido")