matriz = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

def ejr1(i):
    if i < len(matriz):
        matriz[i].append(sum(matriz[i]))
        ejr1(i+1)
    return matriz

def ejr2(cadena):
    if len(cadena) >= 3 and len(cadena) < 10:
        return True
    else:
        return False

def ejr3(lista, a, b, c):
    for i in range(a,b+1, c):
        lista.append(i)
    return lista

def tabla(a,b):
    lista = []
    if 1<=a<=9 and 1<=a<=9:
        for i in range(0,a):
            lista.append([])
        for i in range(0,a):
            for j in range(0,b):
                lista[i].append([])
    return lista