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