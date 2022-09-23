# evaluacion-tema-1

El link a este repositorio es [github](https://github.com/GonzaloGmv/evaluacion-tema-1)

El ejercicio resuelto de codewars:

![codewars](https://user-images.githubusercontent.com/91721237/191991574-326947dd-ef55-4eee-8bfb-fa3fa96a161a.png)

El código de este proyecto es el siguiente:
```
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
        print("No son validos, elija otros: ")
        tabla(int(input("Introduzca el numero de filas: ")), int(input("Introduzca el numero de columnas: ")))
```

Y este es el lanzador:
```
from ejr import printear_matriz, ejr1, ejr2, ejr3, printear_matriz, tabla

def main():
    print("EJERCICIO 1")
    m = ejr1(0)
    printear_matriz(m, 0)
    print("EJERCICIO 2")
    print(ejr2(input("Introduzca el numero que desea analizar: ")))
    print("EJERCICIO 3")
    print(ejr3(0, 10,1))
    print(ejr3(-10, 0,1))
    print(ejr3(0, 20, 2))
    print(ejr3(-19, 0, 2))
    print(ejr3(0, 50, 5))
    print("EJERCICIO 4")
    tabla(int(input("Introduzca el numero de filas: ")), int(input("Introduzca el numero de columnas: ")))
```

Que se ejecuta en el main:
```
from lanzador import main

if __name__ == "__main__":
    main()
```    
