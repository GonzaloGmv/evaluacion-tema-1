matriz = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

def ejr1(i):
    if i < len(matriz):
        matriz[i].append(sum(matriz[i]))
        ejr1(i+1)
    return matriz

def printear_matriz(m, i):
    if i < len(m):
        print(m[i])
        printear_matriz(m, i+1)

def ejr2(cadena):
    if len(cadena) >= 3 and len(cadena) < 10:
        return True
    else:
        return False

def ejr3( a, b, c):
    m = list(range(a,b,c))
    return m

def tabla(a,b):
    if 0 < a < 10 and 0 < b < 10:
        lista = []
        if 1<=a<=9 and 1<=a<=9:
            for i in range(0,a):
                lista.append([])
            for i in range(0,a):
                for j in range(0,b):
                    lista[i].append([])
        printear_matriz(lista, 0)
    else:
        print("No son validos")