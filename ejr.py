matriz = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

def suma(i):
    if i < len(matriz):
        matriz[i].append(sum(matriz[i]))
        suma(i+1)
    return matriz

matriz = suma(0)
for i in range(0, len(matriz)):
    print(matriz[i])
