from ejr import ejr1, matriz, ejr2, ejr3, tabla

def agrupar():
    print("EJERCICIO 1")
    m = ejr1(0)
    for i in range(0, len(matriz)):
        print(matriz[i])
    print("EJERCICIO 2")
    print(ejr2('0123456789'))
    print("EJERCICIO 3")
    print(ejr3([], 0, 10,1))
    print(ejr3([], -10, 0,1))
    print(ejr3([], 0, 20, 2))
    print(ejr3([], -19, 0, 2))
    print(ejr3([], 0, 50, 5))
    print("EJERCICIO 4")
    t=(tabla(4,3))
    for i in range(0, len(t)):
        print(t[i])